from tkinter import *
import ctypes

solver = ctypes.CDLL("/Users/Demosthenix/JOJO/Jumble_Solver/resultsfile.so")
root = Tk()
root.title("Jumble Solver")
root.geometry('350x300')
root.resizable(False, False)

input_frame = Frame(root, height = 51, width = 300, background = 'yellow')
input_frame.pack(side = TOP, expand = False)

output_frame = Text(root, height = 249, width = 300, background = 'cyan')
output_frame.pack(side = BOTTOM, expand = False)

def reset():
	output_frame.delete(1.0, END)

inputstr_label = Label(input_frame, text = "Enter the Letters:", background = 'yellow').grid(row = 0)
word = StringVar()
input_string = Entry(input_frame, textvariable=word).grid(row = 0, column = 1);
def solve():
	s=bytes(str(word.get()),'ascii')
	solver.search(s)
	filename='results.txt'
	f = open(filename, 'r')
	output_frame.insert(END, f.read())


Button(input_frame, text = "Search", command=solve, background = 'yellow', pady = 0).grid(row = 1, column = 0)
Button(input_frame, text = "Reset", command=reset,background = 'yellow', pady = 0, bd = 0).grid(row = 1, column = 1)
Label(input_frame, text = "Click Search to get the words", background = 'yellow', wrap = 149).grid(row = 2, column = 0);
Label(input_frame, text = "Click Reset to clear output", background = 'yellow', wrap = 149).grid(row = 2, column = 1);
root.mainloop()
