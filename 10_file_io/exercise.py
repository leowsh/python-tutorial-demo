"""
第 10 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：CSV 数据分析
# 使用当前目录下的 sample_data.csv（字段：id,name,department,salary,join_date）
# 要求：
#   (a) 找出薪资最高和最低的员工（输出姓名、部门、薪资）
#   (b) 输出 2020 年之后加入（join_date >= 2020-01-01）的员工名单
#   (c) 统计每个部门的员工人数并按人数降序输出
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import csv
# from pathlib import Path
#
# BASE_DIR = Path(__file__).parent
# csv_file = BASE_DIR / "sample_data.csv"
#
# with open(csv_file, "r", encoding="utf-8", newline="") as f:
#     employees = list(csv.DictReader(f))
#
# # (a) 薪资最高/最低
# sorted_by_salary = sorted(employees, key=lambda e: int(e["salary"]))
# lowest = sorted_by_salary[0]
# highest = sorted_by_salary[-1]
# print("薪资最低:", lowest["name"], lowest["department"], lowest["salary"])
# print("薪资最高:", highest["name"], highest["department"], highest["salary"])
#
# # (b) 2020 年后加入
# print("\n2020年后加入的员工:")
# for emp in employees:
#     if emp["join_date"] >= "2020-01-01":
#         print(f"  {emp['name']} ({emp['join_date']})")
#
# # (c) 部门人数
# from collections import Counter
# dept_count = Counter(emp["department"] for emp in employees)
# print("\n各部门人数（降序）:")
# for dept, count in dept_count.most_common():
#     print(f"  {dept}: {count}人")

# ============================================================
# 练习 2：JSON 配置文件管理器
# 要求：实现 ConfigManager 类，操作 JSON 配置文件
#   - __init__(filepath)：加载配置（不存在则创建空字典）
#   - get(key, default=None)：读取配置项
#   - set(key, value)：设置配置项并立即保存到文件
#   - delete(key)：删除配置项
#   - all()：返回所有配置
# 演示：创建 config_test.json，存入若干配置，读取，修改，删除
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import json
# from pathlib import Path
#
# class ConfigManager:
#     def __init__(self, filepath: str | Path) -> None:
#         self.filepath = Path(filepath)
#         if self.filepath.exists():
#             with open(self.filepath, "r", encoding="utf-8") as f:
#                 self._config = json.load(f)
#         else:
#             self._config = {}
#
#     def _save(self) -> None:
#         with open(self.filepath, "w", encoding="utf-8") as f:
#             json.dump(self._config, f, ensure_ascii=False, indent=2)
#
#     def get(self, key: str, default=None):
#         return self._config.get(key, default)
#
#     def set(self, key: str, value) -> None:
#         self._config[key] = value
#         self._save()
#
#     def delete(self, key: str) -> None:
#         self._config.pop(key, None)
#         self._save()
#
#     def all(self) -> dict:
#         return dict(self._config)
#
# cfg_path = Path(__file__).parent / "config_test.json"
# cfg = ConfigManager(cfg_path)
# cfg.set("theme", "dark")
# cfg.set("language", "zh-CN")
# cfg.set("font_size", 14)
# print("所有配置:", cfg.all())
# print("theme:", cfg.get("theme"))
# cfg.delete("font_size")
# print("删除 font_size 后:", cfg.all())
# cfg_path.unlink()  # 清理

# ============================================================
# 练习 3：文件夹整理工具
# 要求：编写函数 organize_files(source_dir)，
#   - 扫描 source_dir 中的所有文件（不递归子目录）
#   - 按扩展名分类，移入子目录（如 .py -> py_files/，.txt -> txt_files/）
#   - 没有扩展名的文件放入 no_ext/ 目录
#   - 输出每类文件的数量
#   - 提示：使用 pathlib.Path，实际移动用 path.rename()
#           演示时可用 print 输出"将要移动"，不实际执行
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from pathlib import Path
# from collections import defaultdict
#
# def organize_files(source_dir: str | Path, dry_run: bool = True) -> None:
#     source = Path(source_dir)
#     groups: dict[str, list[Path]] = defaultdict(list)
#
#     for item in source.iterdir():
#         if item.is_file():
#             ext = item.suffix.lstrip(".") or "no_ext"
#             groups[ext].append(item)
#
#     for ext, files in sorted(groups.items()):
#         target_dir = source / f"{ext}_files"
#         print(f"\n  [{ext}] {len(files)} 个文件 -> {target_dir.name}/")
#         for f in files:
#             dest = target_dir / f.name
#             if dry_run:
#                 print(f"    (模拟) {f.name} -> {dest.relative_to(source)}")
#             else:
#                 target_dir.mkdir(exist_ok=True)
#                 f.rename(dest)
#                 print(f"    已移动: {f.name}")
#
# # 演示（dry_run=True，不实际移动）
# organize_files(Path(__file__).parent, dry_run=True)
