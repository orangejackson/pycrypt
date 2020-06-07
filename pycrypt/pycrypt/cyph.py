#!/usr/bin/python3

keydict = {}
keyfile = "k"
fh = open(keyfile, "r")
for l in fh:
	x = l.split(" ")
	keydict[x[0]] = x[1]

files = ("found1", "found2", "found3")
