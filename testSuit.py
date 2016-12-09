# -*- coding:utf-8 -*-
from unittest import TestSuite,TestLoader
from pyQa import HTMLTestRunner 
import pdb
import sys,os
from pyQa.globalFactory.globalVars import GlobalFactory

def run_all_cases():
    current_dir = os.path.dirname(__file__)
    testSuit_path = os.path.join(current_dir, "testCases")
    all_suits = TestLoader().discover(testSuit_path)
    run_suit(all_suits)
    if GlobalFactory.get_error_count() > 0:
        raise Exception("meet error: %d", GlobalFactory.get_error_count())

def run_suit(suit):
    root_path = os.path.dirname(".")
    root_path = os.path.join(root_path, "report")
    filename = 'result.html'
    report_path = os.path.join(root_path, filename)
    file_handle= open(report_path, 'wb')
    runner = get_runner(file_handle)
    runner.run(suit)
 
def get_runner(file_handle):
    runner = HTMLTestRunner.HTMLTestRunner(stream= file_handle, title="Demo testing result")    
    return runner
 
run_all_cases()    

  