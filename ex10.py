#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename: ex10.py

#转义符\t代表Tab
#\\代表 \
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#'''和"""效果一样
fat_cat = '''
I'll do a list.
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#死循环
while True:
	#\r代表回车
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,