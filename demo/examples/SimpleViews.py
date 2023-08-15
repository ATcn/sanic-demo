#!/usr/bin/env python3
# coding=utf-8
"""
@File : SimpleViews.py
@Author  : AT
@Create  : 2023/8/15 16:34
@Desc    : 
"""
from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')


class SimpleView(HTTPMethodView):

    def get(self, request):
        return text('I am get method')

    def post(self, request):
        return text('I am post method')

    def put(self, request):
        return text('I am put method')

    def patch(self, request):
        return text('I am patch method')

    def delete(self, request):
        return text('I am delete method')


class SimpleAsyncView(HTTPMethodView):

    async def get(self, request):
        return text('I am async get method')

    async def post(self, request):
        return text('I am async post method')

    async def put(self, request):
        return text('I am async put method')


app.add_route(SimpleView.as_view(), '/')
app.add_route(SimpleAsyncView.as_view(), '/async')

if __name__ == '__main__':
    app.run(host="192.168.1.120", port=8000, debug=True, auto_reload=True)