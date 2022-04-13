# Caesar Cipher Encoder/Decoder

A terminal encoder/decoder for the Caesar cipher:

![caesar_cipher_GIF](https://user-images.githubusercontent.com/84557025/163131347-e67ff5fd-da06-4f45-bd59-973ebd92366d.gif)

## The cipher alphabet

For the cipher alphabet I've used the printable character set from Python's [string module](https://pymotw.com/3/string/index.html).

```python 
printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
```

## Warning

Don't use this to secure... [anything](https://cryptogramcenter.com/caesar-cipher-not-secure/).

## Acknowledgement 
I've used the brilliant [Colorama](https://github.com/tartley/colorama) for coloured terminal text on MS Windows.

Read more about the Caesar cipher [here](http://practicalcryptography.com/ciphers/caesar-cipher/).
