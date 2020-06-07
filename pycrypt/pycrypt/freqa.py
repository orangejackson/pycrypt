#!/usr/bin/python3

files = ("found1", "found2", "found3")

counted = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
counts = {}#dict.fromkeys(counted, 0)
counts["All"] = dict.fromkeys(counted, 0)
total = {}
total["All"] = 0

for f in files:
	counts[f] = dict.fromkeys(counted, 0)
	total[f] = 0

	fh = open(f, "r")
	for l in fh:
		for c in l:
			if c in counts[f]:
				counts[f][c] += 1
				total[f] += 1
				
			if c in counts["All"]:
				counts["All"][c] += 1
				total["All"] += 1
	fh.close()

str = "\t"
for f in files:
	str += "%s\t\t\t"
str += "%s"

print(str % (*files, "All"))

for k, v in counts["All"].items():
	str = "%s\t"
	for f in files:
		str += "%d\t%1.1f%%\t\t"
	str += "%d\t%1.1f%%"

	#this is fuck ugly
	print(str % (k, counts["found1"][k], float(counts["found1"][k]) / float(total["found1"]) * 100, counts["found2"][k], float(counts["found2"][k]) / float(total["found2"]) * 100, counts["found3"][k], float(counts["found3"][k]) / float(total["found3"]) * 100, counts["All"][k], float(counts["All"][k]) / float(total["All"]) * 100))
