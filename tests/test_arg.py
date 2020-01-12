# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:23:29 2016

@author: Jee-Bee for jBae (c) 2016
"""

# Test number of arguments in *arg
# http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
# http://agiliq.com/blog/2012/06/understanding-args-and-kwargs/


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    print(len(argv))
    print(argv[1])
    for arg in argv:
        print(arg)
        print("another arg through *argv :", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')
