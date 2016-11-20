
#! /usr/bin/python
# -*- coding: utf-8 -*-

debug_flag=False

def debug_set(set_boolean):
    global debug_flag
    debug_flag=set_boolean

def debug_print(content):
    global debug_flag
    if debug_flag == True:
        print content

