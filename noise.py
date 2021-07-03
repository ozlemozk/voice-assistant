import RPi.GPIO as GPIO
import time
import speech_recognition as sr  #konuşma tanıma kütüphanesi

# Raspberry Pi  kartı pin numaraları kullanımı
GPIO.setmode(GPIO.BOARD)
# GPIO output(çıkış)
GPIO.setup(7, GPIO.OUT) #ses anlamlandırıcı
GPIO.setup(8, GPIO.OUT)  #mikrofon



r = sr.Recognizer()
m = sr.Microphone()    


def listen():
    try:
        print("Sessizlik...")
        with m as source: #ses kaynağı olarak varsayılan mikrofonu kullan
            r.adjust_for_ambient_noise(source) # ortam gürültü seviyeleri için için 1 saniye dinleyin
       
        
        while True:
            with m as source:
                audio = r.listen(source)   #dinle
            print("Got it! Now to recognize it...")
            try:
                print("Lütfen konuşun!")
             # google konuşma tanıma sistemi ile tanıma işlemi
                value = r.recognize_google(audio) #algila

               # unicode  karekterleri çıktıları doğru biçimde yazdırmak özel işlemler
                if str is bytes:  #  (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                    return value
                else:  #  (Python 3+)
                    print("You said {}".format(value))
                    if value == "bedroom":
                        print("Yes, i can ;)")
                        GPIO.output(7,True)
                    if value == "bedroom":
                        print("Yes, i can ;)")
                        GPIO.output(7,False)
                    if value == "restroom":
                        print("Yes, i can ;)")
                        GPIO.output(8,True)
                    if value == "restroom":
                        print("Yes, i can ;)")
                        GPIO.output(8,False)
                    if value == "open everything":
                        print("Yes, i can ;)")
                        GPIO.output((7,8),True)
                    if value == "close everything":
                        print("Yes, i can ;)")
                        GPIO.output((7,8),False)
                            
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass