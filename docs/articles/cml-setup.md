# CMLの導入

CML Free を自宅のPCに入れるときに参考にした記事です。

## CML Free を Windows にインストール

- リンク: [note（Shohei Okada 氏）](https://note.com/sokada_itnet/n/n6a8fa1836968)
- 公開: 2026年4月

Windows に VMware Workstation Pro を入れ、CML Free の OVA と refplat ISO を読み込んで初期設定し、IOL を2台つないで動作確認するまでを順に解説している。Cisco アカウントの作成からダウンロードまでの流れもまとまっている。

!!! note "自分の環境で試したときのメモ"
    - 無料版のファイルは有料版とページが分かれている。名前に `free`（OVA は `_f_`）が入ったものを選ぶ
    - ダウンロード前に Cisco アカウントのプロフィール（住所など）をすべて埋めておく必要がある
    - 新しい版の CML は入れ子の仮想化（VT-x）が必須。Windows の Hyper-V 系の機能が有効だと起動できないので、無効にしてから VMware の「Intel VT-x/EPT を仮想化」をオンにする
