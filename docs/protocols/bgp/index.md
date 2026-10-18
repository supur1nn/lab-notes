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

## 関連ページ

| ページ | 内容 |
|------|------|
| [検証：CE から受けた経路が PE の VRF に入るまで](../../verification/l3vpn-ce-route-to-vrf.md) | L3VPN で、PE の VRF・VPNv4 テーブルに経路が入る順番（検証前） |
