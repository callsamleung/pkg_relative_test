#coding:utf-8

from .pkg_a.index_a import pkg_a_func

def pkg_b_func():
    print 'im pkg bbbbbbbbbbb!'

def pkg_import_a_func():
    pkg_a_func()
