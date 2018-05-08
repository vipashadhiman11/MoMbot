from difflib import SequenceMatcher
text1 = open("transcript-manual.txt").read()
text2 = open("stopwords.txt").read()
s = SequenceMatcher(lambda x: x == " ", text1, text2)
print round(s.ratio(), 3)