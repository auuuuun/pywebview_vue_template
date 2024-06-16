
<div align="center">
    <h1>pywebview_vue_template</h1>
    <h4>pywebview适合编写桌面端gui应用，用浏览器伪装gui程序</h4>
    <h4>萌新的一个小模板，方便快捷</h4>
</div>

#### github pywebview原主页
    https://github.com/r0x0r/pywebview
#### pywebview官方文档
    https://pywebview.flowrl.com/
#### 程序入口
    main.py
#### 安装教程
    pip install -r requirements.txt
#### 打包指令，没有黑窗口，并且把静态文件打包进去
    pyinstaller -F -w --add-data="static;static" main.py
#### 参数解释 
    --noconsole 打包时指定不生成控制台窗口。
    --add-data="static;static" 打包静态文件
