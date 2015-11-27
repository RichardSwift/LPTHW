#!/usr/bin/python
# _*_ coding:utf-8 _*_
#Filename: ex14.py

from sys import argv

script, user_name, user_age = argv
prompt = '> ' #这是一个命令提示符，可以改为任意值比如>>>

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "How old are you?"
age = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You are %s.
And you have a %r computer. Nice.
""" % (likes, lives, age, computer)