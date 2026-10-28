# トラブルシューティング

ラボで実際にうまくいかなかったことと、その切り分けの手順をまとめています。「何が起きたか → どこを確認したか → 何が原因だったか」をセットで残しています。

| ページ | 内容 | 起きた日 |
|------|------|------|
| [ping が届かないとき](ping-unreachable.md) | 同じネットワーク内でも ping が届かないときの切り分け。リンクのダウン、IP アドレスの範囲。CML 特有のリンク状態の見え方 | [2026-10-23](../study-log/2026-10-23.md) |
| [OSPF の Hello の間隔が合わないとき](ospf-hello-interval.md) | ネイバーが張れず、PC 同士の ping が通らない。Hello / Dead の間隔、設定を入れる場所と効く範囲（演習 第1問） | 2026-10-28 |
| [ルータ間の IF が OSPF の passive になっていたとき](ospf-passive.md) | ネイバーが張れず、PC 同士の ping が通らない。passive の意味と本来の使い方（演習 第2問） | 2026-10-28 |
| [OSPF のネイバーが EXSTART / EXCHANGE で止まるとき](ospf-mtu-mismatch.md) | MTU の不一致で DBD の交換が終わらない。ネイバーの状態から原因の見当をつける（演習 第3問） | 2026-10-28 |
| [壊れている場所が2つあったとき](ospf-multiple-faults-1.md) | OSPF の対象から外された PC 側の IF と、PC のゲートウェイの間違い。行きと帰りに分けて考える（演習 第4問） | 2026-10-28 |
| [ネイバーは FULL なのに経路が載らないとき](ospf-network-type-mismatch.md) | ネットワークタイプの不一致（P2P と BROADCAST）。FULL でも安心できない（演習 第5問） | 2026-10-28 |
| [Desktop を Wipe したあと、ping が通らなくなったとき](stale-arp-after-wipe.md) | Wipe で MAC アドレスが変わり、ルータに古い ARP が残っていた。L2 も疑う | 2026-10-29 |
