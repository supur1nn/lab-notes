# OSPF

OSPF に関するまとめです。

## RFC

| RFC | 内容 |
| --- | --- |
| RFC 2328 | OSPFv2（IPv4） |
| RFC 5340 | OSPFv3（IPv6） |
| RFC 8665 | OSPF の Segment Routing 拡張 |

## 関連ページ

| ページ | 内容 |
|------|------|
| [勉強記録 2026-10-17](../../study-log/2026-10-17.md) | OSPF の有効化（IOS と IOS XR の違い）、ループバックの広報 |
| [検証：OSPF で広報される経路](../../verification/ospf/advertised-routes.md) | インターフェースで OSPF を有効にしたとき、どんな経路が広報されるか（検証中） |
| [検証：OSPF をループバックだけで有効にしたとき](../../verification/ospf/loopback-only.md) | IOS XR で、ループバックだけで OSPF を有効にしたとき、対向に広報されるか（検証中） |
| [検証：OSPF を物理 IF だけで有効にしたとき](../../verification/ospf/physical-if-only.md) | IOS XR で、物理 IF に OSPF を設定したとき、どんな経路が広報されるか（ルータ間だけ／PC 向けも）（検証中） |
