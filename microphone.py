from speech_recognition import Microphone , Recognizer , UnknownValueError , RequestError

recog = Recognizer()
mic= Microphone()

with mic :
    recog.adjust_for_ambient_noise(mic, duration=5)
    print('talk:')
    audio = recog.record(mic,3)
try:
    recognized=recog.recognize_google(audio)
    print('you said',recognized)
except RequestError as exp:
    print(exp)
except UnknownValueError:
    print('nothing')


