# OSPF の検証

OSPF に関する検証の一覧です。プロトコルの説明は [プロトコル → OSPF](../../protocols/ospf/index.md) にまとめています。

| 検証 | 問い | 環境 | 状態 |
|------|------|------|------|
| [OSPF で広報される経路](advertised-routes.md) | インターフェースで OSPF を有効にしたとき、どんな経路が、どんな形で広報されるのか | IOSv × 4（CML Free） | 検証中 |
| [ループバックだけで有効にしたとき](loopback-only.md) | IOS XR で、OSPF をループバックだけで有効にしたとき、ループバックは対向に広報されるのか | IOS XRv 9000 × 2 | 検証中（ネイバーが張れていないことまで） |
| [物理 IF だけで有効にしたとき](physical-if-only.md) | IOS XR で、物理 IF に OSPF を設定したとき、どんな経路が広報されるのか（ルータ間だけ／PC 向けも） | IOS XRv 9000 × 2 | 検証中（②-a まで） |
| [max-metric（起動時にコスト最大）](max-metric-on-startup.md) | IOS XR で max-metric router-lsa on-startup を設定したルータを再起動すると、コストと経路はどう変わるのか | IOS XRv 9000 × 4（案） | 検証前 |
