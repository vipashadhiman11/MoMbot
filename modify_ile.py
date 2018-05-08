fw=open("ES2a-edited.txt","w")
with open("ES2a.txt","r") as fo:
	for line in fo:
		line=line.replace("[vocalsound]","")
		line=line.replace("[disfmarker]","")
		line=line.replace("[gap]","")		
		if line.startswith("A:"):
			parts=line.split(':')
			fw.write(parts[1])
		elif line.startswith("B:"):
			parts=line.split(':')
			fw.write(parts[1])
		elif line.startswith("C:"):
			parts=line.split(':')
			fw.write(parts[1])
		elif line.startswith("D:"):
			parts=line.split(':')
			fw.write(parts[1])
		else:
			fw.write(line)
