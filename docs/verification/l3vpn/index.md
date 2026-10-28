# MPLS L3VPN の検証

MPLS L3VPN（VRF・RD・RT・MP-iBGP・ラベル）に関する検証の一覧です。プロトコルの説明は [プロトコル → MPLS](../../protocols/mpls/index.md)、[VRF](../../protocols/vrf/index.md)、[BGP](../../protocols/bgp/index.md) にまとめています。

| 検証 | 問い | 環境 | 状態 |
|------|------|------|------|
| [CE から受けた経路が PE の VRF に入るまで](ce-route-to-vrf.md) | CE から受けた経路を、PE はどういう順番で VRF に入れるのか | CE-PE-P-PE-CE（案） | 検証前 |
| [RT があるのに、なぜ RD が必要なのか](why-rd.md) | RT で VRF を分けられるのに、なぜ RD も設定するのか | PE × 2、P、CE × 4（案） | 検証前 |
| [BGP のネクストホップはどうなるのか](bgp-nexthop.md) | CE2 から CE1 宛てのパケットで、各ルータの BGP のネクストホップと宛先 IP はどうなっているのか | CE-PE-P-PE-CE（案） | 検証前 |
| [MPLS VPN を通るパケットの一生](packet-life.md) | お客さまの経路・VPN ラベル・LDP ラベルは、どのプロトコルでどこへ広報され、パケットはどう運ばれるのか。VPN ラベルと VRF の関係 | CE-PE-P-P-PE-CE（案） | 検証前 |
