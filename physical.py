import socket

class PhysicalLayer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5050

    def transmit_data(self, data):
        print(f"Physical Layer: Transmitting data...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(data.encode())

    def receive_data(self):
        print("Physical Layer: Receiving data")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                print(f"Physical Layer: Data received: {data.decode()}")
                return data.decode()
