import pyttsx3
import speech_recognition as sr
from playsound import playsound
import random
import datetime
hour = datetime.datetime.now().strftime('%H:%M')
#print(hour)
date = datetime.date.today().strftime('%d/%B/%Y')
#print(date)
date = date.split('/')
#print(date)
import webbrowser as wb
import tensorflow as tf
import numpy as np
import librosa
import matplotlib.pyplot as plt
import seaborn as sns
from pygame import mixer
sns.set()
from modules import carrega_agenda, comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas
print(comandos)
print(respostas)

meu_nome = 'Mila'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

def search(frase):
    wb.get(chrome_path).open('https://www.google.com/search?q=' + frase)

#search('linguagem python')


def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    return frase


def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 85) # número de palavras por minuto
    engine.setProperty('volume', 1) # min: 0, max: 1
    engine.say(audio)
    engine.runAndWait()



while (True):
    mixer.init()
    mixer.music.load('n1.mp3')
    result = listen_microphone()
    if(result == meu_nome):
        mixer.music.play()





