#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename: ex12.py

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

#%r是debug专用，显示原始字符；%s是为了显示给用户。
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)