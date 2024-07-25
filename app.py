'''
Author: yancy yancyshang@duck.com
Date: 2024-07-24 09:39:09
LastEditors: yancy yancyshang@duck.com
LastEditTime: 2024-07-25 13:30:21
FilePath: \ragtest\app.py
Description: 
'''
import streamlit as st
import os
import subprocess
import yaml
import sys

# 设置页面标题和介绍
st.set_page_config(page_title="GraphRAG + GPT-4o mini 检索应用")
st.title("GraphRAG + GPT-4o mini 知识图谱检索")
st.write("这个应用程序使用GraphRAG和GPT-4o mini来构建和查询知识图谱。")

# 安装 GraphRAG
@st.cache_resource
def install_graphrag():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "graphrag"])
        st.success("GraphRAG 安装成功!")
    except subprocess.CalledProcessError as e:
        st.error(f"安装 GraphRAG 时出错: {e}")
        st.stop()

install_graphrag()

# 创建必要的目录
if not os.path.exists("./ragtest/input"):
    os.makedirs("./ragtest/input")
    st.success("创建 ragtest/input 目录成功!")

# 文件上传功能
uploaded_file = st.file_uploader("上传文本文件", type=["txt"])
if uploaded_file is not None:
    with open("./ragtest/input/book.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("文件上传成功!")

# API密钥输入
api_key = st.text_input("输入您的OpenAI API密钥", type="password")
if api_key:
    os.environ["GRAPHRAG_API_KEY"] = api_key

# 初始化和索引构建功能
if st.button("初始化和构建索引"):
    try:
        subprocess.run([sys.executable, "-m", "graphrag.index", "--init", "--root", "./ragtest"], check=True)
        
        # 修改settings.yaml
        with open("./ragtest/settings.yaml", "r") as f:
            settings = yaml.safe_load(f)
        settings["llm"]["model"]= "gpt-4o-mini"
        with open("./ragtest/settings.yaml", "w") as f:
            yaml.safe_dump(settings, f)
        
        subprocess.run([sys.executable, "-m", "graphrag.index", "--root", "./ragtest"], check=True)
        st.success("初始化和索引构建完成!")
    except subprocess.CalledProcessError as e:
        st.error(f"发生错误: {e}")

# 查询功能
query = st.text_input("输入您的查询")
if st.button("执行查询"):
    if query:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "graphrag.query", "--root", "./ragtest", "--method", "global", query],
                capture_output=True,
                text=True,
                check=True
            )
            st.write("查询结果:")
            st.write(result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(f"查询出错: {e}")
    else:
        st.warning("请输入查询内容")