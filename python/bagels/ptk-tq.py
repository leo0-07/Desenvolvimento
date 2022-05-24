#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
import pymysql
from datetime import datetime
import time
from dStorage.core import dStorage

rbox = dStorage([0, "ranginho", "10"],["id", "prato", "preço"])
rbox.setdb("precinhos","pratos")
rbox.l_pdindex()
for idp in rbox.litems():
	rbox.loaddata(idp[0])
	rbox.show()
