import serial
from time import sleep

# Replace '/dev/ttyS0' with the actual serial port your USB-to-Serial adapter is connected to
ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)

while True:
    if ser:
        response = ser.readline()
        # message = input("Enter a message: ")
        # ser.write(message.encode("utf-8"))
        # if ser.in_waiting > 0:
        #     print("in waiting ..")
        #     response += ser.readline()

        received_data = response.decode("utf-8")
        print("Received:", received_data)
        sleep(0.5)
