#!/usr/bin/python

import string
from random import choice

def GenPasswd(length, chars):
   return ''.join([choice(chars) for i in range(length)])

password = GenPasswd(16, string.letters + string.digits)

print "16 chars long: %s" % password