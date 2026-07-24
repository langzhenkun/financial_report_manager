from utils.db_utils import get_connection


def get_all_reports():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "select id, company, title, rating, date from reports order by id"
        cursor.execute(sql)
        reports = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return reports

def add_report(company, title, rating, date):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "insert into reports(company, title, rating, date) values(%s, %s, %s, %s)"
        cursor.execute(sql, (company, title, rating, date))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def search_reports_by_company(company):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = """
            select id, company, title, rating, date
            from reports
            where company = %s
            order by id
        """
        cursor.execute(sql, (company,))
        reports = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return reports

def delete_report(report_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = """
            delete from reports
            where id = %s
        """
        cursor.execute(sql, (report_id,))
        affected_rows = cursor.rowcount
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
    return affected_rows > 0

