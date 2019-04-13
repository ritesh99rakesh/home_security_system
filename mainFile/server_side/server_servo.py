import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.4.1", 5008))
server_socket.listen(1)
import os


import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep      # Importing sleep from time library to add delay in code
    # Make all GPIO pins LOW
    
def RUN_SERVO_1():
    servo_pin = 3     # Initializing the GPIO 21 for servo motor

    GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
    GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin

    p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
    p.start(2.5)                    

                    # Loop will run forever
    p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
    sleep(1)                # Delay of 1 sec
#    p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
#    sleep(1)                
    p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
    sleep(1)

    # If Keyborad Interrupt (CTRL+C) is pressed

    GPIO.cleanup()          

def RUN_SERVO_2():
    servo_pin = 3     # Initializing the GPIO 21 for servo motor

    GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
    GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin

    p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
    p.start(2.5)                    

                    # Loop will run forever
    
    p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
    sleep(1)# Delay of 1 sec
    p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
    sleep(1)
#    p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
#    sleep(1)                
    

    # If Keyborad Interrupt (CTRL+C) is pressed

    GPIO.cleanup() 
while (1):
    client_socket, address = server_socket.accept()
    print ("Conencted to - ",address,"\n")
    choice = client_socket.recv(1024)
    if(len(choice) == 0):
        continue
    print(choice)
    choice = int(choice)
    if(choice == 0):
        print("Door Open")
        RUN_SERVO_1()
    else:
        print("Door Close")
        RUN_SERVO_2()
        
    client_socket.close()
    
    
    


        
