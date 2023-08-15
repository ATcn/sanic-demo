#!/usr/bin/env python3
# coding=utf-8
"""
@File : LoggingEnhancements.py
@Author  : AT
@Create  : 2023/8/15 16:45
@Desc    : 
"""
from sanic import Sanic
from sanic import response
import logging

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG
)
log = logging.getLogger()

# Set logger to override default basicConfig
app = Sanic('myapp')


@app.route("/")
def test(request):
    log.info("received request; responding with 'hey'")
    return response.text("hey")

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)