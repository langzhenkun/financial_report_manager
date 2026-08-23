import logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

from services.report_service import get_all_reports, add_report,search_reports_by_company,delete_report
from datetime import datetime


def show_menu():
    print("\n====== 金融研报管理小工具 ======")
    print("1. 新增研报")
    print("2. 查看全部研报")
    print("3. 按公司名查询研报")
    print("4. 删除研报")
    print("5. 退出程序")

def print_report(report):
    print("------------")
    print(f"编号：{report['id']}")
    print(f"公司名：{report['company']}")
    print(f"研报标题：{report['title']}")
    print(f"投资评级：{report['rating']}")
    print(f"发布日期：{report['date']}")
    print("------------")


def main():
    logging.info("程序启动")

    while True:
        show_menu()

        choice = input("请输入你的选择：").strip()

        if choice == "1":
            company = input("请输入公司名：").strip()
            title = input("请输入研报标题：").strip()
            rating = input("请输入投资评级：").strip()
            date = input("请输入发布日期：").strip()

            if company == "" or title == "" or rating == "" or date == "":
                print("新增失败：公司名、标题、评级、日期都不能为空")
                logging.warning("新增研报失败：存在空字段")
                continue

            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("输入的日期格式有误，请重新输入:年-月-日")
                logging.warning(f"新增研报失败,日期格式有误,输入值:{date}")
                continue

            add_report(company, title, rating, date)
            print("研报添加成功")
            logging.info(f"新增研报成功：{company} - {title}")
        elif choice == "2":
            reports = get_all_reports()
            if len(reports) == 0:
                print("当前暂无研报")
            else:
                print(f"共找到 {len(reports)} 份研报")
                for report in reports:
                    print_report(report)
        elif choice == "3":
            company = input("请输入公司名：").strip()
            reports = search_reports_by_company(company)
            if len(reports) == 0:
                print("未找到该公司研报")
            else:
                for report in reports:
                    print_report(report)
        elif choice == "4":
            try:
                report_id = int(input("请输入要删除的研报编号：").strip())
            except ValueError:
                print("输入有误，请重新输入,编号必须是数字")
                logging.warning("删除研报失败：编号不是数字")
                continue

            if delete_report(report_id):
                print("研报删除成功")
                logging.info(f"删除研报成功：编号 {report_id}")
            else:
                print("未找到该研报")
                logging.warning(f"删除研报失败：编号 {report_id}")
        elif choice == "5":
            print("程序已退出")
            logging.info("程序退出")
            break
        else:
            print("输入有误，请重新输入")
            logging.warning(f"菜单输入错误：{choice}")
            continue


if __name__ == "__main__":
    main()