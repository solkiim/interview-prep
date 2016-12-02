#!/usr/bin/python

f = open("test1.txt", "w+")

for i in range(1, 201):
	f.write("insert " + str(i) + "\n")

for i in range(80, 101):
	f.write("delete " + str(i) + "\n")
	f.write("checkNotExists " + str(i) + "\n")

f.close()
