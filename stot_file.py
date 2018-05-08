import speech_recognition as sr
# use the audio file as the audio source
r = sr.Recognizer()


AUDIO_FILE="out000000000.wav"

with sr.AudioFile(AUDIO_FILE) as source:
	    #reads the audio file. Here we use record instead of isten
	audio = r.record(source)  
	 
try:
	fo = open("/Users/Aditi/Desktop/Mombot-web/outputm.txt", "a")
	fo.write(" "+r.recognize_google(audio))
	 
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
	 
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
# for i in range(10,80):
# 	AUDIO_FILE="partsc/out0000000"+str(i)+".wav"

# 	with sr.AudioFile(AUDIO_FILE) as source:
# 	    #reads the audio file. Here we use record instead of listen
# 	    audio = r.record(source)  
	 
# 	try:
# 		fr = open("/Users/Aditi/Desktop/Mombot-web/outputm.txt", "a")
# 		fr.write(r.recognize_google(audio))
	 
# 	except sr.UnknownValueError:
# 	    print("Google Speech Recognition could not understand audio")
	 
# 	except sr.RequestError as e:
# 	    print("Could not request results from Google Speech Recognition service; {0}".format(e))