#!/usr/bin/python
# _*_ coding:utf-8 _*_
#Filename:ex18.py:命名、变量、代码行数

#这里面的*号是告诉python让它把函数所有参数接收进来，并放到名字叫args的列表中去
def print_two(*args):
	arg1, arg2 = args #将参数解包，和脚本参数解包原理差不多
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#这个函数跳过了整个参数解包的过程直接使用()里面的名称作为变量名
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
		
def print_one(arg1):
	print "arg1: %r" % arg1
		
def print_none():
	print "I got nothin'."
		
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

