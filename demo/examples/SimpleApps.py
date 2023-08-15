#!/usr/bin/env python3
# coding=utf-8
"""
@File : SimpleApps.py
@Author  : AT
@Create  : 2023/8/15 16:27
@Desc    : 
"""

from sanic import Sanic
from sanic import response as res

app = Sanic(__name__)


@app.route("/")
async def home(req):
    return res.text("I\'m a teapot", status=418)

@app.route("/json")
async def _json(request):
    return res.json({"test": True})


if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)