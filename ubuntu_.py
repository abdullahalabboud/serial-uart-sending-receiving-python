import serial

# Replace '/dev/ttyUSB0' with the actual serial port your USB-to-Serial adapter is connected to
ser = serial.Serial("/dev/ttyUSB1", 115200, timeout=1)

while True:
    received_data = ser.readline().decode("utf-8")
    print("Received:", received_data)

    message = input("Enter a message: ")
    ser.write(message.encode("utf-8"))
