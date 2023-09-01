import serial
import time

# Set the serial port and baud rate (adjust as needed)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def send_at_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    response = ser.read(ser.in_waiting).decode()
    return response

try:
    # Initialize the SIM800L module
    send_at_command('AT')
    print(send_at_command('ATE0'))  # Disable command echoing
    print(send_at_command('AT+CMGF=1'))  # Set SMS text mode
    print(send_at_command('AT+CNMI=2,2,0,0,0'))  # Disable SMS notifications

    # Send an SMS
    recipient_number = '+1234567890'  # Replace with the recipient's phone number
    message = 'Hello, this is a test message!'
    print(send_at_command('AT+CMGS="{}"'.format(recipient_number)))
    print(send_at_command(message))
    ser.write(chr(26).encode())  # Send Ctrl+Z to indicate the end of the message
    time.sleep(2)
    print("Message sent!")

except KeyboardInterrupt:
    ser.close()  # Close the serial port on Ctrl+C exit

