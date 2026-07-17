from models.report import Report
from utils.file_utils import read_json, write_json

REPORT_FILE = "data/reports.json"

def get_all_reports():
    reports = read_json(REPORT_FILE)
    return reports

def add_report(company, title, rating, date):
    reports = read_json(REPORT_FILE)
    new_id = max(report["id"] for report in reports) + 1
    report = Report(new_id, company, title, rating, date)
    reports.append(report.to_dict())
    write_json(REPORT_FILE, reports)

def search_reports_by_company(company):
    reports = read_json(REPORT_FILE)

    result = []

    for report in reports:
        if report["company"] == company:
            result.append(report)

    return result

def delete_report(report_id):
    reports = read_json(REPORT_FILE)
    for i in range(len(reports)):
        if reports[i]["id"] == report_id:
            reports.pop(i)
            write_json(REPORT_FILE, reports)
            return True
    return False

