# Simulation for network bridge(SNB)  
网桥仿真模拟

### 安装
相关依赖在`requests.txt`文件中  
使用命令 `pip install -r requests.txt`安装依赖

### 开始
在pyccharm中启动`main.py`  
命令行输入`help`可查看所有支持的命令  
按照提示可以执行仿真模拟

### 结束
命令行输入`quit`


### 项目结构

```
├── LICENSE
├── requests.txt    项目依赖清单
├── README.md       readme
├── bin             脚本目录
├── docs            文档目录
├── release         打包目录
└── src
    ├── console     交互模块
    ├── core        核心模块
    ├── data        数据模块
    ├── main.py     程序入口
    ├── manager     管理模块
    ├── nodes       节点模块
    ├── spreader    传播模块
    ├── utils       工具模块
    ├── resource    静态资源文件
    └── view        视图模块
```

