#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename:ex11.py

#每行print后面加逗号，不换行
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
