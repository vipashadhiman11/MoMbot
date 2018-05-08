import textrank

def extract_summary(filename):
	fr=open("summarise.txt","w")
	with open(filename) as f:
		summary = textrank.extract_sentences(f.read())
		fr.write(summary)


extract_summary("transcript-manual.txt")
