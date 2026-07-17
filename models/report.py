class Report:
    def __init__(self, report_id, company, title, rating, date):
        self.report_id = report_id
        self.company = company
        self.title = title
        self.rating = rating
        self.date = date


    def to_dict(self):
        return {
            "id": self.report_id,
            "company": self.company,#公司名
            "title": self.title,#标题
            "rating": self.rating,#评级
            "date": self.date#日期
        }