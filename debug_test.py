# -*- coding:utf-8 -*-
from testCases import test_webSite,test_http_apis

import sys

if __name__ == "__main__":
     test_webSite.WebSiteTest("test_TC001").debug()
     #test_http_apis.TestApis("test_regsiter_lender_user").debug()
    #  test_dabase.DbTest("test_mongo_db").debug()
   # test_http_apis.TestApis("test_send_mq").debug()
    
    
    
  