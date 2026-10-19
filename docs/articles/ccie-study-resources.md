# CCIE 合格者が使った教材

CCIE の受験記・合格体験記を読んで、SP（Service Provider）と EI（Enterprise Infrastructure、旧 R&S）で使われていた本と教材をまとめたものです。自分の勉強の計画は [CCIE SP 合格までのロードマップ](../plan/index.md) にあります。

!!! note "年代に注意"
    ルートリフの岡山氏の受験記は 2004〜2007年ごろのもので、当時の試験には Frame Relay・ATM・ISDN などが出ていた。勉強の進め方は今でも参考になるが、本はそのまま今の試験に当てはまらないものもあるので、最近の合格者の教材と分けている。

## CCIE SP

### ルートリフ 岡山氏（2007年、2回目で合格）

- 記事：[CCIE Service Provider 受験記 1回目](https://rootriff.com/information/ccie-service-provider-first)、[2回目](https://rootriff.com/information/ccie-service-provider-second)

| 本・教材 | メモ |
| --- | --- |
| MPLS Configuration on Cisco IOS Software | MPLS の設定 |
| MPLS and VPN Architectures（Vol.1・Vol.2） | L3VPN の定番 |
| QoS for IP/MPLS Networks | SP の QoS |
| 詳解 MPLS の設計と実装 | 日本語の MPLS の本 |
| INE Workbook | ラボの練習 |
| IOS の MPLS Configuration Guide・Command Reference | 設定の最終確認 |

- R&S の総復習に MPLS・VPN を足す形で勉強していた
- 1回目は BGP の細部で点を落として 77点（合格まであと3点）。終了前に再起動したら VPN が動かなくなり、その対応で時間がなくなった
- 2回目は、BGP を鍛え直して合格

### 最近の SP（v5.x）

- 記事：[CCIE - Service Provider ラボ受験記（APC 技術ブログ、2023年）](https://techblog.ap-com.co.jp/entry/2023/12/14/142457)
- 記事：[HN781: CCIE Service Provider Free Workbook & Track Update（Packet Pushers）](https://packetpushers.net/podcasts/heavy-networking/hn781-ccie-service-provider-free-workbook-track-update/)

| 本・教材 | 挙げていた人 | メモ |
| --- | --- | --- |
| MPLS Fundamentals（Luc De Ghein） | Andrew Ohanian 氏 | 初心者向けとして推薦 |
| Segment Routing Part I・II・III（Clarence Filsfils ほか） | Andrew 氏、APC の方 | Part III は SRv6 |
| MPLS in the SDN Era | Andrew 氏 | 最初は難しく、2回目に読むと面白くなったとのこと |
| BGP Design and Implementation | APC の方 | |
| Definitive MPLS Network Designs | APC の方 | 設計（Design モジュール）対策 |
| Optimal Routing Design | APC の方 | IGP の設計 |
| The Art of Network Architecture | APC の方 | 設計の考え方 |
| [CCIE SP v5.1 無料ワークブック](https://ccie-sp.gitbook.io/ccie-spv5.1-labs)（Andrew Ohanian 氏作） | Packet Pushers で紹介 | 試験範囲に沿ったラボ集。XR（XRd）を使う |
| Cisco の有料 Practice Lab | Andrew 氏 | 本番の環境に慣れる |
| Cisco Live の資料 | Andrew 氏、APC の方 | 設計分野の補強 |

- SP のラボは Design（3時間）と DOO（5時間）に分かれている
- APC の方は「Design は英語の長文を読み続けるのがきつい」「DOO は内容はわかったが時間が足りなかった」と書いていた

## CCIE EI（旧 R&S）

### ルートリフ 岡山氏（R&S、2005年、5回目で合格）

- 記事：[受験記 1回目](https://rootriff.com/information/ccie-rs-first)、[2回目](https://rootriff.com/information/ccie-rs_second)、[3回目](https://rootriff.com/information/ccie-rs-third)、[4回目](https://rootriff.com/information/ccie-rs_fourth)、[5回目](https://rootriff.com/information/ccie-rs_fifth)

| 本・教材 | メモ |
| --- | --- |
| Routing TCP/IP Vol.1・Vol.2 | ルーティングの定番。今の EI 合格者も使っている |
| BGP Design and Implementation | BGP |
| Cisco DQOS Exam Certification Guide | QoS |
| CCIE Routing and Switching Practice Labs（Cisco Press） | ラボの問題集 |
| IPexpert・NetMasterClass・INE のワークブック | 受験のたびに買い足していた |
| Command Reference | 合格前の1か月は、ほぼこれだけを読んでいた |

- 点数は 56 → 66 → 72 → 76 → 合格と少しずつ上がっていった
- 合格の決め手は、Command Reference を読み直して、誤解していたところを1つずつ実機で確かめたこと

### 最近の EI

- 記事：[CCIE EI v1.0 合格体験記（yascaim 氏 / note）](https://note.com/yascaim/n/nf761cb3553b0)
- 記事：[CCIE Enterprise Infrastructure（LAB 試験）に合格しました！（クロスサイド）](https://www.cross-side.co.jp/2022/07/08/ccie-enterprise-infrastructurelab%E8%A9%A6%E9%A8%93%E3%81%AB%E5%90%88%E6%A0%BC%E3%81%97%E3%81%BE%E3%81%97%E3%81%9F/)
- 記事：[CCIE Enterprise Infrastructure 勉強法（Infraexpert）](https://www.infraexpert.com/info/cciez3.html)

| 本・教材 | 挙げていた人 |
| --- | --- |
| ENCOR 350-401 Official Cert Guide（Cisco Press） | yascaim 氏、クロスサイドの方 |
| CCIE Enterprise Infrastructure Foundation（Cisco Press） | yascaim 氏（一番活用した本） |
| Optimal Routing Design | yascaim 氏 |
| Routing TCP/IP Vol.1・Vol.2 | クロスサイドの方 |
| Cisco SD-WAN / Cisco Software-Defined Access の本 | クロスサイドの方 |
| DEVASC 200-901 Official Cert Guide | クロスサイドの方（自動化対策） |
| INE の EI Learning Path（動画と仮想ラボ） | yascaim 氏（勉強時間の約7割） |
| Cisco Learning Network の Practice Lab | yascaim 氏 |
| CML-Personal | yascaim 氏（「Free の5台では足りない」） |
| DevNet Sandbox | yascaim 氏（SD-WAN・SD-Access） |

## 共通して言われていること

- **最終的な正解は設定ガイドと Command Reference**：昔も今も、本の次は公式ドキュメントで確かめている
- **読む → 動かすの繰り返し**：本で読んだことを、自分のラボで必ず確かめる
- **設定の速さより確認のしかた**：「疎通しただけでは足りない、細部の確認が大事」（岡山氏）
- **1回目は本番の形式に慣れるつもりで**：合格者の多くは2〜5回目で合格している
- **英字キーボードに慣れておく**：本番は英字配列（yascaim 氏）
- **8時間の体力配分**：前日の睡眠、糖分やカフェインの補給も計画しておく（yascaim 氏）

## 勉強法の参考

- [CCIE の勉強法（ルートリフ）](https://rootriff.com/information/how_to_study_ccie)：試験範囲の論理・設定・確認方法をすべて押さえたと思えてから受験する。合計約7か月・約500時間
