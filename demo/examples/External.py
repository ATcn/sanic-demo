#!/usr/bin/env python3
# coding=utf-8
"""
@File : External.py
@Author  : AT
@Create  : 2023/8/15 17:04
@Desc    : 
"""
import logging
import socket
from os import getenv
from platform import node
from uuid import getnode as get_mac

from logdna import LogDNAHandler

from sanic import Sanic
from sanic.response import json
from sanic.request import Request

log = logging.getLogger('logdna')
log.setLevel(logging.INFO)


def get_my_ip_address(remote_server="google.com"):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((remote_server, 80))
        return s.getsockname()[0]


def get_mac_address():
    h = iter(hex(get_mac())[2:].zfill(12))
    return ":".join(i + next(h) for i in h)


logdna_options = {
    "app": __name__,
    "index_meta": True,
    "hostname": node(),
    "ip": get_my_ip_address(),
    "mac": get_mac_address()
}

logdna_handler = LogDNAHandler(getenv("LOGDNA_API_KEY"), options=logdna_options)

logdna = logging.getLogger(__name__)
logdna.setLevel(logging.INFO)
logdna.addHandler(logdna_handler)

app = Sanic(__name__)


@app.middleware
def log_request(request: Request):
    logdna.info("I was Here with a new Request to URL: {}".format(request.url))


@app.route("/")
def default(request):
    return json({
        "response": "I was here"
    })


if __name__ == "__main__":
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)