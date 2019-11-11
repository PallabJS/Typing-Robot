#----------------------------------------------------------------------------------------------
# TestTime = 7.6

import speech_recognition as sr
import time
import RPi.GPIO as GPIO

sm1 = 14
sm2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sm1, GPIO.OUT)
GPIO.setup(sm2, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

"""---------------------------------------------------------------------

    recognize_bing()- Microsoft Bing Speech
    recognize_google()- Google Web Speech API
    recognize_google_cloud()- Google Cloud Speech
    recognize_houndify()- Houndify
    recognize_ibm()- IBM Speech to Text
    recognize_sphinx- CMU Sphinx
    recognize_wit()- Wit.ai
"""
    
#-----------------------------------------------------------------------------------------------
# MIC Function
#-----------------------------------------------------------------------------------------------
#with open("api-key.json") as f:
#    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()


def main():
    r = sr.Recognizer()
    while(True):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak Now: ")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                f=open("text.txt","w")
                f.write(text)
                f.close()
                dataread()
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
            except sr.RequestError as e: 
                print("Try again, Google Servie Busy!".format(e))
                print("Done")

def dataread():
    with open("text.txt") as p:
        ch = 'a'
        while ch:
            ch = p.read(1)
            print(ch)
            motor(ch)

def motor(ch):
    if ch == 'a':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(6.2)
        q.ChangeDutyCycle(4.6)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch == 'b':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.1)
        q.ChangeDutyCycle(4.3)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

     if ch == 'c':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.4)
        q.ChangeDutyCycle(4.5)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)
        
    if ch == 'd':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.8)
        q.ChangeDutyCycle(4.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='e':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(6)
        q.ChangeDutyCycle(4.2)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)


    if ch =='f':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.6)
        q.ChangeDutyCycle(4.3)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='g':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.4)
        q.ChangeDutyCycle(4.2)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

        
    if ch =='h':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.3)
        q.ChangeDutyCycle(4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='i':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.4)
        q.ChangeDutyCycle(3.7)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='j':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.3)
        q.ChangeDutyCycle(3.9)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='l':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.1)
        q.ChangeDutyCycle(3.6)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='k':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.1)
        q.ChangeDutyCycle(3.8)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

        
    if ch =='m':    
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5)
        q.ChangeDutyCycle(4.1)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)
        
    if ch =='o':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.3)
        q.ChangeDutyCycle(3.5)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='n':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5)
        q.ChangeDutyCycle(4.1)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='o':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.3)
        q.ChangeDutyCycle(3.5)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='p':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.3)
        q.ChangeDutyCycle(3.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='q':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(6.3)
        q.ChangeDutyCycle(4.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='r':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.8)
        q.ChangeDutyCycle(4.2)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18,GPIO.HIGH)

    if ch =='s':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(6)
        q.ChangeDutyCycle(4.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='t':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.7)
        q.ChangeDutyCycle(4.1)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='u':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.5)
        q.ChangeDutyCycle(3.8)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='v':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.2)
        q.ChangeDutyCycle(4.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='w':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(6.2)
        q.ChangeDutyCycle(4.4)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='x':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.6)
        q.ChangeDutyCycle(4.6)
        time.sleep(1.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05 )
        GPIO.output(18,GPIO.HIGH)

    if ch =='y':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.6)
        q.ChangeDutyCycle(3.9)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18,GPIO.HIGH)

    if ch =='z':
        p = GPIO.PWM(sm1, 50)
        q = GPIO.PWM(sm2, 50)
        p.start(2.5)
        q.start(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.8)
        q.ChangeDutyCycle(4.7)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18,GPIO.HIGH)
        
main()







