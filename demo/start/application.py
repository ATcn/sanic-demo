#!/usr/bin/env python3
# coding=utf-8
"""
@File : instance.py
@Author  : AT
@Create  : 2023/8/15 15:03
@Desc    : 
"""

import time
from sanic import Sanic, Request, text
from sanic.handlers import ErrorHandler
from sanic.config import Config

# instance - 创建
app = Sanic("myapp")

# context 21.3 之前的做法: app.db = Database()
app.ctx.db = Database()

# registry - 复用指定名称
app = Sanic.get_app("myapp")
# registry - 复用唯一一个
app = Sanic.get_app()
# registry - 复用自动创建
app = Sanic.get_app("myapp", force_create=True)

# config - 方式一
app.config.DB_NAME = 'appdb'
# config - 方式二
app.config['DB_USER'] = 'appuser'
# config - 方式三
db_settings = {'DB_HOST': 'localhost', 'DB_NAME': 'appdb', 'DB_USER': 'appuser'}
app.config.update(db_settings)
# config - 方式四
class MyConfig(Config):
    DB_NAME = "appdb"
app = Sanic("myapp", config=MyConfig())

# request
class NanoSecondRequest(Request):
    @classmethod
    def generate_id(*_):
        return time.time_ns()
# ErrorHandler
class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        ''' handles errors that have no error handlers assigned '''
        # You custom error handling logic...
        return super().default(request, exception)
app = Sanic("myapp", request_class=NanoSecondRequest, error_handler=CustomErrorHandler())

@app.get("/")
async def handler(request):
    return text(str(request.id))

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)