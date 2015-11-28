#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename: ex8.py

#应该使用%s为好，只有在想获取某些东西的debug信息时才用到%r。 
formatter = "%r %r %r %r"
	
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "fout")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter,formatter)
print formatter % (
	"I had this string.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
