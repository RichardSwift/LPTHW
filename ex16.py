#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename:ex16.py

#从sys【代码库】引入argv功能
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)" #CTRL-C表示退出，Enter表示继续
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#返回 file object这个磁带机或DVD，模式为“w”
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
#turncate()是清空所有内容，谨慎使用
target.truncate()

print "Now I'm going to ask you for three lines."

#用这三个变量获取你输入的三行内容
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#将这三行内容写到txt文本里面
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()