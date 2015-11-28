#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Filename: ex6.py

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "There who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#注意：%r是会被替换成False的！
#%r用来debug最好，因为它显示变量的原始数据(raw data)
#而%s等则用来向用户显示输出的
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
