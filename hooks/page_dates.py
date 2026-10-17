"""各ページの見出しの下に、作成日と更新日を自動で表示する MkDocs フック。

日付は Git の履歴（そのファイルが最初にコミットされた日と、最後にコミットされた日）から
日本時間で求める。履歴が取れないときはビルドした日を使う。
"""

import os
import re
import subprocess
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))
SKIP = {"index.md"}  # トップページには表示しない


def _git_times(path):
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%at", "--", path],
            capture_output=True, text=True, check=True,
            cwd=os.path.dirname(path) or ".",
        ).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None, None
    if not out:
        return None, None
    to_date = lambda ts: datetime.fromtimestamp(int(ts), JST).strftime("%Y-%m-%d")
    return to_date(out[-1]), to_date(out[0])


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri in SKIP:
        return markdown
    created, updated = _git_times(page.file.abs_src_path)
    today = datetime.now(JST).strftime("%Y-%m-%d")
    created = created or today
    updated = updated or today
    line = f'<p class="page-dates">作成日：{created}　／　更新日：{updated}</p>'
    # 最初の見出し（# タイトル）の直後に入れる。見出しがなければ先頭に入れる
    m = re.search(r"^# .*$", markdown, flags=re.M)
    if m:
        return markdown[: m.end()] + "\n\n" + line + "\n" + markdown[m.end():]
    return line + "\n\n" + markdown
