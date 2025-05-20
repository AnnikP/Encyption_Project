
import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string


charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
charset = list(charset)
key = charset.copy()

#Generates a randomized key and returns as a txt file dictionary, matching original charset and shuffled_chars
def generate_key():
    shuffled_char = key[:]
    random.shuffle(shuffled_char)
    file_path = filedialog.asksaveasfilename(title="Save key file", defaultextension = ".txt", filetypes=[("text files", "*.txt")])
    try:
        with open(file_path, 'w') as f:
            for original, shuffled in zip(charset, shuffled_char):
                f.write(f"{original}: {shuffled}\n")
            messagebox.showinfo("Success", "Your key has been generated")
    except Exception as e:
        messagebox.showerror("Error", f"failed to generate key: {e}")

#loads the key_file and sorts out the mapping and values of the shuffled chars
def load_key(key_file):
    mapping = {}
    with open(key_file, 'r') as f:
        for line in f:
            if ":" in line:
                original_char, value = line.strip().split(": ")
                mapping[original_char] = value
    return mapping


#loads the key and maps out the original chars to the shuffled chars
def reverse_key(key_file):
    mapping = {}
    with open(key_file, 'r') as f:
        for line in f:
            if ":" in line:
                original_char, value = line.strip().split(": ")
                mapping[value] = original_char
    return mapping


#takes the input file and reads the plain text and change it with shuffled char in key file
def encrypt_file():
    input_file = filedialog.askopenfilename(title="Select Input File")
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(title="Save Encrypted File as", defaultextension = ".txt", filetypes=[("text files", "*.txt")])
    key_file = filedialog.askopenfilename(title="Select Key File")

    if input_file and output_file and key_file:
        try:
            mapping = load_key(key_file)
            with open(input_file, 'r') as infile:
                plain_text = infile.read()
                cipher_text = "".join(mapping.get(char, char) for char in plain_text)
            with open(output_file, 'w') as outfile:
                outfile.write(cipher_text)
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt file: {e}")


#takes the input file and reverse the key switching out the characters and returning decrypted output
def decrypt_file():
    input_file = filedialog.askopenfilename(title="Select Encrypted File")
    if not input_file:
        return
    output_file = filedialog.asksaveasfilename(title="Save Decrypted File as", defaultextension = ".txt", filetypes=[("text files", "*.txt")])
    key_file = filedialog.askopenfilename(title="Select Key File")

    if input_file and output_file and key_file:
        try:
            mapping = reverse_key(key_file)
            with open(input_file, 'r') as infile:
                cipher_text = infile.read()
                decrypt_text = "".join(mapping.get(char, char) for char in cipher_text)
            with open(output_file, 'w') as outfile:
                outfile.write(decrypt_text)
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt file: {e}")

#Utilizes tkinter and creates a GUI for the program
def main():
        root = tk.Tk()
        root.title("AP Encrypt-n-Decrypt")
        root.geometry("400x300")

        tk.Label(root, text="AP Encrypt-n-Decrypt", font=("Ariel", 14, "bold")).pack(pady=10)

        tk.Button(root, text="Generate Key", command=generate_key, width=20).pack(pady=5)
        tk.Button(root, text="Encrypt File", command=encrypt_file, width=20).pack(pady=5)
        tk.Button(root, text="Decrypt File", command=decrypt_file, width=20).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

        root.mainloop()
        
if __name__ == '__main__':
    main()
