import zlib

class DataLinkLayer:
    def frame_data(self, data):
        print(f"Data Link Layer: Adding CRC and framing data")
        crc = zlib.crc32(data.encode())
        framed_data = f"{data}:{crc}"
        return framed_data

    def unframe_data(self, data):
        print(f"Data Link Layer: Checking CRC and unframing data")
        try:
            original_data, received_crc = data.rsplit(":", 1)
            calculated_crc = zlib.crc32(original_data.encode())
            if int(received_crc) == calculated_crc:
                print("Data Link Layer: CRC check passed")
                return original_data
            else:
                raise ValueError("Data corruption detected: CRC mismatch")
        except ValueError as e:
            print(f"Error: {e}")
            return None
