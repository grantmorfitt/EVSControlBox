#Author: Grant Morfitt

from gpiozero import LED, Button
import time
import threading
import socket

#-----------------------------Variable Dec--------------------------------------
setupCompleted = False
connected = False

buttonAActive = False
buttonBActive = False
buttonCActive = False
buttonDActive = False

messageSentLED = LED(5)
led_connectionStatus = LED(6)

buttonA = Button(10)
buttonB = Button(22)
buttonC = Button(17)
buttonD = Button(27)

UDP_IP = "192.168.72.111"
UDP_PORT = 5007

#-------------------------------Function Dec------------------------------------ 
def ToggleButtonA():
    global buttonAActive
    
    messageSentLED.toggle()     
    buttonAActive = not buttonAActive
    print(f"Toggled A, new value is {buttonAActive}")
    time.sleep(0.5)
    messageSentLED.toggle()

def ToggleButtonB():
    global buttonBActive
    
    messageSentLED.toggle()     
    buttonBActive = not buttonBActive
    print(f"Toggled B, new value is {buttonBActive}")
    time.sleep(0.5)
    messageSentLED.toggle()
    
def ToggleButtonC():
    global buttonCActive
    
    messageSentLED.toggle()     
    buttonCActive = not buttonCActive
    print(f"Toggled C, new value is {buttonCActive}")
    time.sleep(0.5)
    messageSentLED.toggle()
    
def ToggleButtonD():
    global buttonDActive
    
    messageSentLED.toggle()     
    buttonDActive = not buttonDActive
    print(f"Toggled D, new value is {buttonDActive}")
    time.sleep(0.5)
    messageSentLED.toggle()
    
    
def SendUDP():
    global buttonDActive,buttonCActive,buttonBActive, buttonAActive, connected
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    while True:
        try:
            led_connectionStatus.on()
            val1 = 0b0
            val2 = 0b0
            val3 = 0b0
            val4 = 0b0
            
            if (buttonAActive == True):
                val1 = 1
            if (buttonBActive == True):
                val2 = 1
            if (buttonCActive == True):
                val3 = 1
            if (buttonDActive == True):
                val4 = 1
                
            topic_msg = f"{val1}{val2}{val3}{val4}"
            
            sock.sendto(topic_msg.encode(), (UDP_IP, UDP_PORT))

            print(f"Publishing {topic_msg} to {UDP_IP}:{UDP_PORT}")
            time.sleep(1.0)
        except:
            connected = False
            print("Sending error occured")
            led_connectionStatus.off()
         
        
    
def BlinkStatusLed():
    
    for t in range(0,3):
        led_connectionStatus.toggle()
        time.sleep(1.0)

def main():
  print("Initializing")
  
  BlinkStatusLed() #Blink status LED so we know the program has loaded up
  connected = True
  print("Set up complete")
  
  send_thread = threading.Thread(target=SendUDP) #Start sending the UDP messages in another thread
  send_thread.start()
  
  
  buttonA.when_pressed = ToggleButtonA
  buttonB.when_pressed = ToggleButtonB
  buttonC.when_pressed = ToggleButtonC
  buttonD.when_pressed = ToggleButtonD   
if __name__ == '__main__':
  main()
    
    
     
        

        




