# agent
智能体

生成虚拟环境

### 生成虚拟环境
python3 -m venv .venv

会在代码库agent文件夹下生成.venv文件，.venv文件下有bin、include、lib等文件

### 激活虚拟环境
source .venv/bin/activate

### 安装后端依赖并启动服务
pip install -r requirements.txt   
uvicorn main:app --reload

启动


