"""
第 10 章：文件 I/O
知识点：open() 模式（r/w/a/b）、with 语句、逐行读取、
        csv 模块读写、json 模块序列化/反序列化、pathlib.Path
"""

import csv
import json
from pathlib import Path

# 获取当前文件所在目录，所有文件操作相对于此目录
BASE_DIR = Path(__file__).parent

# ============================================================
# 1. open() 基础 & with 语句
# ============================================================

print("=== 文件基础读写 ===")

# 写文件（w 模式：覆盖写入）
output_file = BASE_DIR / "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("第一行：Python 文件操作\n")
    f.write("第二行：使用 with 语句自动关闭文件\n")
    f.writelines(["第三行\n", "第四行\n", "第五行\n"])
print(f"已写入: {output_file.name}")

# 读文件（r 模式：全部读取）
with open(output_file, "r", encoding="utf-8") as f:
    content = f.read()
print(f"全部读取（{len(content)} 字符）:\n{content}")

# 逐行读取（大文件推荐）
print("逐行读取:")
with open(output_file, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(f"  行{line_no}: {line.rstrip()}")

# readlines() 读取所有行到列表
with open(output_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"\nreadlines() 返回 {len(lines)} 行")

# ============================================================
# 2. 追加写入（a 模式）
# ============================================================

print("\n=== 追加模式 ===")

with open(output_file, "a", encoding="utf-8") as f:
    f.write("第六行：追加内容\n")

with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================
# 3. 二进制模式（b 模式）
# ============================================================

print("=== 二进制读写 ===")

binary_file = BASE_DIR / "sample.bin"
data = bytes(range(16))    # 0x00 ~ 0x0F

with open(binary_file, "wb") as f:
    f.write(data)

with open(binary_file, "rb") as f:
    read_data = f.read()

print(f"写入字节: {data.hex()}")
print(f"读取字节: {read_data.hex()}")
print(f"数据一致: {data == read_data}")

# ============================================================
# 4. csv 模块
# ============================================================

print("\n=== CSV 读写 ===")

csv_file = BASE_DIR / "sample_data.csv"

# 读取 CSV（DictReader：返回每行为字典）
with open(csv_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    employees = list(reader)

print(f"读取 {len(employees)} 条员工记录")
for emp in employees[:3]:
    print(f"  {emp['name']:<8} {emp['department']:<15} 薪资={emp['salary']}")

# 按部门统计平均薪资
dept_salaries: dict[str, list[int]] = {}
for emp in employees:
    dept = emp["department"]
    salary = int(emp["salary"])
    dept_salaries.setdefault(dept, []).append(salary)

print("\n各部门平均薪资:")
for dept, salaries in sorted(dept_salaries.items()):
    avg = sum(salaries) / len(salaries)
    print(f"  {dept:<15} {avg:>10,.0f}")

# 写入 CSV
report_file = BASE_DIR / "dept_report.csv"
with open(report_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["department", "count", "avg_salary"])
    writer.writeheader()
    for dept, salaries in sorted(dept_salaries.items()):
        writer.writerow({
            "department": dept,
            "count": len(salaries),
            "avg_salary": round(sum(salaries) / len(salaries), 2),
        })
print(f"\n部门报告已写入: {report_file.name}")

# ============================================================
# 5. json 模块
# ============================================================

print("\n=== JSON 序列化/反序列化 ===")

# Python 对象 -> JSON 字符串
data = {
    "project": "Python 教学",
    "version": "3.10",
    "topics": ["基础", "OOP", "异常处理"],
    "stats": {"chapters": 12, "exercises_per_chapter": 3},
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("json.dumps 输出:")
print(json_str)

# JSON 字符串 -> Python 对象
restored = json.loads(json_str)
print(f"\njson.loads 类型: {type(restored)}")
print(f"topics: {restored['topics']}")

# 写入 JSON 文件
json_file = BASE_DIR / "config.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"\n已写入: {json_file.name}")

# 从 JSON 文件读取
with open(json_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"从文件读取: {loaded['project']} v{loaded['version']}")

# ============================================================
# 6. pathlib.Path
# ============================================================

print("\n=== pathlib.Path ===")

p = BASE_DIR

# 基本属性
print(f"路径:      {p}")
print(f"名称:      {p.name}")
print(f"父目录:    {p.parent}")
print(f"是目录:    {p.is_dir()}")

# 路径拼接（/ 运算符）
new_path = p / "subdir" / "file.txt"
print(f"路径拼接: {new_path}")
print(f"stem:    {new_path.stem}")
print(f"suffix:  {new_path.suffix}")

# 列出目录内容
print(f"\n当前章节目录文件:")
for item in sorted(p.iterdir()):
    icon = "📁" if item.is_dir() else "📄"
    print(f"  {icon} {item.name}")

# 查找文件（glob）
py_files = list(p.glob("*.py"))
print(f"\n.py 文件: {[f.name for f in py_files]}")

# 文件信息
for f in py_files:
    size = f.stat().st_size
    print(f"  {f.name}: {size} bytes")

# 创建/删除目录
temp_dir = p / "temp_demo"
temp_dir.mkdir(exist_ok=True)
print(f"\n创建目录: {temp_dir.name}, 存在: {temp_dir.exists()}")
temp_dir.rmdir()
print(f"删除目录后存在: {temp_dir.exists()}")

# read_text / write_text（简洁方式）
quick_file = p / "quick.txt"
quick_file.write_text("pathlib 一行写入\n", encoding="utf-8")
print(f"\nread_text: {quick_file.read_text(encoding='utf-8').strip()!r}")
quick_file.unlink()  # 删除文件

# 清理本示例产生的文件
for cleanup in ["output.txt", "sample.bin", "dept_report.csv", "config.json"]:
    target = p / cleanup
    if target.exists():
        target.unlink()
print("\n示例文件已清理完毕")
