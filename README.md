# 金融研报管理小工具

这是一个使用 Python 编写的命令行项目，用于管理金融研报的基本信息。

当前版本已从 JSON 文件存储升级为 MySQL 数据库存储。

## 功能

- 新增研报
- 查看全部研报
- 按公司名查询研报
- 删除研报
- 日志记录

## 技术栈

- Python 3
- MySQL
- PyMySQL
- python-dotenv

## 项目结构

```text
financial_report_manager/
  main.py
  data/
    reports.json          # 旧版 JSON 数据，当前版本不再读写
  logs/
    app.log
  models/
    report.py             # 旧版数据模型，暂时保留
  services/
    report_service.py     # 研报业务和 SQL 操作
  utils/
    db_utils.py           # MySQL 连接工具
    file_utils.py         # 旧版 JSON 工具，暂时保留
  .env.example            # 环境变量示例，不包含真实密码
  .gitignore
  README.md
  requirements.txt
```

## 创建数据库和数据表

登录 MySQL 后执行：

```sql
CREATE DATABASE IF NOT EXISTS financial_report_db
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE financial_report_db;

CREATE TABLE reports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    rating VARCHAR(20) NOT NULL,
    date DATE NOT NULL
) ENGINE=InnoDB;
```

如果数据库表已经存在，不需要重复创建。

## 安装依赖

建议先进入项目虚拟环境，然后执行：

```bash
python -m pip install -r requirements.txt
```

## 配置数据库密码

根据项目根目录中的 `.env.example` 创建本地 `.env` 文件：

```text
DB_PASSWORD=你的MySQL密码
```

`.env` 中包含真实密码，已经通过 `.gitignore` 排除，不能提交到 Git。

## 运行项目

确认 MySQL 服务已经启动，然后在项目根目录执行：

```bash
python main.py
```

## 数据字段

每条研报包含：

- `id`：研报编号，由 MySQL 自动生成
- `company`：公司名
- `title`：研报标题
- `rating`：投资评级
- `date`：发布日期

## 说明

`data/reports.json` 是旧版数据文件，当前 MySQL 版本不会再读取或修改它。旧数据如需继续使用，需要单独迁移到 MySQL。
