# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:41:25 2021

@author: iubeda
"""
from gtts import gTTS
from playsound import playsound
from os import remove
import speech_recognition as sr
import pyttsx3
import requests
import wikipedia
import time
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
#from googlesearch import search
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


num_page = 3
wikipedia.set_lang("es")  
r = sr.Recognizer()
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.db'
)
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.spanish.conversations")

s = gTTS("Hola mundo soy atena", lang='es', slow=False)
remove('hola.mp3')
s.save('hola.mp3')
playsound('hola.mp3')

def SpeakText(command):
    # Inicializamos el proceso de salida de texto a voz
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# En este ciclo esperaremos la entrada de audio a convertir
while (1):

    # Añadimos un try-except en caso de surgir errores
    try:

        # Usamos el microfono para recuperar voz
        with sr.Microphone() as source2:
            # Obtenemos el audio
            print("Escuchando.......")
            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)
            # Ahora, usamos speech_recognition para convertir el audio a texto
            MyText = r.recognize_google(audio2, language='es-ES')
            MyText = MyText.lower()
            print("Intentaste decir: " + MyText)
            # Podemos convertir el texto a voz de nueva cuenta.
            #SpeakText(MyText)
            s = gTTS( MyText, lang='es', slow=False)
            remove('hola.mp3')
            s.save('hola.mp3')
            playsound('hola.mp3')
            print(MyText)
            

            if MyText == 'hola atena' or MyText == 'hola nena':
               s = gTTS( 'hola , soy atena, soy un asistente virtual, creado por Israel ubeda ,con fecha 20 de septiembre 2021 , creada en lenguaje python', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               


            if MyText == 'noticias' or MyText == 'nena noticias':
               s = gTTS( 'Procesando solicitud de noticias', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3') 
               url_google_news ='https://news.google.cl/rss'
               cliente = urlopen(url_google_news)
               contenido_xml = cliente.read()
               cliente.close()
               pagina = soup(contenido_xml,'html.parser')
               items = pagina.findAll('item')
               for item in items:
                   print(item.title.text)
                   s = gTTS( item.title.text, lang='es', slow=False)
                   remove('hola.mp3')
                   s.save('hola.mp3')
                   playsound('hola.mp3')
                   print(item.link.text)
                   #print(item.pubDate.text)
                   
                   print('=' * 70)
               
               
            if MyText == 'indicadores' or MyText == 'nena indicadores':
               s = gTTS( 'Procesando indicadores', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               url ='https://mindicador.cl/api'
               response = requests.get(url)
               print(response.text)
               s = gTTS( response.url, lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               if response.status_code == 200:
                   response_json = response.json()
                   bitcoin = response_json['bitcoin']
                   print(bitcoin)
                   
            if MyText == 'wikipedia' or MyText == 'nena wikipedia':
               s = gTTS( 'que deseas buscar en Wikipedia', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               r.adjust_for_ambient_noise(source2, duration=0.5)
               time.sleep(2)
               audio2 = r.listen(source2)
               MyText = r.recognize_google(audio2, language='es-ES')
               MyText = MyText.lower()
               print("buscare entonces en wikipedia : " + MyText)
               s = gTTS( 'buscare entonces en wikipedia ' + MyText , lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               print(wikipedia.summary( MyText,sentences=4))
               s = gTTS(wikipedia.summary( MyText,sentences=4) , lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')


            if MyText == 'google'or MyText == 'nena google':
               s = gTTS( 'que deseas buscar en google', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               r.adjust_for_ambient_noise(source2, duration=0.5)
               time.sleep(2)
               audio2 = r.listen(source2)
               MyText = r.recognize_google(audio2, language='es-ES')
               MyText = MyText.lower()
               print("buscare entonces en google : " + MyText)
               s = gTTS( 'buscare entonces en google ' + MyText , lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')
               
               search_results = search(MyText, tld='com', lang='es', num=num_page, start=0 , stop=num_page, pause=2.0)
               for result in search_results:
                   print(result)                
                
            if MyText == 'charlar'or MyText == 'nena charlar':
               s = gTTS( 'ok, charlemos', lang='es', slow=False)
               remove('hola.mp3')
               s.save('hola.mp3')
               playsound('hola.mp3')               
               while True:
                   try:
                       r.adjust_for_ambient_noise(source2, duration=0.5)
                       time.sleep(2)
                       audio2 = r.listen(source2)
                       MyText = r.recognize_google(audio2, language='es-ES')
                       MyText = MyText.lower()
                       user_input = MyText
                       print(MyText)

                       bot_response = bot.get_response(user_input)
                       s = gTTS( str(bot_response), lang='es', slow=False)
                       remove('hola.mp3')
                       s.save('hola.mp3')
                       playsound('hola.mp3')
                       print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
                   except (KeyboardInterrupt, EOFError, SystemExit):
                      break
                  
                   except sr.UnknownValueError:
                      print("no entendio o no escucho....")
                
    except sr.RequestError as e:
        print("No existen resultados; {0}".format(e))

    except sr.UnknownValueError:
        print("Error desconocido")
 
         # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
        
s = gTTS("Adios", lang='es', slow=False)
remove('hola.mp3')
s.save('hola.mp3')
playsound('hola.mp3')
