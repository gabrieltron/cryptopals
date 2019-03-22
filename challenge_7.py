import base64
from Crypto.Cipher import AES

def decrypt_text(text : bytearray):
    aes= AES.new('YELLOW SUBMARINE', AES.MODE_ECB)

    decrypted_text = bytearray()
    while encrypted_text:
        to_be_decrypted = encrypted_text[:16]
        encrypted_text = encrypted_text[16:]

        decrypted_phrase = aes.decrypt(bytes(to_be_decrypted))
        decrypted_text.extend(decrypted_phrase)
    return decrypt_text


b64_text = ''
while True:
    try:
        b64_text += input()
    except EOFError:
        break
decoded_text = base64.b64decode(b64_text)
encrypted_text = bytearray(decoded_text)

aes= AES.new('YELLOW SUBMARINE', AES.MODE_ECB)

decrypted_text = bytearray()
while encrypted_text:
    to_be_decrypted = encrypted_text[:16]
    encrypted_text = encrypted_text[16:]

    decrypted_phrase = aes.decrypt(bytes(to_be_decrypted))
    decrypted_text.extend(decrypted_phrase)
