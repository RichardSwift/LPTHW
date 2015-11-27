#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename:ex15.py

#sys是一个【代码库】，这句话意思是：从库里取出argv这个【功能】来给我们使用
from sys import argv

script, filename = argv
#txt = open(filename)返回的是“file object”的东西，可以想象成一个磁带机或DVD，可以任意访问内容的任意位置，并读取这些内容，但是这个object本事并不是他的内容
txt = open(filename)#和raw_input()类似，接收一个参数并返回一个值，将这个值赋给一个变量，这就是打开文件的过程。

print "Here's your file %r: " % filename
print txt.read()#在txt变量上调用函数，也就是，文件本身支持一些命令，并且可以接收参数，但是这里没有参数：意思是嘿！txt!执行你的read命令，无需任何参数。
txt.close()#处理完后一定记得关闭文件

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again) #python允许多次打开同一个文件，不会报错

print txt_again.read()
txt.close()

