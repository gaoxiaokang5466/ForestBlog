# 测试说明

仓库根目录的 `test.py` 用于对仓库结构和关键资源做冒烟测试，只检查文件与目录布局，不会连接数据库或启动 Web 项目。

## 环境要求

- Python 3.6 或更高版本
- 仅使用标准库（`unittest`、`pathlib`），无需安装第三方依赖

## 运行方式

在仓库根目录执行：

```bash
python3 test.py -v
```

`-v` 会输出每个用例的名称和结果。全部通过时退出码为 `0`，存在失败用例时退出码非 `0`。

## 测试用例

| 用例 | 检查内容 |
| --- | --- |
| `test_readme_exists` | 根目录 `README.md` 存在且非空 |
| `test_maven_project_exists` | `ForestBlog/pom.xml` 存在，且包含 `<artifactId>ForestBlog</artifactId>` |
| `test_source_tree_exists` | `ForestBlog/src` 下的 `main/java`、`main/resources`、`main/webapp`、`test/java` 均存在 |
| `test_database_dump_exists` | `forest_blog.sql` 存在且包含 `CREATE TABLE` 建表语句 |
| `test_uploaded_images_exist` | `uploads` 目录下存在图片资源（png/jpg/jpeg/gif，含子目录） |

## 适用场景

- 克隆仓库后快速确认文件是否完整
- 提交前确认没有误删关键目录或资源

## 说明

- 用例通过 `Path(__file__).resolve().parent` 定位仓库根目录，因此在任意工作目录执行均可。
- 测试数据来自仓库中的实际文件；若调整了目录结构（例如移动 `uploads` 或数据库文件），需要同步更新 `test.py`。
