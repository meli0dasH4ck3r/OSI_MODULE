import base64

class PresentationLayer:
    def encode_data(self, data):
        print("Presentation Layer: Sending data")
        encoded_data = base64.b64encode(data.encode()).decode()  
        return encoded_data  

    def decode_data(self, data):
        print("Presentation Layer: Receiving data")
        decoded_data = base64.b64decode(data.encode()).decode()  
        return decoded_data  
