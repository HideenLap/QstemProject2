from time import sleep


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result


def encrypt(text, shifts):
    encrypted_text = text
    for shift in shifts:
        encrypted_text = caesar_cipher(encrypted_text, shift)
    return encrypted_text


def decrypt(text, shifts):
    decrypted_text = text
    for shift in shifts:
        decrypted_text = caesar_cipher(decrypted_text, -shift)
    return decrypted_text


def enc_main():
    word = "Password for that door is qstem "
    shift_values = [3, 1, 4, 1, 5]
    encrypted_word = encrypt(word, shift_values)
    print(encrypted_word)
    sleep(1)
    shift_hints = ", ".join(map(str, shift_values))
    print(f"Caesar = [{shift_hints}]")
    sleep(1)
    print(f'Thats should be, a password to that strange door')


def return_password():
    return "qstem"
