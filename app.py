import streamlit as st
import os
import subprocess
import yaml
import sys


# 初始化会话状态
if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''
# 翻译字典
translations = {
    'en': {
        'title': "GraphRAG + GPT-4o mini Retrieval Application",
        'description': "This application uses GraphRAG and GPT-4o mini to build and query knowledge graphs.",
        'install_success': "GraphRAG installed successfully!",
        'install_error': "Error installing GraphRAG: {}",
        'create_dir_success': "Created ragtest/input directory successfully!",
        'file_upload': "Upload text file",
        'file_upload_success': "File uploaded successfully!",
        'api_key_input': "Enter your OpenAI API key",
        'init_index_button': "Initialize and Build Index",
        'init_index_success': "Initialization and index building completed!",
        'init_index_error': "An error occurred: {}",
        'query_input': "Enter your query",
        'execute_query': "Execute Query",
        'query_results': "Query Results:",
        'query_error': "Query error: {}",
        'query_warning': "Please enter a query",
        'api_key_missing': "Please enter an API key before initializing."
    },
    'zh': {
        'title': "GraphRAG + GPT-4o mini 检索应用",
        'description': "这个应用程序使用GraphRAG和GPT-4o mini来构建和查询知识图谱。",
        'install_success': "GraphRAG 安装成功!",
        'install_error': "安装 GraphRAG 时出错: {}",
        'create_dir_success': "创建 ragtest/input 目录成功!",
        'file_upload': "上传文本文件",
        'file_upload_success': "文件上传成功!",
        'api_key_input': "输入您的OpenAI API密钥",
        'init_index_button': "初始化和构建索引",
        'init_index_success': "初始化和索引构建完成!",
        'init_index_error': "发生错误: {}",
        'query_input': "输入您的查询",
        'execute_query': "执行查询",
        'query_results': "查询结果:",
        'query_error': "查询出错: {}",
        'query_warning': "请输入查询内容",
        'api_key_missing': "请在初始化之前输入API密钥。"
    }
}


# 获取翻译函数
def get_text(key):
    return translations[st.session_state.language][key]

st.set_page_config(page_title=get_text('title'))

# 语言选择器
language = st.selectbox('选择语言 / Select Language', ['English', '中文'])
st.session_state.language = 'en' if language == 'English' else 'zh'



# 设置页面标题和介绍

st.title(get_text('title'))
st.write(get_text('description'))

# 安装 GraphRAG
@st.cache_resource
def install_graphrag():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "graphrag"])
        st.success(get_text('install_success'))
    except subprocess.CalledProcessError as e:
        st.error(get_text('install_error').format(e))
        st.stop()

install_graphrag()

# 创建必要的目录
if not os.path.exists("./ragtest/input"):
    os.makedirs("./ragtest/input")
    st.success(get_text('create_dir_success'))

# 文件上传功能
uploaded_file = st.file_uploader(get_text('file_upload'), type=["txt"])
if uploaded_file is not None:
    with open("./ragtest/input/book.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(get_text('file_upload_success'))

# API密钥输入
api_key = st.text_input(get_text('api_key_input'), type="password", value=st.session_state.api_key, key="api_key_input")
if api_key:
    st.session_state.api_key = api_key
    os.environ["GRAPHRAG_API_KEY"] = api_key

# 初始化和索引构建功能
if st.button(get_text('init_index_button')):
    if st.session_state.api_key:
        try:
            os.environ["GRAPHRAG_API_KEY"] = st.session_state.api_key
            subprocess.run([sys.executable, "-m", "graphrag.index", "--init", "--root", "./ragtest"], check=True)
           
            # 修改settings.yaml
            with open("./ragtest/settings.yaml", "r") as f:
                settings = yaml.safe_load(f)
            settings["llm"]["model"]= "gpt-4o-mini"
            with open("./ragtest/settings.yaml", "w") as f:
                yaml.safe_dump(settings, f)
           
            subprocess.run([sys.executable, "-m", "graphrag.index", "--root", "./ragtest"], check=True)
            st.success(get_text('init_index_success'))
        except subprocess.CalledProcessError as e:
            st.error(get_text('init_index_error').format(e))
    else:
        st.error(get_text('api_key_missing'))

# 查询功能
query = st.text_input(get_text('query_input'))
if st.button(get_text('execute_query')):
    if query:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "graphrag.query", "--root", "./ragtest", "--method", "global", query],
                capture_output=True,
                text=True,
                check=True
            )
            st.write(get_text('query_results'))
            st.write(result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(get_text('query_error').format(e))
    else:
        st.warning(get_text('query_warning'))