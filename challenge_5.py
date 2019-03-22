import binascii

def repeating_key_xor(a : bytearray, b : bytearray):
    result = bytearray()
    for i, byte in enumerate(a):
        result.append(byte ^ b[i % len(b)])
    return result

input_string = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
input_bin = bytearray(input_string, 'utf-8')
key = "ICE"
key_bin = bytearray(key, 'utf-8')
encrypted_input = repeating_key_xor(input_bin, key_bin)

print(binascii.hexlify(encrypted_input))