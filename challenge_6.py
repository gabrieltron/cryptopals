import base64
import string

def hamming_distance(a : bytearray, b : bytearray):
    while len(a) != len(b):
        if len(a) > len(b):
            b.insert(0,0)
        else:
            a.insert(0,0)

    distance = 0
    for byte_a, byte_b in zip(a, b):
        for i in range(8):
            bit_a = (byte_a >> i) & 1
            bit_b = (byte_b >> i) & 1

            if bit_a != bit_b:
                distance += 1

    return distance

def find_probable_key_length(message : bytearray):
    # try sizes 2 to 40
    best_distance = 123456789
    best_guess = -1
    for guessed_size in range(2,41):
        blocks = []
        n_blocks = len(message) // guessed_size
        for block in range(n_blocks):
            start_byte = block * guessed_size
            end_byte = start_byte + guessed_size
            blocks.append(message[start_byte:end_byte])

        distance_sum = 0
        for i in range(len(blocks)-1):
            distance_sum += hamming_distance(blocks[i], blocks[i+1])
        averaged_distance = distance_sum / len(blocks)
        normalized_distance = averaged_distance/guessed_size

        if best_distance > normalized_distance:
            best_distance = normalized_distance
            best_guess = guessed_size
    return best_guess

def transpose_message(message : bytearray, probable_key_length : int):
    blocks = []
    for i in range(probable_key_length):
        blocks.append(bytearray())
    
    for i, byte in enumerate(message):
        byte_position = i % probable_key_length
        blocks[byte_position].append(byte)

    return blocks 

def single_byte_xor(a : bytearray, b : int):
    result = bytearray()
    for byte in a:
        result.append(byte ^ b)
    return result

def repeating_key_xor(a : bytearray, b : bytearray):
    result = bytearray()
    for i, byte in enumerate(a):
        result.append(byte ^ b[i % len(b)])
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
            points -= 15

    letters_frequency = {}
    n_chars = len(message)
    for letter in letters_counter:
        letters_frequency[letter] = (letters_counter[letter] / n_chars) * 100

    for letter in expected_frequency:
        if letter in letters_frequency:
            points -= abs(expected_frequency[letter] - letters_frequency[letter])
        else:
            points -= expected_frequency[letter]
    return points

def find_best_key(message : bytearray):
    biggest_points = -123456789

    best_key = bytearray()
    for key in range(256):
        decrypted_message = single_byte_xor(message, key)
        points = calculate_points(decrypted_message)

        if points > biggest_points:
            biggest_points = points
            best_key = key
    return (best_key, biggest_points)

def calculate_probable_key(transposed_blocks : list, probable_key_length : int):
    probable_key = bytearray()
    for block in transposed_blocks:
        best_key, _ = find_best_key(block)
        probable_key.append(best_key)
    return probable_key

if __name__ == "__main__":
    b64_message = ''
    while True:
        try:
            b64_message += input()
        except EOFError:
            break
    message_text = base64.b64decode(b64_message)
    message = bytearray(message_text)

    probable_key_length = find_probable_key_length(message)
    transposed_blocks = transpose_message(message, probable_key_length)
    probable_key = calculate_probable_key(transposed_blocks, probable_key_length)
    plain_text = repeating_key_xor(message, probable_key)
