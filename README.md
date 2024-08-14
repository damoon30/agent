# agent
智能体

生成虚拟环境

### 生成虚拟环境
python3 -m venv /you/project/path/agent

会在代码库server文件夹下生成 bin、include、lib等文件

### 激活虚拟环境
source /you/project/path/agent/bin/activate

### 安装后端依赖并启动服务
cd agent  
pip install -r requirements.txt   
uvicorn main:app --reload





