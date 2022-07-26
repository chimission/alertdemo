# Prometheus 钉钉报警demo

## 使用

### 安装docker-compose

### 在 dingtalk.py 里更换自己的钉钉机器人api链接

### 根目录运行 docker-compose up -d --build 启动服务

### 执行 cat /dev/zero > /dev/null 占用cpu

### 查看监控状态

[cpu监控](http://127.0.0.1:9090/graph?g0.expr=sum(avg%20without%20(cpu)(irate(node_cpu_seconds_total%7Bmode!%3D%27idle%27%7D%5B30s%5D)))&g0.tab=0&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h)  

[报警监控](http://127.0.0.1:9090/alerts)  

[alertmanager](http://192.168.33.10:9093/#/silences)  

### 等待1m中左右钉钉机器人发送消息
