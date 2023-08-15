#!/usr/bin/env python3
# coding=utf-8
"""
@File : URLRedirect.py
@Author  : AT
@Create  : 2023/8/15 16:38
@Desc    : 
"""

from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route('/')
def handle_request(request):
    return response.redirect('/redirect')


@app.route('/redirect')
async def test(request):
    return response.json({"Redirected": True})


if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)