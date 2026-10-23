# CMLの導入と使い方

CML を自宅のPCや専用機に入れるときや、CML の機能を理解するときに参考にした資料です。自分でベアメタルに構築したときの記録は [CML-Personal をベアメタルで構築する](../about/cml-baremetal.md) にあります。

## CML Free を Windows にインストール

- リンク: [note（Shohei Okada 氏）](https://note.com/sokada_itnet/n/n6a8fa1836968)
- 公開: 2026年4月

Windows に VMware Workstation Pro を入れ、CML Free の OVA と refplat ISO を読み込んで初期設定し、IOL を2台つないで動作確認するまでを順に解説している。Cisco アカウントの作成からダウンロードまでの流れもまとまっている。

!!! note "自分の環境で試したときのメモ"
    - 無料版のファイルは有料版とページが分かれている。名前に `free`（OVA は `_f_`）が入ったものを選ぶ
    - ダウンロード前に Cisco アカウントのプロフィール（住所など）をすべて埋めておく必要がある
    - 新しい版の CML は入れ子の仮想化（VT-x）が必須。Windows の Hyper-V 系の機能が有効だと起動できないので、無効にしてから VMware の「Intel VT-x/EPT を仮想化」をオンにする

## CML-Personal を購入して ESXi に構築

- リンク: [Cisco Modeling Labs を購入・初期構築して試す（Qiita、suzuyui 氏）](https://qiita.com/suzuyui/items/f2ed1738eaa1c8f64408)
- 公開: 2025年2月（CML 2.8.0）

CML-Personal を Cisco Learning Network Store で買うところから、ESXi 上に OVA で構築し、ライセンスを登録して NX-OS を動かすまでをまとめた記事。購入の画面の流れ、ダウンロードするファイル、初期設定で聞かれる項目、ライセンス登録の手順が順に載っている。

ESXi への構築なので、そのまま使えるところと、ベアメタルでは不要なところがある。

| 手順 | ベアメタルでも使えるか |
| --- | --- |
| Learning Network Store での購入 | 使える（Personal は年額 $199＋税） |
| ダウンロード（My Account → My Orders → Download） | 使える。ただし本体は OVA ではなく**ベアメタル用の ISO** を選ぶ |
| refplat は ZIP を展開した **.iso** を使う | 使える |
| VM の CPU・メモリ・ディスクの割り当て | 不要（マシン全体を CML が使う） |
| ESXi の ReversePathFwdCheck、vSwitch の無差別モード | 不要 |
| 初期設定（ホスト名、sysadmin のパスワード、初期ユーザー、IP） | 使える。流れは同じ |
| Web 画面は `https://IP`、管理画面（Cockpit）は `https://IP:9090` | 使える |
| ライセンス登録（Licensing → CML-PER-BASE を選ぶ → トークンを REGISTER） | 使える |

!!! note "自分用のメモ"
    - トークンを登録するまでは 90 日の評価モードになる。登録を忘れない
    - sysadmin のパスワードは 8 文字以上で、文字の種類が少ないと警告が出る
    - トークンは Learning Network Store の My Orders → 対象の注文 → View license(s) から取り出す

## CML をベアメタルにインストール

- リンク: [Intel N97のミニPCを買った話（ついでにCML2.8 Free Tierをベアメタルにインストール）（Qiita、ecodrive 氏）](https://qiita.com/ecodrive/items/5e69c74ad195804fff50)
- 公開: 2024年12月（CML 2.8.0 Free Tier）

ミニ PC の Windows を消して、CML を直接（ベアメタルで）入れた記事。Free Tier だが、インストールの流れは Personal でも同じ。

| 手順 | 内容 |
| --- | --- |
| 1. ダウンロード | CML 本体の **ISO（zip）** と refplat ISO（zip）。どちらも展開して .iso を使う |
| 2. USB の作成 | Rufus で、CML 本体の ISO からブータブル USB を作る。refplat はこの時点では不要 |
| 3. USB から起動 | BIOS で起動順の先頭を USB にする |
| 4. インストール | メニューの先頭「Install CML」を選ぶ。終わると自動で再起動 |
| 5. 初回の起動 | もう一度 USB から起動し、2番目の「Boot from next volume」を選ぶ。CML が起動したら USB を抜く |
| 6. 初期設定 | ユーザーアカウントとネットワークを設定 |
| 7. refplat を入れる | refplat ISO を USB などで CML に渡してマウントし、Cockpit（`https://IP:9090`）の「Copy Refplat ISO」で取り込む |
| 8. 確認 | Web 画面の System Status がすべて READY になれば完了 |

!!! note "自分の Z8 G4 で入れるときのメモ"
    - HP のワークステーションは、起動直後に **F10 で BIOS 設定、F9 で起動するデバイスの選択**
    - refplat を入れるまでは、画面右下に赤字で `SYSTEM HEALTH ISSUE` が出る。故障ではない
    - 最低要件は、メモリ 8GB 以上、物理 4 コア以上の Intel CPU（VT-x と EPT 対応）、NIC 1つ以上、ディスク 32GB 以上

## CML の基本操作（構築したあとの使い方）

- リンク: [【Cisco Modeling Labs】CML2 最初の一歩（note、えのきこ氏）](https://note.com/enokiko/n/n3ff481cbae3e)
- 公開: 2025年6月（CML 2.7.2 / 2.8.1）

CML を入れ終わったあとに、画面の見方からラボの作成、ノードの追加と接続、起動、コンソール操作までを順にまとめた記事。マニュアルのように、困ったときに引く用途で使える。

| 章 | 内容 |
| --- | --- |
| 画面の見方 | Dashboard、画面下の CPU・メモリ・ディスクの使用率とステータス表示 |
| ラボの作成 | Dashboard の「ADD」でラボを作り、Workbench で編集する。名前の変え方 |
| Start / Stop / Wipe / Delete | ノードの起動・停止・状態の消去・削除の違い |
| ノードの追加と選び方 | アイコンをドラッグして追加。メモリ・CPU・ディスクの消費を考えて選ぶ |
| 起動前の設定 | CONFIG タブで初期コンフィグを入れる。インターフェースの数は初回起動前に増やす |
| ケーブル接続 | 「Add Link」でノード同士をつなぐ |
| お絵描き | 図形・線・テキストの追加、グリッドとスナップ |
| コンソール | 右クリックでコンソールを開く。複数パネル表示、履歴行数・フォントの設定 |
| ログ保存 | コンソールのログをダウンロードする |
| ラボのコピー | YAML でダウンロード・インポートする（設定は引き継がれない点に注意） |

!!! note "自分用のメモ"
    - ラボを YAML で保存しても、ルータの設定は自動では入らない。設定ごと残したいときは、保存の前に設定を CONFIG に取り込んでおく
    - インターフェースを増やすのは初回起動の前に。起動後は Wipe してからでないと変えられない

## シスコ公式ウェビナー資料

シスコが開催した「CMLを使ってネットワークを学ぼう！」ウェビナーの資料（PDF）。CML の全体像と主な機能を日本語で体系的に学べる。

!!! warning "バージョンに注意"
    どちらも 2020年7月、CML 2.0 時点の資料。画面や版の構成（当時は Personal / Enterprise のみで、Free はまだない）は今の CML とは異なる部分がある。

### 基礎編

- リンク: [CMLを使ってネットワークを学ぼう！（基礎編）PDF](https://www.cisco.com/c/dam/global/ja_jp/training-events/training-certifications/cln/seminar/jp-webinar-cml01.pdf)
- 発行: シスコシステムズ（2020年7月）

CML の概要から、インストールと初期設定、ラボマネージャ・ワークベンチの基本操作までを解説。パケットキャプチャ、外部接続、ブレイクアウトツール、初期コンフィグの投入といった便利な機能や、資格学習・トラブルシューティング・自動化などの使いどころも紹介されている。

### 応用編

- リンク: [CMLを使ってネットワークを学ぼう！（応用編）PDF](https://www.cisco.com/c/dam/global/ja_jp/training-events/training-certifications/cln/seminar/jp-webinar-cml02.pdf)
- 発行: シスコシステムズ（2020年7月）

使える仮想ノードの紹介に加え、他社製イメージを追加する手順、WAN エミュレータでの遅延・帯域の再現、TRex によるトラフィック生成などを解説。SSH 経由でのコンソール接続、資格試験向けの使い方（制御パケットの確認やキャプチャ）、外部の監視ツールとの連携にも触れている。
