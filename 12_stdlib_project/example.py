"""
第 12 章：综合实战 —— 命令行通讯录
综合运用前 11 章知识：OOP、异常处理、文件 I/O（JSON + pathlib）、
argparse、类型注解、dataclass、装饰器、迭代器等。

使用方式：
  python example.py add   --name 张三 --phone 13800138000 --email z@example.com
  python example.py list
  python example.py show  --name 张三
  python example.py update --name 张三 --phone 13900139000
  python example.py delete --name 张三
  python example.py search --keyword 138
  python example.py export --output contacts_export.csv

也可以直接运行（无参数）进入演示模式：
  python example.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterator

# ============================================================
# 数据层：Contact 数据类
# ============================================================

@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""
    group: str = "默认"
    note: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def matches(self, keyword: str) -> bool:
        """检查联系人是否包含关键词（名字/电话/邮箱/备注）。"""
        kw = keyword.lower()
        return any(kw in field_val.lower() for field_val in [
            self.name, self.phone, self.email, self.group, self.note
        ])

    def __str__(self) -> str:
        parts = [f"姓名: {self.name}", f"电话: {self.phone}"]
        if self.email:
            parts.append(f"邮箱: {self.email}")
        if self.group != "默认":
            parts.append(f"分组: {self.group}")
        if self.note:
            parts.append(f"备注: {self.note}")
        return " | ".join(parts)


# ============================================================
# 自定义异常
# ============================================================

class ContactBookError(Exception):
    """通讯录基础异常。"""
    pass

class ContactNotFoundError(ContactBookError):
    def __init__(self, name: str) -> None:
        super().__init__(f"联系人 '{name}' 不存在")

class DuplicateContactError(ContactBookError):
    def __init__(self, name: str) -> None:
        super().__init__(f"联系人 '{name}' 已存在")


# ============================================================
# 业务层：ContactBook
# ============================================================

class ContactBook:
    """通讯录管理类，数据持久化到 JSON 文件。"""

    def __init__(self, data_file: Path) -> None:
        self._data_file = data_file
        self._contacts: dict[str, Contact] = {}
        self._load()

    # --- 持久化 ---

    def _load(self) -> None:
        """从 JSON 文件加载联系人。"""
        if not self._data_file.exists():
            return
        try:
            with open(self._data_file, "r", encoding="utf-8") as f:
                raw: list[dict] = json.load(f)
            for item in raw:
                contact = Contact(**item)
                self._contacts[contact.name] = contact
        except (json.JSONDecodeError, TypeError) as e:
            print(f"[警告] 加载数据失败: {e}，将使用空通讯录")

    def _save(self) -> None:
        """将联系人保存到 JSON 文件。"""
        self._data_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self._data_file, "w", encoding="utf-8") as f:
            json.dump([asdict(c) for c in self._contacts.values()],
                      f, ensure_ascii=False, indent=2)

    # --- CRUD 操作 ---

    def add(self, contact: Contact) -> None:
        if contact.name in self._contacts:
            raise DuplicateContactError(contact.name)
        self._contacts[contact.name] = contact
        self._save()
        print(f"[+] 已添加联系人: {contact}")

    def get(self, name: str) -> Contact:
        if name not in self._contacts:
            raise ContactNotFoundError(name)
        return self._contacts[name]

    def update(self, name: str, **updates) -> Contact:
        contact = self.get(name)
        for key, value in updates.items():
            if not hasattr(contact, key):
                raise ContactBookError(f"无效字段: {key}")
            setattr(contact, key, value)
        self._save()
        print(f"[~] 已更新联系人: {contact}")
        return contact

    def delete(self, name: str) -> None:
        self.get(name)   # 确认存在，不存在会抛出异常
        del self._contacts[name]
        self._save()
        print(f"[-] 已删除联系人: {name}")

    def search(self, keyword: str) -> list[Contact]:
        return [c for c in self._contacts.values() if c.matches(keyword)]

    def all(self) -> list[Contact]:
        return sorted(self._contacts.values(), key=lambda c: c.name)

    # --- 导出 ---

    def export_csv(self, output_path: Path) -> int:
        """导出到 CSV 文件，返回导出条数。"""
        contacts = self.all()
        if not contacts:
            print("[!] 通讯录为空，无需导出")
            return 0
        fieldnames = list(asdict(contacts[0]).keys())
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for c in contacts:
                writer.writerow(asdict(c))
        print(f"[↗] 已导出 {len(contacts)} 条联系人到: {output_path}")
        return len(contacts)

    # --- 迭代支持 ---

    def __iter__(self) -> Iterator[Contact]:
        return iter(self.all())

    def __len__(self) -> int:
        return len(self._contacts)

    def __contains__(self, name: str) -> bool:
        return name in self._contacts


# ============================================================
# CLI 层：命令行解析
# ============================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="contacts",
        description="Python 通讯录 —— 第12章综合实战",
    )
    sub = parser.add_subparsers(dest="command")

    # add
    p_add = sub.add_parser("add", help="添加联系人")
    p_add.add_argument("--name",  required=True, help="姓名")
    p_add.add_argument("--phone", required=True, help="电话")
    p_add.add_argument("--email", default="",    help="邮箱")
    p_add.add_argument("--group", default="默认", help="分组")
    p_add.add_argument("--note",  default="",    help="备注")

    # list
    sub.add_parser("list", help="列出所有联系人")

    # show
    p_show = sub.add_parser("show", help="查看联系人详情")
    p_show.add_argument("--name", required=True, help="姓名")

    # update
    p_update = sub.add_parser("update", help="更新联系人信息")
    p_update.add_argument("--name",  required=True)
    p_update.add_argument("--phone", default=None)
    p_update.add_argument("--email", default=None)
    p_update.add_argument("--group", default=None)
    p_update.add_argument("--note",  default=None)

    # delete
    p_del = sub.add_parser("delete", help="删除联系人")
    p_del.add_argument("--name", required=True)

    # search
    p_search = sub.add_parser("search", help="搜索联系人")
    p_search.add_argument("--keyword", required=True)

    # export
    p_export = sub.add_parser("export", help="导出为 CSV")
    p_export.add_argument("--output", default="contacts_export.csv")

    return parser


def run_cli(book: ContactBook, args: argparse.Namespace) -> None:
    try:
        match args.command:
            case "add":
                book.add(Contact(
                    name=args.name, phone=args.phone,
                    email=args.email, group=args.group, note=args.note,
                ))
            case "list":
                contacts = book.all()
                if not contacts:
                    print("[i] 通讯录为空")
                else:
                    print(f"共 {len(contacts)} 位联系人:")
                    for i, c in enumerate(contacts, 1):
                        print(f"  {i:3}. {c}")
            case "show":
                print(book.get(args.name))
            case "update":
                updates = {k: v for k, v in vars(args).items()
                           if k not in ("command", "name") and v is not None}
                book.update(args.name, **updates)
            case "delete":
                book.delete(args.name)
            case "search":
                results = book.search(args.keyword)
                if not results:
                    print(f"[!] 未找到包含 '{args.keyword}' 的联系人")
                else:
                    print(f"找到 {len(results)} 条结果:")
                    for c in results:
                        print(f"  {c}")
            case "export":
                book.export_csv(Path(args.output))
            case _:
                print("[!] 未知命令，使用 --help 查看帮助")
    except ContactBookError as e:
        print(f"[错误] {e}")
    except Exception as e:
        print(f"[未知错误] {type(e).__name__}: {e}")


# ============================================================
# 演示模式（直接运行，无命令行参数）
# ============================================================

def demo(book: ContactBook) -> None:
    print("=" * 50)
    print("通讯录演示模式（综合实战）")
    print("=" * 50)

    # 添加联系人
    demo_contacts = [
        Contact("张三", "13800138001", "zhangsan@example.com", "朋友", "大学同学"),
        Contact("李四", "13800138002", "lisi@example.com", "同事"),
        Contact("王五", "13800138003", group="家人"),
        Contact("赵六", "13900139001", "zhaoliu@example.com", "朋友"),
        Contact("钱七", "13700137001", group="同事", note="项目合作"),
    ]

    print("\n--- 批量添加联系人 ---")
    for c in demo_contacts:
        try:
            book.add(c)
        except DuplicateContactError:
            pass  # 演示重复运行时跳过已有联系人

    # 列表
    print("\n--- 列出所有联系人 ---")
    for i, c in enumerate(book, 1):
        print(f"  {i}. {c}")

    # 搜索
    print("\n--- 搜索 '138' ---")
    results = book.search("138")
    for r in results:
        print(f"  {r}")

    # 更新
    print("\n--- 更新张三的备注 ---")
    book.update("张三", note="大学同学，老朋友")

    # 查看详情
    print("\n--- 查看张三 ---")
    print(book.get("张三"))

    # 导出
    print("\n--- 导出 CSV ---")
    export_path = Path(__file__).parent / "demo_export.csv"
    book.export_csv(export_path)

    # 统计
    print(f"\n通讯录总人数: {len(book)}")
    print(f"'张三' in book: {'张三' in book}")
    print(f"'马八' in book: {'马八' in book}")

    # 清理演示数据
    print("\n--- 清理演示数据 ---")
    for name in [c.name for c in demo_contacts]:
        try:
            book.delete(name)
        except ContactNotFoundError:
            pass
    if export_path.exists():
        export_path.unlink()
    print("演示完成！")


# ============================================================
# 入口
# ============================================================

if __name__ == "__main__":
    data_file = Path(__file__).parent / "contacts.json"
    book = ContactBook(data_file)

    if len(sys.argv) == 1:
        # 无参数：演示模式
        demo(book)
    else:
        parser = build_parser()
        args = parser.parse_args()
        run_cli(book, args)
