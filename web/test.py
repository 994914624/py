#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'yang'

from bottle import route, run, template

@route()
@route('/')
@route('/<name>')
def index(name):
    if name in "jssdk":
        return template('jssdk.html', template_lookup=['/Users/yang/Desktop/py/web/templates/'],name=name)
    else:
        return template('base.html', template_lookup=['/Users/yang/Desktop/py/web/templates/'],name=name)

run(host='127.0.0.1', port=8888)

