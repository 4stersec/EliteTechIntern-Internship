from PIL import Image
import numpy as np
import os

def transform_pixels(image, shift):
    pixels = np.array(image)
    # Apply a shift to each pixel value and ensure values stay within 0-255
    transformed_pixels = (pixels + shift) % 256
    return Image.fromarray(transformed_pixels.astype(np.uint8))

def encrypt_image(input_path, output_path, shift):
    print("Encrypting image...")
    image = Image.open(input_path)
    encrypted_image = transform_pixels(image, shift)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, shift):
    print("Decrypting image...")
    image = Image.open(input_path)
    decrypted_image = transform_pixels(image, -shift)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def ensure_extension(file_path, default_ext='.png'):
    base, ext = os.path.splitext(file_path)
    if not ext:
        file_path = base + default_ext
    return file_path

def main():
    print("Image Encryption/Decryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    
    choice = input("Enter 1 for encryption or 2 for decryption: ")
    
    if choice not in ['1', '2']:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    input_path = input("Enter the path to the image file: ")
    output_path = input("Enter the path to save the output image file (including filename and extension): ")
    
    shift = int(input("Enter the shift value (integer): "))

    # Expand user directory if necessary
    input_path = os.path.expanduser(input_path)
    output_path = os.path.expanduser(output_path)
    
    # Ensure output path has a valid extension
    output_path = ensure_extension(output_path)
    
    # Validate input path
    if not os.path.isfile(input_path):
        print(f"Input file does not exist: {input_path}")
        return

    try:
        if choice == '1':
            encrypt_image(input_path, output_path, shift)
        elif choice == '2':
            decrypt_image(input_path, output_path, shift)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
