#!/usr/bin/env python3
# coding=utf-8
"""
@File : Concurrency.py
@Author  : AT
@Create  : 2023/8/15 16:54
@Desc    : 
"""
from sanic import Sanic
from sanic.response import json

import asyncio
import aiohttp

app = Sanic(__name__)

sem = None


@app.listener('before_server_start')
def init(sanic, loop):
    global sem
    concurrency_per_worker = 4
    sem = asyncio.Semaphore(concurrency_per_worker, loop=loop)

async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with sem, session.get(url) as response:
        return await response.json()


@app.route("/")
async def test(request):
    """
    Download and serve example JSON
    """
    url = "https://api.github.com/repos/channelcat/sanic"

    async with aiohttp.ClientSession() as session:
        response = await bounded_fetch(session, url)
        return json(response)

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)