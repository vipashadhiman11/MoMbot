text1 = open("transcript-manual.txt").read()
text2 = open("stopwords.txt").read()
str1=text1.split()
str2=text2.split()
count=0
for i in range( 0,len(str1)):
	for j in range(0,len(str2)):        
                if str1[i] == str2[j]:
                  	count=count+1
                  	i=i+1
                  	j=j+1
# if count <= len(str1):
print count,len(str1)
per = (count /len(str1))
# else:
#     per = 100
print per
