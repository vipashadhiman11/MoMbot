words1 = set(open("ES2a-edited.txt").read().split())
words2 = set(open("transcript-manual.txt").read().split())

duplicates  = words1.intersection(words2)
#uniques = words1.difference(words2).union(words2.difference(words1))

print "Duplicates(%d):%s"%(len(duplicates),duplicates)
#print "\nUniques(%d):%s"%(len(uniques),uniques)
recall = float(len(duplicates))/len(words1);
precision = float(len(duplicates))/len(words2);

print recall;
print precision;