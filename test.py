#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'yang'

from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
