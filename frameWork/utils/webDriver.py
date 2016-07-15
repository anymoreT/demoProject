# -*- coding:utf-8 -*-
from selenium import webdriver
from frameWork.global_list.global_var import Global_factory
#from sqlalchemy.sql.sqltypes import Interval
import time
import pdb
from selenium.webdriver.chrome.options import Options
from frameWork.log.log import Log

class WebDriver(object):
    driver = None
    @staticmethod
    def start_driver(brower = None):
        global_config = Global_factory.get_global_config()
        if brower is not None:
            global_config['browser'] = brower.strip() 
        if global_config['browser'] == 'chrome' :
#             chromeOptions = Options()
#             prefs = {'profile.default_content_settings.multiple-automatic-downloads': 1, 'download.prompt_for_download' : False, 'download.default_directory' : "d:"}
#             chromeOptions.add_experimental_option("prefs", prefs)
#             WebDriver.driver = webdriver.Chrome(chrome_options = chromeOptions)
            WebDriver.driver = webdriver.Chrome()
        else:    
            WebDriver.driver = webdriver.Firefox()
        WebDriver.driver.maximize_window()
        Global_factory.set_driver(WebDriver.driver)
     

            
    @staticmethod
    def go_to_url(url):
        WebDriver.driver.get(url)
        
    @staticmethod    
    def wait_page_load(timeout = 30, interval = 3):
        times = int(timeout/interval)
        for i in range(times):
            if "complete" == WebDriver.driver.execute_script('return document.readyState'):
                time.sleep(2)
                return True
            else:
                time.sleep(interval)  
        else:
            raise("page is still loading")           
        #WebDriver.driver.wait_for_page_to_load()
        
    @staticmethod
    def refresh_page():
        WebDriver.driver.refresh()
        
    @staticmethod
    def quit():
        try :
            WebDriver.driver.quit()
        except:
            Log.log_error_info("+++++close driver meet error" )     
        
    @staticmethod
    def get_cookie():
        pass
    
    @staticmethod
    def del_all_cookie():
        WebDriver.driver.delete_all_visible_cookies()
    
    @staticmethod
    def back(self):
        WebDriver.driver.go_back()
    
    @staticmethod
    def switch_to_frame(frame_name):
        """
         :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """
        WebDriver.driver.switch_to_frame(frame_name)
     
    @staticmethod   
    def get_window_handles():
        return WebDriver.driver.window_handles
    
    @staticmethod     
    def switch_to_window(window):
        WebDriver.driver.switch_to.window(window)    