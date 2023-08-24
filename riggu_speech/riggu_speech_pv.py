from pvrecorder import PvRecorder as pvr
import pvporcupine
# from playsound import playsound
import threading
import speech_recognition

import os
import openai
from gtts import gTTS
from  io import BytesIO
import uberduck
from time import sleep
from pygame import mixer
import whisper

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv("OPENAI_API_KEY")



class riggutalk():
    def __init__(self) -> None:
        ACCESS_KEY = "swuJ4g7WtF+fGGHw67F+rXIpc0vbP1c0DNuFzDo29eELccjlEXDT5Q==" #acess key for porcupine
        KEYWORD_FILE_PATH = r"riggu_speech/hey-Raghu_en_linux_v2_2_0.ppn"  #recognition model path

       
        uberduck_auth = ("pub_aesmuzashdbtevqqql", "pk_d4b7bfe6-33a3-41ce-bd70-6f1496a392ff")
        self.msg_hist = [{"role":"system","content":"you are a robot assistant named riggu. You have a physical body who can move around in the room"},
            {"role":"system","content":"""when ever asked to follow someone by the name of shibin, karthik ,aftaab  please reply as a json with keys person"""}]
        
        self.porcupine = pvporcupine.create(
        access_key=f'{ACCESS_KEY}',
        keyword_paths=[f'{KEYWORD_FILE_PATH}']
        )
        self.recoder = pvr(device_index=-1, frame_length=self.porcupine.frame_length)


        self.recognizer = speech_recognition.Recognizer()
        mixer.init()
    
    def speak(self,text):
        
        mp3_fp = BytesIO()
        tts = gTTS(text,lang = 'en')
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        mixer.music.load(mp3_fp,"mp3")
        mixer.music.play()  
        while(mixer.music.get_busy()):
             sleep(0.1)
        
        

        
    def getchatresponse(self,prompt):
        try:
            self.msg_hist.append({"role":"user","content":prompt})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = self.msg_hist,
                max_tokens = 120)
            answer = response['choices'][0]['message']['content']
            self.msg_hist.append({"role":"assistant","content":answer})
        except Exception as e:
            print(e)

        return answer
    
    def start_listen(self):
        self.thread = threading.Thread(target=self.listen)
        self.thread.start()
    def stop_listen(self):
        pass

    def listen(self):
        self.recoder.start()
        while True:
                
                print("listening for wake word")
                keyword_index = self.porcupine.process(self.recoder.read())            
                print("didnt detect wake word")
                if keyword_index >= 0:
                    self.speak("hi how can i help you")
                    print("detected wake word")
                    while True:
                        try:
                            with speech_recognition.Microphone() as mic:
                                text= ""
                                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                                print("one")
                                audio = self.recognizer.listen(mic)
                                print("two")
                                text = self.recognizer.recognize_whisper(audio)
                                print("waiting for wake word")
                                text = text.lower()
                                print(text)
                                
                                if(text==""):
                                    continue

                                rsp = self.getchatresponse(text)
                                print(rsp)
                                self.speak(rsp)

                                if ("bye riggu" in text):
                                    self.speak("bye bye")
                                    continue
                                
                        except:
                            print("stop listening")
                            continue


    
rt = riggutalk()
# rt.speak("hello i am riggu")
rt.start_listen()
