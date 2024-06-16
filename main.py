from contextlib import redirect_stdout
from io import StringIO

from app.views import app
from app.views import socketio

import webview
import threading


def run_server(port):
    socketio.run(app, allow_unsafe_werkzeug=True, port=port)


# 程序入口
if __name__ == '__main__':
    port = webview.http._get_random_port()
    # 创建flask服务器
    threading.Thread(target=run_server, args=(port,)).start()

    window = webview.create_window(title='pwwebview', width=400, height=300, url=f"http://127.0.0.1:{port}")
    webview.start(debug=True)
    # webview.start(run_server(port), debug=True, http_server=True)
