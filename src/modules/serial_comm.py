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

class SERIAL_MODULE:
    def __init__(self):
        self.available_ports_name = []
        self.serial_ports = []
        self.list_serial_ports()
        pass

    def print_serial_ports(self, port):
        print("-" * 40)
        print(f"포트 이름: {port.device}")
        print(f"설명: {port.description}")
        print(f"하드웨어 ID: {port.hwid}")
        print("-" * 40)

    def list_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        if not ports:
            print("연결된 시리얼 포트가 없습니다.")
            return None
        for port in ports:
            self.available_ports_name.append(port.name)

    def find_serial_port(self, port_name):
        if self.serial_ports == []:
            return None
        for ser in self.serial_ports:
            if port_name == ser.name:
                return ser
        return None

    def connect(self, port_name, baud_rate=9600, timeout=1):
        """지정된 포트에 연결."""
        try:
            ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout)
            print(f"{port_name} 포트에 성공적으로 연결되었습니다.")
            print(f"시리얼 포트 이름: {ser.name}")
            print(f"시리얼 포트 하드웨어 ID: {ser.port}")
            print(f"시리얼 포트 버스 유형: {ser.baudrate}")
            print(f"시리얼 포트 시간초과: {ser.timeout}")
            print(f"시리얼 포트 디버깅: {ser.port}")
            self.serial_ports.append(ser)
            return ser
        except serial.SerialException as e:
            print(f"{port_name} 포트에 연결 실패: {e}")
            return None

    def disconnect(self, ser):
        """지정된 시리얼 포트를 연결 해제."""
        if self.serial_ports.count(ser) == 0:
            print(f"{ser.name} 포트를 연결 해제 실패: 연결된 포트가 없습니다.")
            return False
        try:
            ser.close()
            print(f"{ser.name} 포트를 연결 해제 성공했습니다.")
            self.serial_ports.remove(ser)
            return True
        except serial.SerialException as e:
            print(f"{ser.name} 포트를 연결 해제 실패: {e}")
            return False

    def write(self, ser, data):
        """지정된 데이터를 시리얼 포트에 쓰기."""
        try:
            ser.write(data.encode())
            print(f"시리얼 포트에 {data} 데이터를 쓰기 성공했습니다.")
        except serial.SerialException as e:
            print(f"시리얼 포트에 {data} 데이터를 쓰기 실패: {e}") 

    def read(self, ser, size=1):
        """지정된 크기만큼 시리얼 포트에서 데이터 읽기."""
        try:
            data = ser.read(size)
            print(f"시리얼 포트에서 {data} 데이터를 읽었습니다.")
            return data
        except serial.SerialException as e:
            print(f"시리얼 포트에서 데이터 읽기 실패: {e}")