from pathlib import Path
import subprocess
from subprocess import CompletedProcess

def Md2Docx(tgt_file: Path) -> CompletedProcess:
    docx_file = tgt_file.with_suffix(".docx")
    return subprocess.run(f'pandoc "{tgt_file}" --from=markdown --to=docx -o {docx_file}')

def Md2Pdf(tgt_file: Path) -> CompletedProcess:
    pdf_file = tgt_file.with_suffix(".pdf")
    return subprocess.run(f'pandoc "{tgt_file}" -V documentclass=ltjarticle --pdf-engine=lualatex -o {pdf_file}')

def Md2Stdout(tgt_file: Path) -> CompletedProcess:
    return subprocess.run(f'pandoc "{tgt_file}"')

def Md2Html(tgt_file: Path) -> CompletedProcess:
    html_file = tgt_file.with_suffix(".html")
    return subprocess.run(f'pandoc "{tgt_file}" -o {html_file}')

def main():
    md_file = input("変換したい.mdのファイルパスを指定してください:")
    suffix = input("変換先を選択してください。docx:1, PDF:2, Stdout:3, HTML:4 :")
    if suffix == "1":
        result = Md2Docx(Path(md_file))
    elif suffix == "2":
        result = Md2Pdf(Path(md_file))
    elif suffix == "3":
        result = Md2Stdout(Path(md_file))
    elif suffix == "4":
        result = Md2Html(Path(md_file))
    else:
        print("変換先の指定が不正です")
        exit()
    status = "成功" if result.returncode == 0 else "失敗"
    print(f"{result.args}の実行に{status}しました")

if __name__ == "__main__":
    main()
