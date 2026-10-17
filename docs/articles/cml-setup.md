# CMLの導入と使い方

CML Free を自宅のPCに入れるときや、CML の機能を理解するときに参考にした資料です。

## CML Free を Windows にインストール

- リンク: [note（Shohei Okada 氏）](https://note.com/sokada_itnet/n/n6a8fa1836968)
- 公開: 2026年4月

Windows に VMware Workstation Pro を入れ、CML Free の OVA と refplat ISO を読み込んで初期設定し、IOL を2台つないで動作確認するまでを順に解説している。Cisco アカウントの作成からダウンロードまでの流れもまとまっている。

!!! note "自分の環境で試したときのメモ"
    - 無料版のファイルは有料版とページが分かれている。名前に `free`（OVA は `_f_`）が入ったものを選ぶ
    - ダウンロード前に Cisco アカウントのプロフィール（住所など）をすべて埋めておく必要がある
    - 新しい版の CML は入れ子の仮想化（VT-x）が必須。Windows の Hyper-V 系の機能が有効だと起動できないので、無効にしてから VMware の「Intel VT-x/EPT を仮想化」をオンにする

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
