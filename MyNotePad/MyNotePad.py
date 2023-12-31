#MyNotePad
#icons from www.doublejdesign.co.uk
import tkinter 
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

#definewindow
root= tkinter.Tk()
root.title('NotePad')
root.iconbitmap('pad.ico')
root.geometry("600x600")
root.resizable(0, 0)

#Define colors and fonts
text_color = ('#fffacd')
menu_color = ('#dbd9db')
root_color = ('#6c809a')
root.config(bg= root_color)

#define functions
def change_font(event):
    """Change the given font based off dropbox options"""
    if font_option.get()=='none':
        my_font=(font_family.get(), font_size.get())
    else:
        my_font=(font_family.get(), font_size.get(), font_option.get())
    
    #change the font style
    input_text.config(font=my_font)

def new_note():
    """Create a new Note which essentially clears the screen"""
    #use a messagebox to ask for a new note
    question = messagebox.askyesno('New Note', ' Are you sure you want to start a new note?')
    if question == 1:
        #ScrolledText widgets starting index is 1.0 not 0.
        input_text.delete("1.0", END)
    
def close_note():
    """Closes the note which essentially quits the program"""
    #Use a messagebox to ask to close
    question=messagebox.askyesno("Close Note", "Are you sure you want to close your note")
    if question ==1:
        root.destroy()

def save_note():
    """Save the note first three lines are saved as font family, font size and font option"""
    #Use file dialog to get location and name of where/what to save the file as
    save_name = filedialog.asksaveasfile(initialdir="./", title="Save Note", filetypes=(("Text Files", "*.txt"), ("All File", "*.*")))
    with open(save_name, "w") as f:
        #first three lines are saved as font family, font size and font option font size should be string not an intgr
        f.write(font_family.get()+"\n")
        f.write(str(font_size.get())+"\n")
        f.write(font_option.get()+"\n")

        #write remaining text in field to the file
        f.write(input_text.get("1.0", END))

def open_note():
    """open a not which has been saved previously....first three lines are saved as font family, font size and font option first set the font , then load the text"""
    #Use filedialog to get location and directory of the file
    open_name= filedialog.askopenfilename(initialdir="./", title="Open Note", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    with open(open_name, "r") as f:
        #clear the current text
        input_text.delete("1.0", END)

        #first three lines are saved as font family, font size and font option , The new line char at the end of each line must be striped
        font_family.set(f.readline().strip()) 
        font_size.set(f.readline().strip())
        font_option.set(f.readline().strip())

        #Call the change font for these .set() and pass an arbitrary value 
        change_font(1)

        #read the rest of the file and insert it into the text field
        text=f.read()
        input_text.insert("1.0", text)

#define Layout
#define frames
menu_frame = tkinter.Frame(root, bg= menu_color)
text_frame = tkinter.Frame(root, bg= text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout4MenuFrame
#Build the Menu, New, Open, Save, Close, FontFamily, FontSize, FontOption, 
new_image =ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image= ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)    

#Create a list for fonts to use 
families = ["Terminal", "Modern", "Script", "Courier", "Arial", "Calibri", "Cambria", "Georgia", "MS Gothic", "SimSun", "Tahoma", "Times New Roman", "Verdana", "Wingdings"]
font_family= StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')
#set the width so it will fit times new roman and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes= [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size= IntVar()
font_size_drop= tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
#set width to be constant even if its 8
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)
options = ["normal", "bold", "italic"]
font_option= StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
font_option.set('normal')
#ser the width to be constant
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

#Layout for the next frame
my_font= (font_family.get(), font_size.get())

#Create input_text as a scrolltext so you can scroll through the text field
#Set default width and height to be more than the window size so that on the smallest text size, the text field size is constant
input_text= tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=100, bg=text_color, font=my_font)
input_text.pack()
#run the APP
root.mainloop()