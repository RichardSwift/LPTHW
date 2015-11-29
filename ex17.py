#!/usr/bin/python
# _*_ coding:utf-8 _*_
#Filename:ex17.py

from sys import argv
from os.path import exists #import了一个很好用的命令exists，判断文件是否存在返回True或False

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file) #打开要复制的文件，保存在中间变量中；
indata = in_file.read()# 读取这个文件，把信息保存在一个变量

print "The input file is %d bytes long" % len(indata)
#判断是否要保存拷贝信息的文件是否存在
print "Does the ouput file exist? %r" % exists(to_file) 
	
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#打开要保存拷贝信息的文件，并且将中间变量保存的信息写入该文件
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()