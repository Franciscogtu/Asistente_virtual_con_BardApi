#!/usr/bin/env python
# coding: utf-8

# ASISTENTE VIRTUAL USANDO BARDAPI

# In[45]:


#!pip install sounddevice numpy
#!pip install pyttsx3


# In[84]:


import sounddevice as sd
import numpy as np
import wave
from IPython.display import Audio
import pyttsx3

engine = pyttsx3.init() # object creation
engine.say("dime lo que necesitas")
engine.runAndWait()
engine.stop()



# Configura los parámetros de grabación
sample_rate = 44100  # Tasa de muestreo en Hz
duration = 7  # Duración de la grabación en segundos
output_file = "grabacion.wav"  # Nombre del archivo de salida

# Graba audio desde el micrófono
print("Grabando audio... Presiona Ctrl+C para detener.")
audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
sd.wait()  # Espera a que termine la grabación

# Guarda la grabación en un archivo WAV
with wave.open(output_file, "wb") as wf:
    wf.setnchannels(1)  # Un canal (mono)
    wf.setsampwidth(2)  # 16 bits por muestra
    wf.setframerate(sample_rate)
    wf.writeframes(audio.tobytes())

print(f"Grabación guardada como '{output_file}'")

# Reproduce el audio grabado
print("Reproduciendo audio...")
Audio(output_file)
print(output_file)


# In[85]:


from IPython.display import Audio

# Especifica la ruta del archivo MP3 en tu sistema de archivos local o una URL en línea
ruta_mp3 = 'grabacion.wav'  # Cambia 'tu_archivo.mp3' al nombre y ruta de tu archivo MP3

# Reproduce el archivo MP3
Audio(ruta_mp3)


# In[82]:



#!pip install SpeechRecognition


# In[89]:


import speech_recognition as sr

# Nombre del archivo de audio grabado
audio_file = "grabacion.wav"

# Crea un objeto Recognizer
recognizer = sr.Recognizer()

# Abre el archivo de audio
with sr.AudioFile(audio_file) as source:
    #print(f"Transcribiendo audio de '{audio_file}'...")

    # Escucha el audio desde el archivo
    audio = recognizer.record(source)

    try:
        # Intenta reconocer el texto del audio
        text = recognizer.recognize_google(audio,language='es-CO')  # Puedes usar otros motores de reconocimiento también
        print("Texto reconocido:")
        print(text)

    except sr.UnknownValueError:
        print("No se pudo entender lo que se dijo en el audio")

    except sr.RequestError as e:
        print(f"Error al solicitar el servicio de reconocimiento: {e}")


# In[91]:


from bardapi import BardCookies
  
    
#PARA TENER LAS KEYS DEBES LOGEAR EN LA APP  DE API , A CONTINUACION F12 (buscar en herramientas de creacion pestaña Aplicacion), a continuacion buscar
#en almacenamiento las cookies de https://bard.google.com donde encontraras   "__Secure-1PSID" y  "__Secure-1PSIDTS" que los reemplazas
cookie_dict = {
    "__Secure-1PSID": "xxxx",
    "__Secure-1PSIDTS": "xxxx",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)
respuesta= bard.get_answer(text)
salida = respuesta["content"]
print(salida)

#print(bard.get_answer(text))


# In[92]:


import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # speaking rate
#print (rate)                        
engine.setProperty('rate', 240)     


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                         
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say(salida)
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(salida, 'test.mp3')
engine.runAndWait()


# In[93]:


from IPython.display import Audio

# Especifica la ruta del archivo MP3 en tu sistema de archivos local o una URL en línea
ruta_audio = 'test.mp3'  # Cambia 'tu_archivo.mp3' al nombre y ruta de tu archivo MP3

# Reproduce el archivo MP3
Audio(ruta_audio)


# In[ ]:




