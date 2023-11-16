# polsMint
PRC-20 POLS 自动化mint脚本
## 效果图
![image](https://github.com/chriscczhou/polsMint/assets/108380177/e703937e-0ab3-46c1-898e-2a9bd6545017)

## 依赖环境

- Python3环境 
- Git命令

## 使用说明

### 1. 下载项目源码

`git clone https://github.com/chriscczhou/polsMint.git`

### 2. 创建Python虚拟环境

```
cd polsMint
python -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```
pip install web3==6.11.3
pip install python-dotenv==1.0.0
```

### 4. 在.env文件中写入地址和私钥

### 5. 运行脚本

`python polsMint.py`
