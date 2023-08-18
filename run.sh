# #!/bin/bash

#进程名称
process_name=shangmen_admin

while [ 0 -eq 0 ]
do
    ps -ef|grep $process_name |grep -v grep
    # $? -ne 0 不存在，$? -eq 0 存在
    if [ $? -ne 0 ]
    then
        echo ">>>process is stop,to start"
        #启动进程
        nohup gunicorn --bind 0.0.0.0:8888 shangmen_admin.wsgi  &
        
        break
    else
        echo ">>>process is runing,to kill"
        #停止进程
        ps -ef | grep $process_name | grep -v grep | awk '{print $2}' | xargs kill
        #休眠一秒后判断
        sleep 1
    fi
done