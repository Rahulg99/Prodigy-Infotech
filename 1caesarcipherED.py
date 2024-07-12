def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(text, shift):
    """
    Decrypts
    """
    return caesar_encrypt(text, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter E for encrypt or D for decrypt.")
        return

    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if choice == 'E':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
