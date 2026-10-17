# supur1n Network Lab Notes

CML で検証した内容をまとめる MkDocs (Material) サイトです。

## 1. 手元で動かす

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

ブラウザで http://127.0.0.1:8000 を開くとプレビューできます（保存すると自動で更新）。

## 2. GitHub Pages で公開する

1. GitHub で `lab-notes` という名前のリポジトリを作成（Public）
2. `mkdocs.yml` の `YOUR-GITHUB-ID` を自分の ID に置き換える
3. このフォルダを push

   ```bash
   git init
   git add .
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-GITHUB-ID/lab-notes.git
   git push -u origin main
   ```

4. リポジトリの **Settings → Pages → Build and deployment → Source** を **GitHub Actions** にする
5. Actions タブでデプロイが成功すると `https://YOUR-GITHUB-ID.github.io/lab-notes/` で公開されます

以降は記事を書いて push するだけで自動更新されます。

## 3. 記事を追加する

1. `templates/article-template.md` をコピーして、`docs/<カテゴリ>/<記事名>.md` に置く
2. `mkdocs.yml` の `nav:` に追加
3. カテゴリの `index.md` の一覧表に追加

画像は `docs/assets/images/` に置き、`![説明](../assets/images/xxx.png)` で参照します。

## 公開前チェック

- [ ] 業務の設定・ホスト名・IPアドレス・社内構成に似たものが入っていない
- [ ] CMLのノードイメージ等のファイルを置いていない（コンフィグ・show出力・図はOK）
- [ ] show出力にシリアル番号やライセンス情報が入っていない
