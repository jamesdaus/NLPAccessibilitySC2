import speech_recognition as sr

def callback(recognizer, audio):
    print('Speech Heard!')
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        parsedAudio = recognizer.recognize_google(audio)
        with open('voice.txt', 'w') as audioFile:
            audioFile.write(parsedAudio)
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

class AudioParser:

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.r.pause_threshold = .5
        with self.m as source:
            print('Shh!')
            self.r.adjust_for_ambient_noise(source, duration=5)

    def callback(self, recognizer, audio):
        try:
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            parsedAudio = self.r.recognize_google(audio)
            with open('log.txt', 'a') as logFile:
                logFile.write('\nParsed Audio: {}\n'.format(parsedAudio))
            return parsedAudio
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    def listenBackground(self):
        with self.m as source:
            pass
        self.stop_listening = self.r.listen_in_background(source, callback)

    def stopListening(self):
        self.stop_listening(wait_for_stop=False)

def main():
    parser = AudioParser()
    parser.listenBackground()
    input('Press Enter When Complete')
    parser.stopListening
    input('Goodbye')

if __name__ == "__main__":
    main()
