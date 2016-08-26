# -*- coding:utf-8 -*-
from dianRongQa.web.importAll import *
import pdb

class UserNameTextInput(TextInputElement):
    def __init__(self):
        TextInputElement.__init__(self,  "id", "username")
        
class PasswordTextInput(TextInputElement):
    def __init__(self):
        TextInputElement.__init__(self,  "id", "password")        

class LoginButton(ButtonElement):
    def __init__(self):
        TextInputElement.__init__(self,  "name", "submit")               