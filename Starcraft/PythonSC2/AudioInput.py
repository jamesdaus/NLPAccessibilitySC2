import speech_recognition as sr

# obtain audio from the microphone

class AudioParser:

    def __init__(self):
        with open('log.txt', 'w') as logFile:
            pass
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)

    def getAudio(self):
        print("Say something!")
        with sr.Microphone() as source:
            input('Press enter to begin command')
            audio = self.r.listen(source, timeout=15, phrase_time_limit=3)
        print("Heard you!")

        try:
            parsedAudio = self.r.recognize_google(audio)
            print("Google thinks you said " + parsedAudio)
            with open('log.txt', 'a') as logFile:
                logFile.write('\nParsed Audio: {}\n'.format(parsedAudio))
            return parsedAudio
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
'''
try:
    parsedAudio = r.recognize_sphinx(audio)
    with open('voice.txt', 'w') as voiceFile:
        voiceFile.write(parsedAudio)
    print("Sphinx thinks you said " + parsedAudio)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
'''