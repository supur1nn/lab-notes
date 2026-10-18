# BGP

BGP に関するまとめです。

## ケイパビリティの確認：show ip bgp neighbors

`show ip bgp neighbors` で、ネイバーとどのケイパビリティ（機能）をやり取りできているかを確認できる。

```
show ip bgp neighbors <ネイバーのアドレス>
```

出力の `Neighbor capabilities:` の部分を見る。

```
  Neighbor capabilities:
    Route refresh: advertised and received(new)
    Four-octets ASN Capability: advertised and received
    Address family IPv4 Unicast: advertised and received
    Address family VPNv4 Unicast: advertised and received
```

- ケイパビリティは、BGP のセッションを張るとき（OPEN メッセージ）にお互いに伝え合う
- **advertised and received**：自分も相手も対応している → その機能が使える
- **advertised** だけ：自分は対応しているが、相手が対応していない → 使えない
- アドレスファミリー（IPv4 Unicast、VPNv4 Unicast など）もケイパビリティの一つ。両方で有効になっていないと、そのアドレスファミリーの経路はやり取りされない

!!! tip "L3VPN での使いどころ"
    PE 同士で VPNv4 の経路が届かないときは、まずここで `Address family VPNv4 Unicast: advertised and received` になっているかを確認する。片方だけ `advertised` なら、相手側で `address-family vpnv4` の `neighbor ... activate` が抜けている可能性が高い。

## ベストパス選択アルゴリズム

同じ宛先への経路が複数あるとき、BGP は決まった順番で属性を比べて、1つの最適経路（ベストパス）を選ぶ。**上から順に比べて、差がついた時点で決まる**のがポイント。

| 順番 | 比べるもの | 優先されるほう | メモ |
| --- | --- | --- | --- |
| 0 | 経路が使えるか | — | ネクストホップに到達できない経路などは、最初から候補にならない |
| 1 | Weight | 大きいほう | シスコ独自。そのルータの中だけで有効で、他のルータには伝わらない |
| 2 | **Local Preference** | 大きいほう | AS 内の全ルータで共有される。**自 AS から出ていく方向**を決めるのに使う |
| 3 | 自分で発信した経路か | 自分で発信したほう | `network` や `redistribute` で入れた経路 |
| 4 | **AS_PATH の長さ** | 短いほう | 通過する AS の数 |
| 5 | Origin | IGP < EGP < Incomplete | `network` で入れると IGP、`redistribute` で入れると Incomplete |
| 6 | **MED** | 小さいほう | **隣の AS に「こちらから入ってきて」と伝える**ための値。初期設定では、同じ隣接 AS から来た経路同士でしか比べない |
| 7 | eBGP か iBGP か | eBGP | |
| 8 | **ネクストホップまでの IGP コスト** | 小さいほう | AS の出口までの近さ（ホットポテト） |
| 9 | マルチパスの判定 | — | 設定していれば、ここで同等の経路を複数使う |
| 10 | 受け取った順 | 古いほう | eBGP 同士のとき。経路が頻繁に入れ替わるのを防ぐ |
| 11 | ルータ ID | 小さいほう | |
| 12 | クラスタリストの長さ | 短いほう | ルートリフレクタ環境 |
| 13 | ネイバーのアドレス | 小さいほう | 最後の決め手 |

!!! note "自分のメモ"
    実際の設計でよく使って大事なのは、**Local Preference・AS_PATH の長さ・MED・ネクストホップまでの IGP コスト**。

    - **Local Preference**：自 AS から**出ていく**ときにどの出口を使うかを、AS 全体でそろえて決める
    - **AS_PATH の長さ**：他の AS からの入り方を調整したいときに、**入ってきてほしくない側**の経路に、わざと自分の AS を足して長くする（AS-PATH プリペンド）
    - **MED**：隣の AS とつながる回線が複数あるとき、どの回線から**入ってきてほしい**かを伝える
    - **IGP コスト**：ここまでで決まらないときに、AS 内でいちばん近い出口を使う

    Weight はそのルータの中だけの値なので、AS 全体の方針には Local Preference を使う。

参考：[BGP ベストパスアルゴリズムの選択（シスコ）](https://www.cisco.com/c/ja_jp/support/docs/ip/border-gateway-protocol-bgp/13753-25.html)

## BGP マルチパス（maximum-paths）

BGP は通常、ベストパスを1つだけ選ぶ。`maximum-paths` を設定すると、条件を満たす複数の経路をルーティングテーブルに入れて、負荷分散（マルチパス）できる。

```
router bgp 65000
 address-family ipv4
  maximum-paths 2          ← eBGP で学んだ経路のマルチパス
  maximum-paths ibgp 2     ← iBGP で学んだ経路のマルチパス
```

### マルチパスになる条件

ベストパス選択アルゴリズムの、**ネクストホップまでの IGP コスト（順番 8）まで**の属性が、ベストパスとすべて同じであること。

| 一致が必要なもの | 補足 |
| --- | --- |
| Weight | |
| Local Preference | |
| AS_PATH | 長さが同じであること。初期設定では、隣接 AS も同じである必要がある |
| Origin | |
| MED | |
| eBGP か iBGP か | eBGP 同士、または iBGP 同士 |
| ネクストホップまでの IGP コスト | |

!!! note "自分のメモ"
    - マルチパスにしても、**ベストパスは1つのまま**。ネイバーに広報するのもベストパス1つだけで、複数の経路を自分のルーティングテーブルに入れるだけ
    - eBGP と iBGP で設定が分かれている（`maximum-paths` と `maximum-paths ibgp`）
    - 違う AS から来た経路同士でマルチパスにしたいときは、`bgp bestpath as-path multipath-relax` で「AS_PATH の長さが同じなら OK」にゆるめられる

参考：[BGP Multipath（シスコ）](https://docs.manage.security.cisco.com/cdfmc/c_bgp_multipath.html)

## 関連ページ

| ページ | 内容 |
|------|------|
| [検証：CE から受けた経路が PE の VRF に入るまで](../../verification/l3vpn-ce-route-to-vrf.md) | L3VPN で、PE の VRF・VPNv4 テーブルに経路が入る順番（検証前） |
