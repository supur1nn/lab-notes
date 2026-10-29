# 検証

ひとつの問いを「仮説 → 設定 → 確認 → 結果 → 考察」の流れで確かめた記録です。進め方は [検証の進め方](workflow.md) にまとめています。プロトコルごとに分けて、検証のページには必ず構成図を入れています。

## 分類

| 分類 | 内容 | 件数 |
|------|------|------|
| [OSPF](ospf/index.md) | 広報される経路、ループバック、max-metric など | 4件 |
| [MPLS L3VPN](l3vpn/index.md) | VRF に経路が入るまで、RD と RT、BGP のネクストホップ、ラベルとパケットの流れ | 4件 |
| [プラットフォーム](platform/index.md) | CML のノード（XRd など）でできること・できないこと | 1件 |

## OSPF

| 検証 | 状態 |
|------|------|
| [OSPF で広報される経路](ospf/advertised-routes.md) | 検証中 |
| [ループバックだけで有効にしたとき](ospf/loopback-only.md) | 検証中 |
| [物理 IF だけで有効にしたとき](ospf/physical-if-only.md) | 検証中 |
| [max-metric（起動時にコスト最大）](ospf/max-metric-on-startup.md) | 検証前 |

## MPLS L3VPN

| 検証 | 状態 |
|------|------|
| [CE から受けた経路が PE の VRF に入るまで](l3vpn/ce-route-to-vrf.md) | 検証前 |
| [RT があるのに、なぜ RD が必要なのか](l3vpn/why-rd.md) | 検証前 |
| [BGP のネクストホップはどうなるのか](l3vpn/bgp-nexthop.md) | 検証前 |
| [MPLS VPN を通るパケットの一生](l3vpn/packet-life.md) | 検証前 |

## プラットフォーム

| 検証 | 状態 |
|------|------|
| [XRd は P ルータとして動くか](platform/xrd-as-p-router.md) | 検証前 |
