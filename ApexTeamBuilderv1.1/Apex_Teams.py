
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def load_button_clicked():
    messagebox.showinfo("Load", "Load Button Clicked")


def save_button_clicked():
    messagebox.showinfo("Save", "Save Button Clicked")


def generate_button_clicked():
    messagebox.showinfo("Generate", "Generate Button Clicked")


def delete_button_clicked():
    messagebox.showinfo("Delete", "Delete Button Clicked")


def undo_button_clicked():
    messagebox.showinfo("Undo", "Undo Button Clicked")


window = Tk()

window.geometry("243x431")
window.configure(bg="#313131")

canvas = Canvas(
    window,
    bg="#313131",
    height=431,
    width=243,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("Locked_In_Fish.png"))
image_1 = canvas.create_image(
    121.0,
    215.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("Teams_Generated_Display.png"))
image_2 = canvas.create_image(
    123.0,
    343.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("Named_List_Holder.png"))
image_3 = canvas.create_image(
    123.0,
    213.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Load_Button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=load_button_clicked,
    relief="flat"
)
button_1.place(
    x=143.0,
    y=397.0,
    width=72.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Save_Button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=save_button_clicked,
    relief="flat"
)
button_2.place(
    x=17.0,
    y=397.0,
    width=72.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Generate_Button.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=generate_button_clicked,
    relief="flat"
)
button_3.place(
    x=168.0,
    y=93.0,
    width=72.0,
    height=31.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("Delete_Button.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=delete_button_clicked,
    relief="flat"
)
button_4.place(
    x=6.0,
    y=93.0,
    width=113.0,
    height=31.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("Undo_Button.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=undo_button_clicked,
    relief="flat"
)
button_5.place(
    x=119.0,
    y=93.0,
    width=49.0,
    height=31.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("User_Text_Field.png"))
entry_bg_1 = canvas.create_image(
    164.5,
    73.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=89.0,
    y=58.0,
    width=151.0,
    height=28.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("Enter_Name_Text.png"))
image_4 = canvas.create_image(
    46.0,
    72.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("Apex_Teams_Header.png"))
image_5 = canvas.create_image(
    121.0,
    29.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
