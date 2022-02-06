from pathlib import Path
import subprocess
from subprocess import CompletedProcess

from github import Github

# REPOSITORY = "hy-sksem/GeneratePdfFileFromGithubIssue"
REPOSITORY = "your username/your repository name" 
TOKEN = "your personal access token" # Personal access token

def ConvertIssue(issue_num: str, suffix: str):

    def _Md2Docx(tgt_file: Path) -> CompletedProcess:
        docx_file = tgt_file.with_suffix(".docx")
        return subprocess.run(f'pandoc "{tgt_file}" --from=markdown --to=docx -o {docx_file}')

    def _Md2Pdf(tgt_file: Path) -> CompletedProcess:
        pdf_file = tgt_file.with_suffix(".pdf")
        return subprocess.run(f'pandoc "{tgt_file}" -V documentclass=ltjarticle --pdf-engine=lualatex -o {pdf_file}')

    def _Md2Stdout(tgt_file: Path) -> CompletedProcess:
        return subprocess.run(f'pandoc "{tgt_file}"')

    def _Md2Html(tgt_file: Path) -> CompletedProcess:
        html_file = tgt_file.with_suffix(".html")
        return subprocess.run(f'pandoc "{tgt_file}" -o {html_file}')

    issue = Github(TOKEN).get_repo(REPOSITORY).get_issue(int(issue_num))
    md_file = Path(__file__).parent / f"{issue.title}.md"
    with open(md_file, "w", encoding="utf-8", newline="") as f:
        f.write(issue.body)
    if suffix == "1":
        result = _Md2Docx(md_file)
    elif suffix == "2":
        result = _Md2Pdf(md_file)
    elif suffix == "3":
        result = _Md2Stdout(md_file)
    elif suffix == "4":
        result = _Md2Html(md_file)
    return result

def main():
    issue_num = input("Issue番号 :")
    suffix = input("変換先を選択してください。docx:1, PDF:2, Stdout:3, HTML:4 :")
    if suffix != "1" and suffix != "2" and suffix != "3" and suffix != "4":
        print("変換先の指定が不正です")
        exit()
    result = ConvertIssue(issue_num, suffix)
    
        
    status = "成功" if result.returncode == 0 else "失敗"
    print(f"{result.args}の実行に{status}しました")

if __name__ == "__main__":
    main()
