## **更新了脚本使用文档—马蹄POLY铭文脚本使用教程（来自社区）.pdf**

# polsMint
PRC-20 POLS 自动化mint脚本

该脚本同时也兼容其他EVM链，需要修改3处代码。

 - 换rpc地址：找到代码中的`rpc_url = "https://1rpc.io/matic"`，打开chainlist.org查看可用的rpc节点进行替换
 - 修改chainId：找到代码中`'chainId': 137`,根据chainlist.org查看对应链的chainId进行替换
 - 修改交易的data：找到代码中的`'data':'0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a22706f6c73222c22616d74223a22313030303030303030227d'`，使用utf8-hex.py把mint字符串转换后替换



## 效果图
![image](https://github.com/chriscczhou/polsMint/assets/108380177/e703937e-0ab3-46c1-898e-2a9bd6545017)

## 依赖环境

- Python3环境 
- Git命令

## 使用说明（新版）

### 1. 下载项目源码

```
git clone https://github.com/chriscczhou/polsMint.git
```

### 2. 创建Python虚拟环境(非必需步骤)

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

```
python polsMint.py
```
