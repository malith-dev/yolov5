import serial

# Define the serial port and baud rate
serial_port = 'COM6'  # Replace with the correct COM port on your PC
baud_rate = 9600

def get_speed():
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        try:
            while True:
                # Read a line of data from the GPS module
                line = ser.readline().decode('utf-8').strip()

                # Check if the line starts with "$GPRMC" (recommended minimum GPS data)
                if line.startswith("$GPRMC"):
                    # Process the line for GPS data
                    parts = line.split(',')
                    if len(parts) >= 7:
                        speed_knots = parts[7]
                        try:
                            speed_float = float(speed_knots)  # Try to convert to float
                            speed_kmph = speed_float * 1.852
                            print(f"{speed_kmph} kmph")
                            return speed_kmph
                        
                        except ValueError:
                            print(f"Invalid speed data: {speed_knots}")
                        
                
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    get_speed()



