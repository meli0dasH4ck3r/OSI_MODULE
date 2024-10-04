class TransportLayer:
    def __init__(self, protocol="TCP"):
        self.protocol = protocol

    def segment_data(self, data, segment_size=10):
        print(f"Transport Layer: Segmenting data into smaller parts")
        return [data[i:i+segment_size] for i in range(0, len(data), segment_size)]

    def reassemble_data(self, segments):
        print(f"Transport Layer: Reassembling data from segments")
        return ''.join(segments)
