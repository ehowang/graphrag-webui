#!/bin/bash
###
 # @Author: yancy yancyshang@duck.com
 # @Date: 2024-07-24 09:40:02
 # @LastEditors: yancy yancyshang@duck.com
 # @LastEditTime: 2024-07-24 09:40:20
 # @FilePath: \ragtest\scripts\init.sh
 # @Description: 
### 
# 创建虚拟环境
python3 -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
echo "虚拟环境创建并依赖安装完成。"