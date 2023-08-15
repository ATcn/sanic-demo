#!/usr/bin/env python3
# coding=utf-8
"""
@File : Rollbar.py
@Author  : AT
@Create  : 2023/8/15 17:06
@Desc    : 
"""
import rollbar

from sanic.handlers import ErrorHandler
from sanic import Sanic
from sanic.exceptions import SanicException
from os import getenv

rollbar.init(getenv("ROLLBAR_API_KEY"))


class RollbarExceptionHandler(ErrorHandler):

    def default(self, request, exception):
        rollbar.report_message(str(exception))
        return super().default(request, exception)


app = Sanic(__name__, error_handler=RollbarExceptionHandler())


@app.route("/raise")
def create_error(request):
    raise SanicException("I was here and I don't like where I am")

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)