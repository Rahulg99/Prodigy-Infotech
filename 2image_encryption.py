from PIL import Image
import numpy as np
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        # Open the image
        image = Image.open(input_path)
        np_image = np.array(image)

        # Encrypt/Decrypt the image by applying XOR with the key
        encrypted_decrypted_image = np_image ^ key

        # Save the modified image
        result_image = Image.fromarray(encrypted_decrypted_image)
        result_image.save(output_path)
        print(f"Image saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
    except Image.UnidentifiedImageError:
        print(f"Error: The file {input_path} is not a valid image file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    key = 123  # Example key for XOR operation

    
    input_image_path = r"C:\Users\RAHUL ANAND\Desktop\Prodigy Infotech\input_image.png"
    encrypted_image_path = r"C:\Users\RAHUL ANAND\Desktop\Prodigy Infotech\encrypted_image.png"
    decrypted_image_path = r"C:\Users\RAHUL ANAND\Desktop\Prodigy Infotech\decrypted_image.png"

    # Encrypt the image
    encrypt_decrypt_image(input_image_path, encrypted_image_path, key)

    # Decrypt the image
    encrypt_decrypt_image(encrypted_image_path, decrypted_image_path, key)
