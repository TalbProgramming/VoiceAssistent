import pyttsx3
import speech_recognition as sr


def read_string(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


file_location = "recording.wav"
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)  # starts and stops recording by defualt silence time


try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    generated_text = r.recognize_google(audio)

    read_string(generated_text)

    print(f"The program thinks you said: \n>>>\t\t {generated_text}")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

