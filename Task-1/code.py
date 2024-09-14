def caesar_cipher(text, shift):
    result = []
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Enter 1 for encryption or 2 for decryption: ")
    
    if choice not in ['1', '2']:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == '1':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == '2':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
