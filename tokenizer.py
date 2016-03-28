import sys

file=open(sys.argv[1],"r+")
words={}

wordTotalCount = 0.0;
wordTypeCount = 0.0;

for word in file.read().split():
	if word not in words:
  		words[word] = 1
  		wordTypeCount = wordTypeCount + 1
	else:
  		words[word] += 1

	wordTotalCount = wordTotalCount + 1
for key in words.keys():
	print ("%s %s " %(key , words[key]))

print "===================="
print "type : " + str(wordTypeCount) + ", word : " + str(wordTotalCount)
print "TTL is " + str(wordTypeCount / wordTotalCount)

file.close();