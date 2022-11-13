import tkinter as tk
from PIL import Image, ImageTk
from time import sleep as wait
# from tkinter.ttk import Combobox


# Declare global variables here
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650
LOGO_WIDTH = 100
LOGO_HEIGHT = 100
FRAME_BG = "#0D6EFD"


# GUI APP MAIN WINDOW
window = tk.Tk()

# TKINTER WINDOW CONFIGURATION
window.title("My GUI")
window.geometry("1000x650+170+25")
window.resizable(False, False)
window.config(bg="#0D6EFD")


# BUTTON COMMANDS
def on_exit():
	window.destroy()


def show_profile():
	myname_label.configure(text="Rensyl Quiroben")
	mycourse_label.configure(text="Computer Science")
	caption_label.configure(text="Personal GUI")
	portfolio_btn.configure(text="View Portfolio", command=show_portfolio)
	bootstrap_label.configure(text="Personal GUI")
	sqlite_label.configure(text="Personal GUI")
	# course_label.configure(text="")


def show_portfolio(): 
	myname_label.configure(text="Here's my portfolio.")
	mycourse_label.configure(text="")
	caption_label.configure(text="")
	portfolio_btn.configure(text="View Profile", command=show_profile)
	bootstrap_label.pack(pady=10, side="left")
	sqlite_label.pack(pady=10, side="right")
	course_label.configure(text="")


def get_course():
	if course_entry.get() == "" or course_entry.get().startswith(" "):
		return
	elif len(course_entry.get()) > 64:
		res = "Too long !!!"
	elif len(course_entry.get()) > 30 and len(course_entry.get()) < 65:
		whole = []
		course = course_entry.get()
		mid = len(course) >> 1
		first_half = course[:mid+1]
		second_half = course[mid+1:]
		whole.append(first_half)
		whole.append(second_half)
		join_course = '\n'.join(whole)
		res = join_course  + " is a great course!"
	else:
		res = course_entry.get().capitalize()  + " is a great course!"

	course_label.configure(text=res)
	course_entry.delete(0, "end")


def get_course_event(event):
	if course_entry.get() == "" or course_entry.get().startswith(" "):
		return
	elif len(course_entry.get()) > 64:
		res = "Too long !!!"
	elif len(course_entry.get()) > 30 and len(course_entry.get()) < 65:
		whole = []
		course = course_entry.get()
		mid = len(course) >> 1
		first_half = course[:mid+1]
		second_half = course[mid+1:]
		whole.append(first_half)
		whole.append(second_half)
		join_course = '\n'.join(whole)
		res = join_course  + " is a great course!"
	else:
		res = course_entry.get().capitalize()  + " is a great course!"

	course_label.configure(text=res)
	course_entry.delete(0, "end")



#          TKINTER WIDGETS

# PHOTOIMAGES here
python_pil_image = Image.open("assets/images/Python Logo.png")
python_resize_pil_image = python_pil_image.resize((LOGO_WIDTH, LOGO_HEIGHT))
python_logo = ImageTk.PhotoImage(python_resize_pil_image)

bootstrap_pil_image = Image.open("assets/images/Bootstrap Logo.png")
bootstrap_resize_pil_image = bootstrap_pil_image.resize((LOGO_WIDTH, LOGO_HEIGHT))
bootstrap_logo = ImageTk.PhotoImage(bootstrap_resize_pil_image)

sqlite_pil_image = Image.open("assets/images/SQLite Logo.png")
sqlite_resize_pil_image = sqlite_pil_image.resize((LOGO_WIDTH, LOGO_HEIGHT))
sqlite_logo = ImageTk.PhotoImage(sqlite_resize_pil_image)


# FRAMES, LABELFRAMES here
topframe = tk.Frame(window, bg=FRAME_BG)
topframe_center = tk.Frame(topframe, bg=FRAME_BG)
topframe_right = tk.Frame(topframe, bg=FRAME_BG)
bottomframe = tk.Frame(window, bg=FRAME_BG)
logo_frame = tk.Frame(window, bg=FRAME_BG)


# LABELS, ENTRY, BUTTONS here
newline = tk.Label(topframe_center, bg=FRAME_BG).pack(pady=2)
exit_btn = tk.Button(topframe_right, text="Exit", bg=FRAME_BG, width=13, command=on_exit)
myname_label = tk.Label(topframe_center, text="Rensyl Quiroben", bg=FRAME_BG, font=("Tahoma", 28))
mycourse_label = tk.Label(topframe_center, text="Computer Science", bg=FRAME_BG, underline=1, font=("System", 28))
caption_label = tk.Label(topframe_center, text="Personal GUI", fg="blue", bg=FRAME_BG, font=("@System", 25))
python_label = tk.Label(logo_frame, image=python_logo, bg=FRAME_BG)
bootstrap_label = tk.Label(logo_frame, image=bootstrap_logo, bg=FRAME_BG)
sqlite_label = tk.Label(logo_frame, image=sqlite_logo, bg=FRAME_BG)
portfolio_btn = tk.Button(topframe_center, text="View Portfolio", bg="green", fg="yellow", width=15, command=show_portfolio)
name_label = tk.Label(bottomframe, text="enter your course", bg=FRAME_BG, font=("Arial", 15))
course_entry = tk.Entry(bottomframe, width=50)
course_entry.insert("end", "Computer Science")
course_entry.bind("<Return>", get_course_event)
submit_btn = tk.Button(bottomframe, text="Submit", bg="white", width=8, font=("Arial", 15), command=get_course)
course_label = tk.Label(bottomframe, text="", bg=FRAME_BG, font=("System", 20))

# PACK GEOMETRY MANAGER
topframe.pack(ipadx=WINDOW_WIDTH)
topframe_right.pack(pady=6, padx=5, anchor=tk.NE)
topframe_center.pack(anchor=tk.CENTER)
logo_frame.pack()
bottomframe.pack(ipadx=WINDOW_HEIGHT / 2)
exit_btn.pack(pady=5)
myname_label.pack()
mycourse_label.pack()
caption_label.pack()
python_label.pack(pady=10, side="left")
portfolio_btn.pack(pady=10)
name_label.pack(ipady=10, ipadx=100)
course_entry.pack(ipady=8)
submit_btn.pack(pady=8)
course_label.pack()


# Main event loop
if __name__ == "__main__":
	window.mainloop()
