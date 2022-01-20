def encrypt(_string, _encrypt_key):
    _encrypted_list = []
    for i in range(len(_encrypt_key)):
        x = (_string[i] - ord('A') + _encrypt_key[i] - ord('A')) % 26 + ord('A')
        _encrypted_list.append(chr(x))
    encrypted = "".join(_encrypted_list)
    return encrypted


def decrypt(_encrypted, _encrypt_key):
    _decrypted_list = []
    for i in range(len(_encrypt_key)):
        x = ((_encrypted[i] + 26 - _encrypt_key[i]) % 26) + ord('A')
        _decrypted_list.append(chr(x))
    decrypted = "".join(_decrypted_list)
    return decrypted


def generate_encryption_key(strig, _encrypt_key):
    if len(strig) == len(_encrypt_key):
        return _encrypt_key
    else:
        for i in range(len(strig) - len(_encrypt_key)):
            _encrypt_key.append(_encrypt_key[i % len(_encrypt_key)])
    _encrypt_key = _encrypt_key[0:len(strig)]
    return _encrypt_key


def ask(state):
    string = [ord(char) for char in str(input(f"Type string that you want to be {state}: ")).upper()]
    encrypt_key = [ord(char) for char in str(input("Type encryption key: ")).upper()]

    return string, encrypt_key


if __name__ == "__main__":
    while True:
        state = str(input("Do u want to encrypt or decrypt? e/d "))

        if state in ["e", "encrypt"]:
            string, encrypt_key = ask("encrypt")
            encrypt_key = generate_encryption_key(string, encrypt_key)
            print(encrypt(string, encrypt_key))

        elif state in ["d", "decrypt"]:
            string, encrypt_key = ask("decrypt")
            encrypt_key = generate_encryption_key(string, encrypt_key)
            print(decrypt(string, encrypt_key))

        elif state in ["q", "quit"]:
            print("Quitting...")
            break
        elif state in ["h", "help"]:
            print("h, help - this command")
            print("e, encrypt - encrypt")
            print("d, decrypt - decrypt")
            print("q, quit - exit program")
        else:
            print("Input was invalid. Type help to see all commands avaible.")

