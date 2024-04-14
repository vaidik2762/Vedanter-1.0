import androidhelper
import time
from datetime import date
android=androidhelper.Android()
def speak(string):
    android.ttsSpeak(str(string))

def convertre(string):
    index1=string.index("result=")
    index1 += 7
    ogstr = ""
    while(True):
        checkstr = (string[index1] + string[(index1)+1] + string[(index1)+2] ) 
        if checkstr == ", e" :
            break 
        ogstr += string[index1]
        index1 += 1
     
    #print("Result :", string)
    #print("OG str :" ,ogstr)
    return ogstr

def lisn():
    result = str(android.recognizeSpeech())
    return str(convertre(result))
    
def greet():
    speak("Jay Mataji I am V.M sir's Vedantar")
    time.sleep(1)

speak("Lisning...")
time.sleep(1)
mainstr=(lisn()).lower()

print("Start")

var = 0
try :
    while(True) :
        print(f"Its back in loop {var} time")    
        if "hello vedantar" in mainstr:
            speak("Thank you for calling by my name ")
            greet()
            time.sleep(4)
            speak("is any thing else ")
            mainstr = (lisn()).lower()
        elif "hello" in mainstr:
            greet()
            time.sleep(4)
            speak("is any thing else") 
            mainstr=(lisn()).lower()
        elif "something about you" in mainstr:
            print("\tIt working")
            speak("I am created by V.M sir. my scalability is end less") 
            time.sleep(4)
            speak("is any thing else")
            mainstr=(lisn()).lower()
        elif "call" in mainstr:
            print("\tdialing....    ") 
            speak("ok than what is the number")
            time.sleep(2)
            num=(lisn()).lower()
            phonenum = num.replace(" ","")
            print("\tThis is the number :",phonenum)
            android.phoneDialNumber(phonenum)
            break
        elif  "send a mail"  in  mainstr:
             speak("For sending a mail I need mail ID please enter a mail ID by typing")
             time.sleep(4)
             mid=input("Enter a mail id :")
             print("\tMail Ditals")
             speak("Ok than what is the subject")
             time.sleep(2)
             subject=(lisn()).lower()
             speak("and what is the body")
             time.sleep(2)
             body=(lisn()).lower()
             android.sendEmail(mid,subject,body)
             speak("sending")
             android.makeToast("Sending....")             
             print("\tMail id :",mid,"\n\tSubject :",subject,"\n\tBody :",body)             
             break
        elif "bluetooth name" in mainstr :
            speak("Cheking ")
            android.makeToast("Cheking...")
            name = str(android.bluetoothGetLocalName())
            print("\tdivice name :",end="")
            result = convertre(name)
            print(result)
            speak(result)
            time.sleep(2)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
        elif "bluetooth connected" in mainstr :
            print("\tIs conected :",end="")
            re=str(android.checkBluetoothState())
            result=convertre(re)
            print(result)
            if "True" in result:
                speak("Yes, you are Bluetooth device is connected")
            else :
                speak("No your bluetooth is not connected")                
            time.sleep(2)
            speak("is any thing else")
            time.sleep(1)
            mainstr=(lisn()).lower()
        elif "turn on bluetooth" in mainstr :
            speak("Turning on")
            android.makeToast("Turning on bluetooth")
            print("\tOn bluetooth")
            re=str(android.toggleBluetoothState(True))
            result= convertre(re)
            print("\t\tResult :" ,result)
            time.sleep(1)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "turn off bluetooth" in mainstr :
            speak("Turning of")
            android.makeToast("Turning off bluetooth")
            print("\toff bluetooth")
            re=str(android.toggleBluetoothState(False))
            result=convertre(re)
            print("\t\tResult :" ,result)
            time.sleep(1)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()

        elif "bluetooth on" in mainstr :
            speak("checking..")
            android.makeToast("Chekcing.....")
            print("\tIs bluetooth on ?")
            re=str(android.checkBluetoothState())
            result = convertre(re)
            print("\t\t Result :",result)
            if "True" in result:
                speak("Yes, you are Bluetooth is on")
            else :
                speak("No your bluetooth is off")                
            time.sleep(4)
            speak("is any thing else")
            time.sleep(1)
            mainstr=(lisn()).lower()
                    
        elif "turn on wi-fi" in mainstr :
            speak("Turning on")
            android.makeToast("Turning on Wifi")
            print("\tOn wifi")
            re=str(android.toggleWifiState(True))
            result=convertre(re)
            print("\t\tResult :" ,result)
            time.sleep(1)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "turn off wi-fi" in mainstr :
            speak("Turning off")
            android.makeToast("Turning off Wifi")
            print("\tOn wifi")
            re=str(android.toggleWifiState(False))
            result=convertre(re)
            print("\t\tResult :" ,result)
            time.sleep(1)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "in my clipboard" in mainstr :
            speak("checking")
            android.makeToast("Checking clipbord")
            a = android.getClipboard()
            re=str(a)
            result = convertre(re)
            print("\t In clipbord")
            print("\t\t Default :",a)
            print("\t\t result :",result)
            speak(result)
            speak("is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "my media volume" in mainstr :
            print("\tCheck media volume")
            re=str(android.getMediaVolume())
            result = convertre(re)
            print("\t\t Result :",result)
            speak(result)
            speak("Is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif ("my network operator" in mainstr) or ("my network provider" in mainstr):
            print("\tCheck network operator")
            re=str(android.getNetworkOperator())
            result = convertre(re)
            print("\t\t Result :",result)
            speak("your network operator is")
            speak(result)
            time.sleep(3)            
            speak("Is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "phone ring volume" in mainstr :
            print("\tRing Volume")
            re=str(android.getRingerVolume())
            result = convertre(re)
            print("\t\tResult :",result)
            speak("your volume is")
            time.sleep(1)
            speak(result)
            time.sleep(2)
            speak("Is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "screen brightness" in mainstr :
            print("\tScreen Brightness")
            re=str(android.getScreenBrightness())
            result = convertre(re)
            print("\t\tResult :",result)
            speak("your brigthness is")
            time.sleep(1)
            speak(result)
            time.sleep(2)
            speak("Is any thing else")
            time.sleep(1)
            mainstr = (lisn()).lower()
            
        elif "screen timeout" in mainstr :
            print("\tTime out")
            re=str(android.getScreenTimeout())
            result = convertre(re)
            print("\t\tResult : ",result)
            speak("your screen timeout time is")
            time.sleep(2)
            speak(result)
            time.sleep(1)
            speak("mili second")
            time.sleep(1)
            speak("is any thing else")
            time.sleep(2)
            mainstr = (lisn()).lower()             
                                    
        elif "sim state" in mainstr :
            print("\tSim state ")
            re = str(android.getSimState())
            result = convertre(re)
            print("\t\tResult :",result)
            speak("Your sim is in")
            speak(result)
            speak("state")
            speak("Is any thing else")
            time.sleep(4)
            mainstr = (lisn()).lower()
            
        elif "set my volume" in mainstr :
            print("\tSet volume :")
            speak("ok then which level")
            time.sleep(1)
            level=int(input("\t\tEnter level :"))
            re=str(android.setMediaVolume(level))
            result=convertre(re)
            print("\t\tResult :",result)
            speak("seted successfully")
            time.sleep(1)
            speak("is any thing else")
            time.sleep(2)
            mainstr = (lisn()).lower()
            
        elif "where is my home" in mainstr :
            print("\tMap ")
            serch = "Home"
            re=str(android.viewMap(serch))
            result=convertre(re)
            print("\t\t Result :",result)
            break
            
        elif "search on map" in mainstr :
            print("\tMap ")
            speak("ok than what do you search")
            time.sleep(2)
            serch = (lisn()).lower()
            re=str(android.viewMap(serch))
            result=convertre(re)
            print("\t\t Result :",result)
            break
            
        elif "what is today date" in mainstr :
            print("\tDate :")
            today=str(date.today())
            speak(today)
            print("\t\t Today date :",today)
            time.sleep(1)
            speak("is any thing else")
            time.sleep(2)
            mainstr = (lisn()).lower()
            
        elif "what is current time" in mainstr :
            print("\tTime :")
            tim = str(time.strftime("%l : %M %p"))
            speak(tim)
            time.sleep(1)
            print("\t\tTime : ", tim)
            speak("is any thing else")
            time.sleep(2)
            mainstr = (lisn()).lower()            
                                                                                                                                                                  
        elif "no" in mainstr :
            android.makeToast("Closeing...")
            speak("closeing..")
            break
            
        elif "stop" in mainstr :
            android.makeToast("Closeing....")
            speak("closeing..")
            break

        else :
            android.makeToast("Closeing...")
            speak("sorry I did't understand")            
            break          
        var += 1
except :
    speak("Something wrong") 
    
print(mainstr)
print("complet")