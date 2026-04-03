"""
第 12 章：练习题 —— 扩展通讯录功能
在 example.py 的基础上，完成以下三个扩展任务。
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：导入 CSV 功能
# 要求：为 ContactBook 添加 import_csv(csv_path) 方法
#   - 读取 CSV 文件（与 export_csv 的格式对应）
#   - 跳过已存在的联系人（不报错，但计数）
#   - 返回 (imported, skipped) 元组
#   - 演示：先调用 export_csv 导出，清空数据，再用 import_csv 恢复
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import csv
# import json
# from dataclasses import asdict
# from pathlib import Path
# from example import Contact, ContactBook, DuplicateContactError
#
# def import_csv(book: ContactBook, csv_path: Path):
#     imported = skipped = 0
#     with open(csv_path, "r", encoding="utf-8", newline="") as f:
#         for row in csv.DictReader(f):
#             try:
#                 book.add(Contact(**row))
#                 imported += 1
#             except DuplicateContactError:
#                 skipped += 1
#     print(f"[↙] 导入完成: {imported} 条成功, {skipped} 条跳过")
#     return imported, skipped
#
# # 演示
# data_file = Path(__file__).parent / "contacts_import_test.json"
# book = ContactBook(data_file)
# # 先添加几个联系人
# for name, phone in [("测试A", "111"), ("测试B", "222")]:
#     try:
#         book.add(Contact(name=name, phone=phone))
#     except Exception:
#         pass
# # 导出
# export_path = Path(__file__).parent / "import_test.csv"
# book.export_csv(export_path)
# # 清空
# data_file.write_text("[]", encoding="utf-8")
# book2 = ContactBook(data_file)
# # 导入
# imported, skipped = import_csv(book2, export_path)
# print(f"恢复后人数: {len(book2)}")
# # 清理
# data_file.unlink(missing_ok=True)
# export_path.unlink(missing_ok=True)

# ============================================================
# 练习 2：分组统计与报告
# 要求：为 ContactBook 添加 group_summary() 方法
#   - 按 group 字段分组统计人数
#   - 返回 dict[str, list[Contact]]
#   - 额外编写 print_report(book) 函数，输出格式：
#
#   ==== 通讯录分组报告 ====
#   [朋友] 2人
#     - 张三  13800138001
#     - 赵六  13900139001
#   [同事] 2人
#     ...
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from collections import defaultdict
# from pathlib import Path
# from example import Contact, ContactBook
#
# def group_summary(book: ContactBook) -> dict[str, list[Contact]]:
#     groups: dict[str, list[Contact]] = defaultdict(list)
#     for contact in book:
#         groups[contact.group].append(contact)
#     return dict(groups)
#
# def print_report(book: ContactBook) -> None:
#     groups = group_summary(book)
#     print("==== 通讯录分组报告 ====")
#     for group_name in sorted(groups.keys()):
#         members = sorted(groups[group_name], key=lambda c: c.name)
#         print(f"\n[{group_name}] {len(members)}人")
#         for c in members:
#             print(f"  - {c.name:<6} {c.phone}")
#
# # 演示
# data_file = Path(__file__).parent / "contacts_report_test.json"
# book = ContactBook(data_file)
# test_contacts = [
#     Contact("张三", "138001", group="朋友"),
#     Contact("李四", "138002", group="同事"),
#     Contact("王五", "138003", group="朋友"),
#     Contact("赵六", "139001", group="家人"),
# ]
# for c in test_contacts:
#     try:
#         book.add(c)
#     except Exception:
#         pass
# print_report(book)
# data_file.unlink(missing_ok=True)

# ============================================================
# 练习 3：交互式命令行界面（REPL）
# 要求：编写 interactive_shell(book) 函数，实现一个简单的交互式通讯录
#   - 命令：add/list/search/delete/quit
#   - 输入 "quit" 或 "exit" 退出
#   - 每次操作后显示结果
#   - 捕获所有异常，友好提示
#   （不需要真正等待用户输入，用列表模拟命令序列演示即可）
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from pathlib import Path
# from example import Contact, ContactBook, ContactBookError
#
# def interactive_shell(book: ContactBook, commands: list[str] | None = None) -> None:
#     """
#     交互式 REPL。如果提供 commands 列表则依次执行（用于演示）；
#     否则从 input() 读取（真实交互）。
#     """
#     HELP = """
# 可用命令:
#   add <姓名> <电话> [邮箱]  - 添加联系人
#   list                      - 列出所有联系人
#   search <关键词>            - 搜索
#   delete <姓名>             - 删除
#   quit / exit               - 退出
# """
#     print("=== 通讯录交互模式 ===")
#     print(HELP)
#
#     cmd_iter = iter(commands) if commands else None
#
#     while True:
#         try:
#             if cmd_iter:
#                 try:
#                     line = next(cmd_iter)
#                     print(f">>> {line}")
#                 except StopIteration:
#                     break
#             else:
#                 line = input(">>> ").strip()
#
#             if not line:
#                 continue
#             parts = line.split()
#             cmd = parts[0].lower()
#
#             match cmd:
#                 case "quit" | "exit":
#                     print("再见！")
#                     break
#                 case "list":
#                     contacts = book.all()
#                     print(f"共 {len(contacts)} 位联系人:")
#                     for c in contacts:
#                         print(f"  {c}")
#                 case "add":
#                     if len(parts) < 3:
#                         print("用法: add <姓名> <电话> [邮箱]")
#                         continue
#                     name, phone = parts[1], parts[2]
#                     email = parts[3] if len(parts) > 3 else ""
#                     book.add(Contact(name=name, phone=phone, email=email))
#                 case "search":
#                     if len(parts) < 2:
#                         print("用法: search <关键词>")
#                         continue
#                     results = book.search(parts[1])
#                     for r in results:
#                         print(f"  {r}")
#                     if not results:
#                         print(f"未找到 '{parts[1]}'")
#                 case "delete":
#                     if len(parts) < 2:
#                         print("用法: delete <姓名>")
#                         continue
#                     book.delete(parts[1])
#                 case _:
#                     print(f"未知命令 '{cmd}'，{HELP}")
#
#         except ContactBookError as e:
#             print(f"[错误] {e}")
#         except KeyboardInterrupt:
#             print("\n中断，退出")
#             break
#
# # 演示
# data_file = Path(__file__).parent / "contacts_repl_test.json"
# book = ContactBook(data_file)
# interactive_shell(book, commands=[
#     "add 小明 18600000001 xm@test.com",
#     "add 小红 18600000002",
#     "list",
#     "search 186",
#     "delete 小明",
#     "list",
#     "quit",
# ])
# data_file.unlink(missing_ok=True)
