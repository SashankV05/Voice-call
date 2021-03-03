import os
import socket
import pyaudio
import wave
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 400
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []
try:
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    HOST = '192.168.1.6'
    PORT = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)

    i = 1
    while data != '':
        stream.write(data)
        data = conn.recv(1024)
        i = i + 1
        print(i)
        frames.append(data)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.close()
except:

    print('restarting Server')
    print("the below exeption occured "+" \n " + str(Exception))
    time.sleep(2)
    os.startfile('server.py')
    print('restarted successfully')
    conn.close()
    time.sleep(2)
    quit()
