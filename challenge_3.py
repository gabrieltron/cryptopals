import base64
import binascii
import string

def single_byte_xor(a : bytearray, b : int):
    result = bytearray()
    for byte in a:
        result.append(byte ^ b)
    return result

def calculate_points(message : bytearray):
    expected_frequency = {
        'a': 08.167,
        'b': 01.492,
        'c': 02.782,
        'd': 04.253,
        'e': 12.702,
        'f': 02.228,
        'g': 02.015,
        'h': 06.094,
        'i': 06.966,
        'j': 00.153,
        'k': 00.772,
        'l': 04.025,
        'm': 02.406,
        'n': 06.749,
        'o': 07.507,
        'p': 01.929,
        'q': 00.095,
        'r': 05.987,
        's': 06.327,
        't': 09.056,
        'u': 02.758,
        'v': 00.978,
        'w': 02.360,
        'x': 00.150,
        'y': 01.974,
        'z': 00.074,
    }

    points = 100
    letters_counter = {}
    for byte in message:
        letter = chr(byte).lower()
        if letter in letters_counter:
            letters_counter[letter] += 1
        else:
            letters_counter[letter] = 1
        if letter not in string.printable:
            points -= 10

    letters_frequency = {}
    n_chars = len(message)
    for letter in letters_counter:
        letters_frequency[letter] = letters_counter[letter] / n_chars

    for letter in expected_frequency:
        if letter in letters_frequency:
            points -= abs(expected_frequency[letter] - letters_frequency[letter])
        else:
            points -= expected_frequency[letter]
    return points

input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
input_bin = bytearray.fromhex(input_string)

biggest_points = -123456789
best_message = bytearray()
best_key = bytearray()
for key in range(256):
    decrypted_message = single_byte_xor(input_bin, key)
    points = calculate_points(decrypted_message)

    if points > biggest_points:
        biggest_points = points
        best_message = decrypted_message
        best_key = key
