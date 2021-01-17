from tkinter import*
from tkinter import messagebox

def init(title="RM Calculator"):
    global problem
    root = Tk()
    root.geometry("250x320")
    root.title(title)

    root.resizable(width=False, height=False)
    problem = Entry(root,   font=("Helvetica", 40), width=10)
    problem.grid(row=0, column=0)
    problem.grid(columnspan=500)
    def equal():

        global problem
        result = problem.get()
    
            
        if "÷" in result:
            
            result = result.replace("÷", "/")

        if "×" in result:
            result = result.replace("×", "*")

        if "−" in result:
            result = result.replace("−", "-")

        
        try:
            result = eval(result)
            problem.delete(0, END)
            problem.insert(0, result)
        except:
            problem.delete(0, END)
            problem.insert(0, "Error")
    def clear():
        problem.delete(0,"end")
    def seven():
        problem.insert(END, "7")
    def four():
        problem.insert(END, "4")
    def one():
        problem.insert(END, "1")
    def zero():
        problem.insert(END, "0")
    def eight():
        problem.insert(END, "8")
    def five():
        problem.insert(END, "5")
    def two():
        problem.insert(END, "2")
    def nine():
        problem.insert(END, "9")
    def six():
        problem.insert(END, "6")
    def three():
        problem.insert(END, "3")
    def divide():
        problem.insert(END, "÷")
    def multiply():
        problem.insert(END, "×")
    def minus():
        problem.insert(END, "-")
    def plus():
        problem.insert(END, "+")
    def point():
        problem.insert(END, ".")



    clear = Button(root, text=" C ", command=clear,  font=("Helvetica", 40))
    clear.grid(row=1,column=0)
    seven = Button(root, text=" 7  ", command=seven,   font=("Helvetica", 40))
    seven.grid(row=2,column=0)
    four = Button(root, text=" 4  ", command=four,   font=("Helvetica", 40))
    four.grid(row=3,column=0)
    one = Button(root, text=" 1  ", command=one,   font=("Helvetica", 40))
    one.grid(row=4,column=0)

    eight = Button(root, text="  8  ", command=eight,   font=("Helvetica", 40))
    eight.grid(row=2,column=1)
    five = Button(root, text="  5  ", command=five,   font=("Helvetica", 40))
    five.grid(row=3,column=1)
    two = Button(root, text="  2  ", command=two,   font=("Helvetica", 40))
    two.grid(row=4,column=1)
    nine = Button(root, text=" 9 ", command=nine,   font=("Helvetica", 40))
    nine.grid(row=2,column=2)
    six = Button(root, text=" 6 ", command=six,   font=("Helvetica", 40))
    six.grid(row=3,column=2)
    three = Button(root, text=" 3 ", command=three,   font=("Helvetica", 40))
    three.grid(row=4,column=2)
    point = Button(root, text=" .  ", command=point,   font=("Helvetica", 40))
    point.grid(row=5,column=2)

    divide = Button(root, text=" ÷ ", command=divide,   font=("Helvetica", 40))
    divide.grid(row=1,column=3)
    multiply = Button(root, text=" × ", command=multiply,   font=("Helvetica", 40))
    multiply.grid(row=2,column=3)
    minus = Button(root, text=" − ", command=minus,   font=("Helvetica", 40))
    minus.grid(row=3,column=3)
    plus = Button(root, text=" + ", command=plus,   font=("Helvetica", 40))
    plus.grid(row=4,column=3)
    equal = Button(root, text=" = ", command=equal,   font=("Helvetica", 40))
    equal.grid(row=5,column=3)

    zero = Button(root, text="    0      ", command=zero,   font=("Helvetica", 40))
    zero.grid(row=5,column=0)
    zero.grid(columnspan=2)
    root.mainloop()

   

