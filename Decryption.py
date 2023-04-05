import emoji
from PIL import Image, ImageTk
import tkinter as tk

#ask the user to input the encrypted string with bold text
encrypted_string = input("\033[1mEnter a string to decrypt: \033[0m")

#replace the symbols in the string to their corresponding letters:
## replace '*' with 'a'
## replace '&' with 'e'
## replace '#' with 'i'
## replace '+' with 'o'
## replace '!' with 'u'
decrypted_string = encrypted_string.replace('*', 'a') \
                                    .replace('&', 'e') \
                                    .replace('#', 'i') \
                                    .replace('+', 'o') \
                                    .replace('!', 'u')

#find the word 'brown' in the decrypted string
brown_word = decrypted_string.find("brown")

#highlight the word 'brown' with its color
#then add emoji at the end of the sentence
highlighted_word = decrypted_string[:brown_word] + \
"\033[38;2;165;42;42m" + "brown" + "\033[0m" + \
decrypted_string[brown_word + 5:] + \
emoji.emojize(":fox:" + ":person_cartwheeling:" + ":dog_face:")

#print the output
print("\n\033[1mThe Plain Text: \033[0m" + highlighted_word)

#for more fun, a gif will be shown for the user after the output
#get the path of the gif file to open
gif_path = "C:/Users/BELLE/Downloads/foxdog.gif"
gif = Image.open(gif_path)

#set a window to display the gif with its title, label widget
root = tk.Tk()
root.title("Fox and Dog")
label = tk.Label(root)
label.pack()

#then a list will be created for the PhotoImage instances
gif_frames = []

#update the gif with a function
def gif_update(frame):
    gif_frame = gif_frames[frame]
    label.config(image=gif_frame)
    root.after(50, gif_update, (frame + 1) % gif.n_frames)
    
#loop for the frames of the gif by the PhotoImage instances
for i in range(gif.n_frames):
    gif.seek(i)
    gif_frames.append(ImageTk.PhotoImage(gif))

gif_update(0)

#finally, run the main loop
root.mainloop()
