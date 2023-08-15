#!/usr/bin/env python3
# coding=utf-8
"""
@File : run.py
@Author  : AT
@Create  : 2023/8/15 14:51
@Desc    :  sanic server.app to start or main
"""

from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8001, debug=True, auto_reload=True)