import base64
import binascii

def xor(a : bytearray, b : bytearray):
    result = bytearray()
    for byte_a, byte_b in zip(a, b):
        result.append(byte_a ^ byte_b)

    return result

input_1_string = "1c0111001f010100061a024b53535009181c"
input_2_string = "686974207468652062756c6c277320657965"

input_1_bin = bytearray.fromhex(input_1_string)
input_2_bin = bytearray.fromhex(input_2_string)

xor_value = xor(input_1_bin, input_2_bin)
xor_value_hex = binascii.hexlify(xor_value)

print(xor_value_hex)