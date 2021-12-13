import speech_recognition as sr

def callback(recognizer, audio):
    print('Speech Heard!')
    try:
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        parsedAudio = recognizer.recognize_google(audio)
        print(parsedAudio)
        with open('voice.txt', 'w') as audioFile:
            audioFile.write(parsedAudio)
    except sr.UnknownValueError:
        pass
        #print("Google could not understand audio")
    except sr.RequestError as e:
        pass
        #print("Could not request results from Google Speech Recognition service; {0}".format(e))

class AudioParser:

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.r.non_speaking_duration = 0.01
        self.r.pause_threshold = 0.01
        with self.m as source:
            print('Shh!')
            self.r.adjust_for_ambient_noise(source, duration=3)
    
    def listenBackground(self):
        with self.m as source:
            pass
        self.stop_listening = self.r.listen_in_background(source, callback, phrase_time_limit=5)

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
