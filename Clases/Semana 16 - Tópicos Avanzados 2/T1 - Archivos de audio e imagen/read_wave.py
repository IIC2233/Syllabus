def from_bytes(data):
    return int.from_bytes(data, byteorder='little')

def to_bytes(number, length):
    return int.to_bytes(number, length, byteorder='little')


class WAVE(bytearray):
    def __init__(self, filename):
        super().__init__(b'')
        with open(f"{filename}.wav", 'rb') as wave_in:
            data = wave_in.read()
        self.filename = filename
    
    def save(self):
        with open(f'{self.filename}_new.wav', 'wb') as wave_out:
            pass


if __name__ == '__main__':
    filename = None
    WAVE(filename)
