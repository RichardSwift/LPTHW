#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename: ex13.py

#import将Python的功能引入我们的脚本
#argv是参数变量，它包含了我们传递给Python的参数
from sys import argv

#将argv中的东西解包(unpack)，将所有参数依次赋给左边变量名
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
x = raw_input()
y = raw_input()
#python ex13.py apple banana pear表示输入4个参数
#假如参数个数不足，会报错
#模组(modulws)为脚本提供额外功能
#argv和raw_input()区别是输入时机不同：argv是用户在执行命令时输入参数，而raw_input()则是在脚本运行过程中输入参数。