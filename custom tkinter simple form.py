from tkinter import *
import customtkinter
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

root=customtkinter.CTk()
root.title('img app')
root.iconbitmap('home.ico')

def btnwork():
    mylbl.configure(text=f'hello {mentry.get()}')
    mentry.configure(state='disabled')

def clear():
    mentry.delete(0, 'end')
    mentry.configure(state='normal')

mentry=customtkinter.CTkEntry(root,placeholder_text='enter your name')
mentry.pack(pady=20)

mylbl=customtkinter.CTkLabel(root,text='')
mylbl.pack(pady=30)

btn=customtkinter.CTkButton(
    root,text='click this',
    width=50,
    height=30,
    corner_radius=8,
    fg_color='#ffdd05',
    hover_color='white',
    text_color='black',
    border_width=5,
    border_color='black',
    font=customtkinter.CTkFont('arial',24),
    command=btnwork,
)
btn.pack(pady=40)

cbtn=customtkinter.CTkButton(
    root,text='clear',
    width=50,
    height=30,
    corner_radius=8,
    fg_color='#ffdd05',
    hover_color='white',
    text_color='black',
    border_width=5,
    border_color='black',
    font=customtkinter.CTkFont('arial',24),
    command=clear,
)
cbtn.pack(pady=40)




root.mainloop()


