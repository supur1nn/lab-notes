# このサイトの作り方

このサイトは MkDocs（Material テーマ）と GitHub Pages を使って、無料で公開しています。記事は Markdown で書いて保存するだけで、数分後に自動でサイトに反映されます。

この記事では、サイトを作った理由と、公開するまでの手順・つまずいたポイントをまとめます。

## このサイトを作った理由

ネットワークエンジニアとして学んだことを、自分の言葉で整理して残しておく場所がほしかった。勉強した内容は手元のメモに散らばりがちで、あとから見返したいときに見つからない。サイトにまとめておけば、自分の復習にもなり、同じことを調べている誰かの役にも立つと考えた。

もうひとつの理由は、アウトプットすることで理解が深まるから。人に説明できる形に書き直すと、わかったつもりになっていた部分がはっきりする。

### CMLでやっていること

Cisco Modeling Labs（CML）で仮想ラボを組み、サービスプロバイダ向けの技術を中心に検証している。

- MPLS（LDP、RSVP-TE、L3VPN）
- BGP（iBGP、ルートリフレクタ、ポリシー制御）
- Segment Routing（SR-MPLS、TI-LFA、SR-TE）
- IOS XR の操作と IOS XE との違い

設定して終わりではなく、わざと障害を起こして切り分けるところまでやるのが自分の学習スタイル。その過程も記事に残していく。

## 公開方法の比較

勉強ノートを体系的に整理したかったので、2の「静的サイト＋無料ホスティング」を選んだ。

| 方法 | 例 | 手軽さ | 自由度 | 向いている使い方 |
| --- | --- | --- | --- | --- |
| 1. 技術ブログサービス | Zenn、Qiita、はてなブログ | 最も手軽。登録してすぐ書ける | 低い（見た目・構成はサービス次第） | 記事を単発でどんどん出す。読者に見つけてもらいやすい |
| 2. 静的サイト＋無料ホスティング | MkDocs / Hugo ＋ GitHub Pages / Cloudflare Pages | 最初の準備だけ少し必要。以降は書いて保存するだけ | 高い（構成・見た目・独自ドメイン） | テーマ別にノートを整理するドキュメントサイト |
| 3. 自前サーバー | VPS、自宅サーバー | 手間が大きい（セキュリティ・保守が必要） | 最も高い | DNS・TLS・FWも含めて勉強したいとき |

## 選んだ構成

MkDocs（Material テーマ）で Markdown をサイトにし、GitHub Actions で自動ビルド、GitHub Pages で無料公開する。

```mermaid
graph LR
  A["記事を書く<br/>Markdownで編集"] -- commit --> B["リポジトリ<br/>変更履歴を保存"]
  B -- 自動で起動 --> C["GitHub Actions<br/>Markdown → HTML"]
  C -- deploy --> D["GitHub Pages<br/>サイトを公開"]
```

記事を保存すると、1〜2分でサイトに反映される。MkDocs はテーマ別にノートを整理しやすく、検索・ダークモード・コードのコピーボタンが標準で付く。

## GitHubとは

GitHub は、ファイルの変更履歴をすべて残しながら保管できるネット上の置き場所。中心にある Git の考え方は、IOS XR の commit / rollback とほぼ同じ。

| 用語 | 意味 | ネットワーク機器でいうと |
| --- | --- | --- |
| リポジトリ | ファイルと履歴をまとめたプロジェクト単位の箱 | 1台分のコンフィグ管理単位 |
| コミット | 変更を確定して履歴に残すこと | IOS XR の commit |
| Push | 手元PCで確定した変更を GitHub に送ること | 設定のアップロード |
| Public / Private | 誰でも見られるか、自分だけか | — |
| GitHub Actions | ファイルが更新されたら自動で処理を動かす仕組み | EEM アプレット |
| GitHub Pages | リポジトリの中身を Web サイトとして無料公開する機能 | — |

!!! note
    無料プランでは Private のリポジトリから Pages を公開できないため、サイト用のリポジトリは Public にする。

### 自動公開の設定ファイル（.github/workflows/deploy.yml）

GitHub Actions への手順書。GitHub は `.github/workflows/` にある YAML を自動で探して実行する。

- いつ動くか: main に変更がコミットされたとき、または手動実行したとき
- build: 一時的な Linux マシンで MkDocs をインストールし、Markdown から HTML を生成
- deploy: 生成したサイトを GitHub Pages に公開

## 公開手順（ブラウザだけで行う方法）

Python や Git をインストールしなくても、ブラウザだけで公開できる。

1. **GitHub アカウントを作る** — ユーザー名がサイトURLの一部になる（`https://ユーザー名.github.io/リポジトリ名/`）。
2. **リポジトリを作る** — 右上「＋」→「New repository」。名前を決め、**Public** を選び、README などのチェックは入れずに「Create repository」。
3. **サイトのファイル一式を用意する** — mkdocs.yml、requirements.txt、docs フォルダなど。zip でもらった場合は右クリック →「すべて展開」で解凍しておく。
4. **ファイルをアップロードする** — 「uploading an existing file」を開き、ファイルとフォルダを選んで**ドラッグ＆ドロップ**→「Commit changes」。一覧に `docs/index.md` のようにフォルダ名が付いていれば成功。
5. **URL を書き換える** — mkdocs.yml を鉛筆マークで編集し、`site_url` などを自分のユーザー名に変えて保存。
6. **公開スイッチを入れる** — Settings → Pages → Build and deployment の Source を「GitHub Actions」に変更。
7. **自動公開の設定ファイルを作る** — 「Add file」→「Create new file」。ファイル名に `.github/workflows/deploy.yml` と入力し、下の内容を貼って「Commit changes」。
8. **確認する** — Actions タブで緑のチェックになれば公開完了。赤い✕ならログでエラー箇所を確認する。

手順7で貼る内容:

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

## つまずいたポイント

| 症状 | 原因 | 対処 |
| --- | --- | --- |
| 既存のリポジトリが Private だった | 無料プランは Private から Pages を公開できない | サイト用に Public のリポジトリを新規作成 |
| アップロード一覧に index (1).md、index (2).md が並ぶ | zip を解凍せず、フォルダ構造が崩れていた | 「すべて展開」してからフォルダごとドラッグ＆ドロップ |
| 一覧に download というファイルがある | 解凍前のファイルが混ざっていた | zip を解凍してから選び直す |
| .github フォルダがアップロードされない | Windows では隠しフォルダ扱いで見えない | Create new file で .github/workflows/deploy.yml を直接作る |

---

<small>記載の会社名・製品名は各社の商標または登録商標です。</small>
