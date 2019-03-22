import binascii

def read_input():
    hex_ciphertexts = []
    while True:
        try:
            text = input()
        except EOFError:
            break
        hex_ciphertexts.append(text)
    cipher_texts = list(map(bytearray.fromhex, hex_ciphertexts))
    return cipher_texts

def calculate_repeated_blocks(message : bytearray, block_size : int):
    blocks_in_text = set()
    repeated_blocks = 0
    while message:
        block = message[:block_size]

        block = bytes(block)
        if block in blocks_in_text:
            repeated_blocks += 1
        else:
            blocks_in_text.add(block)
    
        message = message[block_size:]

    return repeated_blocks

if __name__ == "__main__":
    cipher_texts = read_input()
    max_repeated_blocks = 0
    max_repeated_index = -1
    for index, cipher_text in enumerate(cipher_texts):
        repeated_blocks = calculate_repeated_blocks(cipher_text, 16)
        if repeated_blocks > max_repeated_blocks:  
            max_repeated_block = repeated_blocks
            max_repeated_index = index
    
    print(max_repeated_index)

