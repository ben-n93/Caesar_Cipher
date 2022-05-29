# Caesar Cipher encrypter/decrypter/codebreaker

A terminal encoder/decoder/codebreaker for the Caesar cipher:

![caesar_cipher](https://user-images.githubusercontent.com/84557025/163703460-c2997b5f-9dcb-4dc3-b887-7c113ef7023f.gif)

Read more about the Caesar cipher [here](http://practicalcryptography.com/ciphers/caesar-cipher/).

## The cipher alphabet

For the cipher alphabet I've used the **ascii_lowercase** constant and from Python's [string module](https://pymotw.com/3/string/index.html).

```python 
ALPHABET='abcdefghijklmnopqrstuvwxyz'
```

## Warning

Don't use this to secure... [anything](https://cryptogramcenter.com/caesar-cipher-not-secure/).

## Acknowledgement 
I've used the brilliant [Colorama](https://github.com/tartley/colorama) for coloured terminal text.
