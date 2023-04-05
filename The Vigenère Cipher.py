#import tkinter module
import tkinter as tk

#the user ought to input a message and key, then the program will encrypt the message using the key
#to be more, engaging, this program will use tkinter module to create GUI in order for user to enter the message and key in new window
#then user will click a button to encrypt the message
#finally, the encrypted message will be displayed

#define a function that takes the message and key
def encrypt(message, key):
#remove the spaces, if any, from the message and convert to uppercase    
    message = message.replace(" ", "").upper()
#also, the key is set to be uppercase
    key = key.upper()

#initialize the ciphertxt as empty string
    ciphertxt = ""
#iterate over each character in the message
    for i in range(len(message)):
        #get the corresponding letter values(0-25) and subtract 65 to get value bet. 0 & 25
        mssg_value = ord(message[i]) - 65
        #likewise in key by using the modulo operator to cycle through the key characters
        key_value = ord(key[i%len(key)]) - 65
        #then add the two values and get the result modulo 26
        encrypt_value = (mssg_value + key_value) % 26
        #convert that result back to character and add the ciphertext
        ciphertxt += chr(encrypt_value + 65)
    
    #return the ciphertext as string
    return ciphertxt


#--for GUI --
#define function to be called when the button is clicked
def trigger_action():
    #get the message and key from respective entry fields
    message = mssg_entry.get()
    key = key_entry.get()
    #store the result of the first function in ciphertext
    ciphertxt = encrypt(message, key)
    #then a encrypted message must be displayed in the ciphertext field
    ciphertxt_entry.delete(0, tk.END)
    ciphertxt_entry.insert(0, ciphertxt)

#now, create the window with its title
win = tk.Tk()
win.title("The Vigenère Cipher")

#make the input fields, button, and output elements
##input fields
mssg_label = tk.Label(win, text = "Message:", font = ("Arial", 10))
mssg_entry = tk.Entry(win, width = 30)
envelope = tk.Label(win, text = "\U0001F582", font = ("Arial Bold", 13, "bold"))
key_label = tk.Label(win, text = "Key:", font = ("Arial", 10))
key_entry = tk.Entry(win, width = 30)
squared_key = tk.Label(win, text = "\U000026BF", font = ("Arial", 10))

##buttons
encrypt_button = tk.Button(win, text = "Encypt", foreground = "blue", command = trigger_action)

##output elements
ciphertxt_label = tk.Label(win, text = "Ciphertext:", font = ("Arial Bold", 10))
ciphertxt_entry = tk.Entry(win, width = 30)

#arrange the layout
mssg_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
mssg_entry.grid(row=0, column=1, padx=5, pady=5)
envelope.grid(row=0, column=2, padx=5, pady=5, sticky="e")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
key_entry.grid(row=1, column=1, padx=5, pady=5)
squared_key.grid(row=1, column=2, padx=5, pady=5, sticky="e")
encrypt_button.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
ciphertxt_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
ciphertxt_entry.grid(row=3, column=1, padx=5, pady=5)

#start the tkinter main event loop
win.mainloop()