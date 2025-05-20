# Encyption_Project
Overview:
Utilizes symmetric key algorithm, using one key for both encryption and decryption
Encryption using a mix of transposition and substitution using the key
Decryption reversing the process of encryption, using key to revert cipher text back to original text
Programming language: Python
Libraries Used:
Tkinter: for graphical user interface
From tkinter, filedialog, and messagebox.
Filedialog: to create interface to open and save files
Messagebox: to created messages prompting a task is completed
Random: for randomizing characters for our generated key
String: to cleanly use each English character
Generating Key:
Required for encryption and decryption

Copies the key which copy the character set of all possible characters, to variable shuffled_char
Randomizes the characters using the random library
Creates a new file based on user input of the file name to save it in
Saves as a dictionary of the original characters as a key, and shuffled characters as a value
Encryption

Asks the user to input the file to encrypt (then check if its true)
Prompts to create a encrypted file
Selects the key generated from generate_key function
Loads the key, with mapping of the original character to shuffled character

For each character in plain text it is substituted by the shuffled character based on the index of the original character
Then saves cipher text to the encrypted file
Decryption

Prompts user to select the encrypted file to decrypt
Create a save file for the decrypted text
Prompts to select the key file
Reverse the key by mapping the shuffled character as the key, and original as value

Then for each character in cipher text, is substituted by the original character it replaced using the key
Then saves into the decrypted file we created.



GUI / User interface

Creates the user interface, with buttons for each element of: Generate key, encrypt file, decrypt file, and exit
