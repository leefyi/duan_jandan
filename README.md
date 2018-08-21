1.每天爬取N页jandan网(www.jandan.net)段子的程序
  主要基于requests-html(requests库作者的新库，试试水)
  
    
2.默认爬取最新的10页段子，并写入文本，每天定时以邮件附件发送


依赖：

pip install -r requirements.txt

    只依赖了如下库：
    PyYAML
    requests-html
    apscheduler
    zmail
其它依赖会自动安装

启动：
    
    入口为episode.py,
    其中包含主要调用，使用APScheduler简单做定时任务。
    定时策略比较粗糙，目前可将主程序添加为守护进程运行。

不足与后续更新：
    
    1.文本格式过于粗犷，后续会美化一下文件，再用邮件发送。
    2.目前只生成了txt文件，后续会支持更多的格式，太晚了，很困，来不及写。
    3.定时策略太原始了，过于占用系统资源，带菜J笔者学习些其它更好的再来优化。

