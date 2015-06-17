#!/usr/bin/env python

import http_server
import os

os.system("./parser")

http_server.load_url('test1.html')
