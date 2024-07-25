@echo off
setlocal

REM 创建虚拟环境
python -m venv venv

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 升级pip
python -m pip install --upgrade pip

REM 如果存在requirements.txt文件，则安装依赖
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. No packages installed.
)

echo Virtual environment created and packages installed.