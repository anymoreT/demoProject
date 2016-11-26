# -*- coding:utf-8 -*-
from pyQa.web.importAll import *
import pdb


class SpanText(TextElement):
    def __init__(self, text):
        #pdb.set_trace()
        TextElement.__init__(self, "xpath", "//span[contains(text(),'%s')]" % (text))
                        
class InputText(TextInputElement):
    def __init__(self,text):
        #TextInputElement.__init__(self,"xpath","//input[@id=%s]"%(text)) 
        TextInputElement.__init__(self,"xpath","//li[contains(.,'%s')]//input"%(text))
        
class CalenderInput(TextInputElement):
    def __init__(self,text):  
        TextInputElement.__init__(self,"xpath","//input[@id='%s']"%(text))              
        
class LabelText(TextElement):
    def __init__(self, text):
        #pdb.set_trace()
        TextElement.__init__(self, "xpath", "//label[contains(text(),'%s')]" % (text))
                
class TextAreaInput(TextInputElement):
    def __init__(self,text):
        #TextElement.__init__(self,"xpath","//textarea[@name='%s']"%(text))  
        TextInputElement.__init__(self,"xpath","//li[contains(.,'%s')]//textarea"%(text))        
        
class ThText(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath", "//th[contains(text(),'%s')]"%(text))
        
class TdText(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//td[contains(text(),'%s')]"%(text))
        
class CheckBox(CheckBoxElement):
    def __init__(self,text):
        CheckBoxElement.__init__(self, "xpath", "//input[@name='%s']"%(text))
 
class TextLInk(LinkElement):
    def __init__(self, text):
        LinkElement.__init__(self, "xpath", "//a[contains(text(),'%s')]"%(text))
                 
class SingleSelect(SelectElement):
    def __init__(self,text):
        #SelectElement.__init__(self,"xpath","//select[@id='%s']"%(text))
        SelectElement.__init__(self,"xpath", "//li[contains(.,'%s')]//select"%(text))
       
class SaveButton(ButtonElement):
    def __init__(self):
        ButtonElement.__init__(self, "xpath", "//input[@value='保存']")

class SearcherButton(ButtonElement):
    def __init__(self):
        ButtonElement.__init__(self,"xpath","//button[contains(text(),'搜索')]")

class AtextButton(ButtonElement):
    def __init__(self,text):
        ButtonElement.__init__(self,"xpath","//a[contains(text(),'%s')]"%(text))
        
class ButtonText(ButtonElement):
    def __init__(self,text):
        ButtonElement.__init__(self,"xpath","//button[contains(text(),'%s')]"%(text))
        
class CheckAllCustomerTable(TableElement):
    def __init__(self):
        TableElement.__init__(self, "xpath", "//table[@id='dataList']")


        
class H1Text(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//H1[contains(text(),'%s')]"%(text))

class H1SmallText(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//h1[contains(text(),'%s')]"%(text))
        
class H2Text(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//H2[contains(text(),'%s')]"%(text))
        
class H3Text(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//H3[contains(text(),'%s')]"%(text))        
        
class H4Text(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//H4[contains(text(),'%s')]"%(text))                
   
class TextLink(LinkElement):
    def __init__(self,text):
        LinkElement.__init__(self,"xpath","//a[contains(text(),'%s')]"%(text))        
  
        
class PText(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//P[contains(text(),'%s')]"%(text))    


class StartDateInput(TextInputElement):
    def __init__(self):
        TextInputElement.__init__(self, "id", "startDate")
        
class EndDateInput(TextInputElement):
    def __init__(self):
        TextInputElement.__init__(self, "id", "endDate")        
        
        
class DivText(TextElement):
    def __init__(self,text):
        TextElement.__init__(self,"xpath","//div[contains(text(),'%s')]"%(text))        