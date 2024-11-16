from pvrecorder import PvRecorder as pvr
import pvporcupine
# from playsound import playsound
import threading
import speech_recognition
import multiprocessing
import os
from gtts import gTTS
from  io import BytesIO
from time import sleep
from pygame import mixer
import sys
import google.generativeai as genai

# openai.api_key = os.getenv("OPENAI_API_KEY")

genai_key = '.........................'


class riggutalk():
    def __init__(self) -> None:

        self.stop_flag = False
        ACCESS_KEY = "..........................." #acess key for porcupine
        KEYWORD_FILE_PATH = r"/home/aftaab/Documents/riggu_git/Riggu-2023/Riggu_GUI/riggu_speech/hey-Raghu_en_linux_v2_2_0.ppn"  #recognition model path
    #    "/ws/Riggu_GUI/riggu_speech/hey-Raghu_en_linux_v2_2_0.ppn"
        self.msg_hist = [{"role":"system","content":"you are a robot assistant named riggu. You have a physical body who can move around in the room"},
            {"role":"system","content":"""when ever asked to follow someone by the name of shibin, karthik ,aftaab  please reply as a json with keys person"""}]
        
        self.porcupine = pvporcupine.create(
        access_key=f'{ACCESS_KEY}',
        keyword_paths=[f'{KEYWORD_FILE_PATH}']
        )
        self.recoder = pvr(device_index=-1, frame_length=self.porcupine.frame_length)


        self.recognizer = speech_recognition.Recognizer()
        genai.configure(api_key='AIzaSyBR-osMaWgALJehm2mUfElFsfaSvbyEtAA')
        model = genai.GenerativeModel("gemini-pro")
        self.chat = model.start_chat()
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
        
    def speak_async(self,words):
        t = threading.Thread(target=self.speak,args=(words,))
        t.start()
        t.join(10)


        
    def getchatresponse(self,prompt):
        # try:
        #     self.msg_hist.append({"role":"user","content":prompt})
        #     response = openai.ChatCompletion.create(
        #         model = "gpt-3.5-turbo",
        #         messages = self.msg_hist,
        #         max_tokens = 120)
        #     answer = response['choices'][0]['message']['content']
        #     self.msg_hist.append({"role":"assistant","content":answer})
        # except Exception as e:
        #     print(e)
        response = self.chat.send_message(prompt)
        answer = response.text
        return answer
    
    def start_listen(self):
        self.thread = threading.Thread(target=self.listen)
        self.thread.start()

    def stop_listen(self):
        self.stop_flag = True
        # self.thread.join()

        pass

    def listen(self):
        self.recoder.start()
        while True:                
                print("listening for wake word")
                keyword_index = self.porcupine.process(self.recoder.read()) 
                if(self.stop_flag == True):
                        # self.recoder.delete()
                        # self.thread.join()
                        sys.exit()
                
                # print("didnt detect wake word")
                if keyword_index >= 0:
                    self.speak("hi how can i help you")
                    # print("detected wake word")
                    while True:
                        try:
                            with speech_recognition.Microphone() as mic:
                                text= ""
                                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                                print("one")
                                audio = self.recognizer.listen(mic)
                                print("two")
                                text = self.recognizer.recognize_whisper(audio)
                                # print("waiting for wake word")
                                text = text.lower()
                                print(text)

                                if ("bye, go to sleep." in text):
                                    self.speak("bye bye")
                                    break   

                                if(text==""):
                                    continue
                                if(self.stop_flag == True):
                                    # self.recoder.delete()
                                    # self.thread.join()
                                    sys.exit()
                                rsp = self.getchatresponse(text)
                                print(rsp)
                                self.speak(rsp)
       
                        except:
                            print("stop listening")
                            continue
        


    
rt = riggutalk()
rt.speak("hello i am riggu")
rt.start_listen()
