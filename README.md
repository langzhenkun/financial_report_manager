# 金融研报管理小工具

这是一个 Python 命令行项目，用于管理金融研报的基本信息。

## 功能

- 新增研报
- 查看全部研报
- 按公司名查询研报
- 删除研报
- 日志记录

## 项目结构

```text
financial_report_manager/
  main.py
  data/
    reports.json
  logs/
    app.log
  models/
    report.py
  services/
    report_service.py
  utils/
    file_utils.py
  README.md
  requirements.txt
```

## 运行方式

```bash
python main.py
```

## 数据字段

每条研报包含：

- id：研报编号
- company：公司名
- title：研报标题
- rating：投资评级
- date：发布日期