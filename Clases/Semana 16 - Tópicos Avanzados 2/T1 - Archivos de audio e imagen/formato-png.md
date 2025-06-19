# PNG FORMAT
https://en.wikipedia.org/wiki/PNG


## Chunk
|Length| Chunk type |Chunk data|CRC32|
|-|-|-|-|
|4 bytes|4 bytes|Length bytes|4 bytes|

CRC32 is applied to concatenation of `Chunk type` with `Chunk data`

### Critical chunks
|name| content |
|-----|---|
|IHDR|<ol><li>(4B) width<li>(4B) height<li>(1B) bit depth<li>(1B) color type<li>(1B) compression methid<li>(1B) filter method<li>(1B) interlace method|
|IDAT|Length compressed content|
|IEND|(0B)|

Additional information:
* IHDR must be the first chunk
* Use byteorder big
* bit depth: bits per channel
* color type: (2 is RGB, 6 is RGBA)
* compression method, filter method: Always 0 in docs
* interlace method: 0 is no interlace, 1 is Adam7 interlace.
* All IDAT need to be concatenated before decompressing
* RGB is 3 channels and RGBA is 4 channels

### Decompressed IDAT Reading
https://www.libpng.org/pub/png/spec/1.1/png-1.1-pdg.html#Filters

Each scanline starts with a byte that corresponds to the compression algorithm used.
* scanline: row of image
* filters used: 0, 1, 2, 3
