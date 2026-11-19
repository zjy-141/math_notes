
from pathlib import Path

# ================= 配置区域 =================

# 默认处理的 Markdown 文件
INPUT_FILE = r"D:\01_Project\math_notes\格式更改.md"

# 输出文件路径
# None 表示直接覆盖原文件
OUTPUT_FILE = None

# =============================================

def convert_markdown(input_file, output_file=None):
    input_path = Path(input_file)

    if not input_path.is_file():
        raise FileNotFoundError(f"文件不存在：{input_path}")

    content = input_path.read_text(encoding="utf-8")

    replacements = {
        r"\[ ": "$$",
        r" \]": "$$",
        r"\( ": "$",
        r" \)": "$",
        r"\[": "$$",
        r"\]": "$$",
        r"\(": "$",
        r"\)": "$",
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    output_path = Path(output_file) if output_file else input_path
    output_path.write_text(content, encoding="utf-8")

    print("转换完成！")
    print(f"处理文件：{input_path}")
    print(f"输出文件：{output_path}")


if __name__ == "__main__":
    convert_markdown(INPUT_FILE, OUTPUT_FILE)
