# OSPF をループバックだけで有効にしたとき

!!! info "検証中"
    結果までは確認済み。理由（考察）はこれから確かめる。進め方は [検証の進め方](../workflow.md) を参照。

- 開始日：2026-10-23（[勉強記録](../../study-log/2026-10-23.md)）
- 関連：[OSPF で広報される経路](advertised-routes.md)（IOSv で、ループバックは OSPF を有効にしないと広報されないことを確認した）

## 問い

**IOS XR で、OSPF をループバックだけで有効にしたとき、ループバックのアドレスは対向のルータに広報されるのか。**

## 構成

CML-Personal（ベアメタル）上の IOS XRv 9000 2台と、PC 役の Desktop 2台。

![ラボ構成図](../../assets/images/2026-10-23-ospf-lab-topology.png)

```mermaid
graph LR
  D1["desktop-1<br/>.1"] -- "192.168.1.0/24<br/>E1 ⇔ G0/1" --- R1["R1<br/>(XRv 9000)"]
  R1 -- "192.168.2.0/24<br/>G0/0 ⇔ G0/0" --- R2["R2<br/>(XRv 9000)"]
  R2 -- "192.168.3.0/24<br/>G0/1 ⇔ E1" --- D0["desktop-0<br/>.1"]
```

| リンク | ネットワーク | 接続 |
| --- | --- | --- |
| desktop-1 - R1 | 192.168.1.0/24 | desktop-1 E1（.1） - R1 G0/0/0/1（.2） |
| R1 - R2 | 192.168.2.0/24 | R1 G0/0/0/0（.1） - R2 G0/0/0/0（.2） |
| R2 - desktop-0 | 192.168.3.0/24 | R2 G0/0/0/1（.2） - desktop-0 E1（.1） |

| ルータ | ホスト名 | OSPF ルータ ID | Loopback0 |
| --- | --- | --- | --- |
| R1 | iOS-XR-R1 | 1.1.1.1 | （ループバックのアドレスを書く） |
| R2 | iOS-XR-R2 | 2.2.2.2 | （ループバックのアドレスを書く） |

## 仮説

- OSPF の設定でループバックを有効にすれば、そのループバックのアドレスが対向のルータに広報されるのではないか

## 設定

OSPF は**ループバックだけ**で有効にした。R1 と R2 をつなぐ G0/0/0/0 は、OSPF に入れていない。

=== "R1"

    ```
    RP/0/RP0/CPU0:iOS-XR-R1#show run router ospf
    router ospf 1
     router-id 1.1.1.1
     area 0
      interface Loopback0
      !
     !
    !
    ```

=== "R2"

    ```
    RP/0/RP0/CPU0:iOS-XR-R2#show run router ospf
    router ospf 1
     router-id 2.2.2.2
     area 0
      interface Loopback0
      !
     !
    !
    ```

- 両方とも `area 0` の中に `interface Loopback0` だけが入っている
- ルータ ID は手動で設定（R1 が 1.1.1.1、R2 が 2.2.2.2）

## 確認

| どこで | コマンド | 何を見るか |
| --- | --- | --- |
| R1 / R2 | `show ospf interface brief` | OSPF が有効になっているインターフェース |
| R1 / R2 | `show ospf neighbor` | 対向とネイバーになっているか |
| R1 / R2 | `show route ospf` | 対向のループバックが OSPF の経路（`O`）として載っているか |
| R1 / R2 | `show ospf database` | どんな LSA を持っているか |

（確認コマンドの出力をここに貼る）

## 結果

- **対向のルータに、ループバックのアドレスは広報されなかった**
- 仮説は外れた

## 考察

（なぜ広報されなかったのか。`show ospf neighbor` と `show ospf database` の出力を根拠に書く）

## 次の問い

- R1 と R2 をつなぐ G0/0/0/0 でも OSPF を有効にすると、ループバックは広報されるか
- `show ospf neighbor` で、ネイバーは今どういう状態か
- ループバックのインターフェースは、OSPF の Hello を送っているのか
