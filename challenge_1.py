import base64

input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

input_bytes = bytearray.fromhex(input_string)
input_base64 = base64.b64encode(input_bytes)

print(input_base64)