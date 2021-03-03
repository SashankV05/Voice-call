import os
import socket
import time

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 400

HOST = '192.168.1.8'
PORT = 8080
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((HOST, PORT))

 p = pyaudio.PyAudio()

 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

 print("*recording")

 frames = []

 for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
  data  = stream.read(CHUNK)
  frames.append(data)
  s.sendall(data)

 print("*done recording")

 stream.stop_stream()
 stream.close()
 p.terminate()
 s.close()

 print("*closed")
except:
    print('connection ended unexpectedly')
    time.sleep(0.6)
    try:
     print('trying to reconnect')

     time.sleep(1.212312)
     os.startfile('client.py')

     quit()
    except:
        print('unable to connect')