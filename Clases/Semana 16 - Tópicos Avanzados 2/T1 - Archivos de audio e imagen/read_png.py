from zlib import compress, decompress, crc32


class Bytearray2D(bytearray):
    def __init__(self, content, width, height, has_scanlines=False, bytes_per_pixel=4):
        self.width = width
        self.height = height
        self.has_scanlines = has_scanlines
        self.bytes_per_pixel = bytes_per_pixel
        self.len_bytes_x = width * bytes_per_pixel + has_scanlines
        if content is None:
            # create bytearrayof 0s
            content = bytes(self.len_bytes_x*height)
        super().__init__(content)

    def copy(self):
        pass

    def __getitem__(self, key):
        if isinstance(key, tuple):
            pass
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            pass
        return super().__setitem__(key, value)


class PNG(Bytearray2D):
    HEADER = b'\x89PNG\r\n\x1a\n'
    def __init__(self, fname=''):
        self._idat_compressed = bytearray()
        self.width = None
        self.height = None
        with open(fname, 'rb') as png_file:
            header = png_file.read(0x8)
            # self._read_chunk(png_file)
        # super().__init__ missing

    def _read_chunk(self, file):
        chunk_content_length = None
        chunk_type = None
        chunk_content = None
        match chunk_type:
            case b'IHDR':
                self._read_IHDR(chunk_content)
            case b'IDAT':
                self._read_IDAT(chunk_content)
            case b'IEND':
                self._write_IDAT()
            case _:
                print('Skipped chunk', chunk_type)
                return True
        return chunk_type != b'IEND'
                
    def _read_IHDR(self, content):
        self.width = None
        self.height = None
        self.bit_depth = None
        self.color_type = None
        compression_method = None
        filter_method = None
        interlace_method = None
        print('bit_depth', self.bit_depth)
        print('color_type', self.color_type)
        print('compression method', compression_method)
        print('filter method', filter_method)
        print('interlace method', interlace_method)

    def _read_IDAT(self, content):
        self._idat_compressed += content

    def _write_IDAT(self):
        pass

    def _unfilter_scanlines(self, read_bytes_2d, write_bytes_2d):
        x_minus_1 = lambda x: x-write_bytes_2d.bytes_per_pixel
        pass


if __name__ == '__main__':
    PNG('dcc.png')
