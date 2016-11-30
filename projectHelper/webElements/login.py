# -*- coding:utf-8 -*-
from pyQa.web.importAll import *


import pdb

class SearchTextInput(TextInputElement):
    def __init__(self):
        TextInputElement.__init__(self,  "id", "kw")
       

class SearchButton(ButtonElement):
    def __init__(self):
        TextInputElement.__init__(self,  "id", "su")


class BaiduHomePage(object):
    SearchTextInput = ( "id", "kw")
    SearchButton = ("id", "su")

