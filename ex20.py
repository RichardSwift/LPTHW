#!/usr/bin/python
# _*_ coding:utf-8 _*_
#Filename:ex20.py:函数和文件

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
		
def rewind(f):
	f.seek(0) #python的文件和磁带机一样，有一个读取数据的磁头，每次运行f.seek（0）就回到了文件开始而运行；运行f.readline()则读取文件一行，然后将磁头移动到\n后面
		
def print_a_line(line_count, f):
	print line_count, f.readline()
		
current_file = open(input_file)

#添加逗号，那么就不会打印print本身的\n，仍然会打印磁头读取的那个\n，因此一共就是一个\n
print "First let's print the whole file:\n",

print_all(current_file) #调用函数，读取文件

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)