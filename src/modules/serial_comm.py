# 시리얼 통신 기능
import serial.tools.list_ports

class BaudRate:
    BAUD_9600 = 9600
    BAUD_19200 = 19200
    BAUD_38400 = 38400
    BAUD_57600 = 57600
    BAUD_115200 = 115200
    BAUD_230400 = 230400
    BAUD_460800 = 460800
    BAUD_921600 = 921600

class Serial_Comm:
    def __init__(self):
        pass

    def connect(self):
        pass

    


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("연결된 시리얼 포트가 없습니다.")
    else:
        print("현재 연결된 시리얼 포트:")
        for port in ports:
            print(f"포트 이름: {port.device}")
            print(f"설명: {port.description}")
            print(f"하드웨어 ID: {port.hwid}")
            print("-" * 40)

def connect_to_port(port_name, baud_rate=9600, timeout=1):
    """지정된 포트에 연결."""
    try:
        ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout)
        print(f"{port_name} 포트에 성공적으로 연결되었습니다.")
        return ser
    except serial.SerialException as e:
        print(f"{port_name} 포트에 연결 실패: {e}")
        return None

def serial_write(ser, data):
    """지정된 데이터를 시리얼 포트에 쓰기."""
    try:
        ser.write(data.encode())
        print(f"시리얼 포트에 {data} 데이터를 쓰기 성공했습니다.")
    except serial.SerialException as e:
        print(f"시리얼 포트에 {data} 데이터를 쓰기 실패: {e}")

def serial_read(ser, size=1):
    """지정된 크기만큼 시리얼 포트에서 데이터 읽기."""
    try:
        data = ser.read(size)
        print(f"시리얼 포트에서 {data} 데이터를 읽었습니다.")
        return data
    except serial.SerialException as e:
        print(f"시리얼 포트에서 데이터 읽기 실패: {e}") 

list_serial_ports()
ser = connect_to_port("COM5",BaudRate.BAUD_230400,1)
serial_write(ser,"test")
data = serial_read(ser,5)
print(data)