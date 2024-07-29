<!--
 * @Author: yancy yancyshang@duck.com
 * @Date: 2024-07-26 13:56:18
 * @LastEditors: yancy yancyshang@duck.com
 * @LastEditTime: 2024-07-26 14:09:19
 * @FilePath: \ragtest\readme_CN.md
 * @Description: 
-->

# GraphRAG + GPT-4o mini 知识图谱检索应用

[中文版](README_CN.md) | [English](README.md)
## 简介

这是一个基于 Streamlit 的 Web 应用程序，利用 GraphRAG 和 GPT-4o mini 构建并查询知识图谱。该应用支持中英文界面，允许用户上传文本文件，构建知识索引，并执行查询操作。

## 功能特点

- 双语界面（中文/英文）
- 文本文件上传
- 自动安装 GraphRAG
- 知识图谱索引构建
- 基于 GPT-4o mini 的查询功能

## 安装要求

- Python 3.7+
- Streamlit
- GraphRAG（应用程序会自动安装）
- OpenAI API 密钥

## 安装步骤

1. 克隆此仓库 ``` git clone 仓库URL```
2. 跳转到项目目录下根据不同的系统执行init脚本


## 使用方法

1. 运行应用程序：```streamlit run app.py```

2. 在浏览器中打开显示的 URL（通常是 http://localhost:8501）。

3. 使用界面：
- 选择您偏好的语言（中文/英文）
- 上传文本文件（.txt 格式）
- 输入您的 OpenAI API 密钥
- 点击"初始化和构建索引"按钮
- 在查询框中输入您的问题，然后点击"执行查询"

## 注意事项

- 确保您有有效的 OpenAI API 密钥。
- 上传的文本文件应为纯文本格式（.txt）。
- 首次运行时，应用程序会自动安装 GraphRAG，这可能需要一些时间。

## 故障排除

如果遇到问题：
- 确保您的 Python 版本兼容（3.7+）
- 检查 API 密钥是否正确输入
- 查看控制台输出以获取详细的错误信息

## 贡献

欢迎提交 issues 和 pull requests 来帮助改进这个项目。

