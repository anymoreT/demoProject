# -*- coding:utf-8 -*-
from .webElement import *
import pdb
class ButtonElement(WebElement):
    def __init__(self, element_type, locator):
        WebElement.__init__(self, element_type, locator)