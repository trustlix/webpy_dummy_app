#!/usr/bin/env python
#
# -*- encoding: utf-8 -*-
#Copyright (C) 2011 Abril group

###
# Classes:
# Author : Alex Z. de Lima <alex.lima@abril.com.br>
# Descr. :
# Created: 2014 Jul 18
# Updated:
###

#def app(environ, start_response):
#      data = "Hello, World!\n"
#      start_response("200 OK", [
#          ("Content-Type", "text/plain"),
#          ("Content-Length", str(len(data)))
#      ])
#      return iter([data])


import web

urls = ( '/.*', 'hello',)

class hello:
    def GET(self):
        return "Hello, world."

app = web.application(urls, globals())
wsgiapp = app.wsgifunc()

