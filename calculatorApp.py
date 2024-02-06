from tkinter import *

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(background='light blue')
        self.root.title('Simple Calculator')
        self.root.geometry('270x150')
        
        self.expression = ""
        self.equation = StringVar()
        self.expression_field = Entry(self.root, textvariable=self.equation, justify='right')
        self.expression_field.grid(columnspan=4, ipadx=70)
        
        button1 = Button(root, text=' 1 ', fg='black', bg='#ADD8E6', 
                    command=lambda: self.press(1), height=1, width=8) 
        button1.grid(row=2, column=0) 
    
        button2 = Button(root, text=' 2 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(2), height=1, width=7) 
        button2.grid(row=2, column=1) 
    
        button3 = Button(root, text=' 3 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(3), height=1, width=7) 
        button3.grid(row=2, column=2) 
    
        button4 = Button(root, text=' 4 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(4), height=1, width=8) 
        button4.grid(row=3, column=0) 
    
        button5 = Button(root, text=' 5 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(5), height=1, width=7) 
        button5.grid(row=3, column=1) 
    
        button6 = Button(root, text=' 6 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(6), height=1, width=7) 
        button6.grid(row=3, column=2) 
    
        button7 = Button(root, text=' 7 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(7), height=1, width=8) 
        button7.grid(row=4, column=0) 
    
        button8 = Button(root, text=' 8 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(8), height=1, width=7) 
        button8.grid(row=4, column=1) 
    
        button9 = Button(root, text=' 9 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(9), height=1, width=7) 
        button9.grid(row=4, column=2) 
    
        button0 = Button(root, text=' 0 ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press(0), height=1, width=8) 
        button0.grid(row=5, column=0) 
    
        plus = Button(root, text=' + ', fg='black', bg='#ADD8E6', 
                    command=lambda: self.press("+"), height=1, width=8) 
        plus.grid(row=2, column=3) 
    
        minus = Button(root, text=' - ', fg='black', bg='#ADD8E6', 
                    command=lambda: self.press("-"), height=1, width=8)
        minus.grid(row=3, column=3) 
    
        multiply = Button(root, text=' * ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press("*"), height=1, width=8) 
        multiply.grid(row=4, column=3) 
    
        divide = Button(root, text=' / ', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press("/"), height=1, width=8) 
        divide.grid(row=5, column=3) 
    
        equal = Button(root, text=' = ', fg='black', bg='#ADD8E6', 
                    command=self.equalpress, height=1, width=7) 
        equal.grid(row=5, column=2) 
    
        clear = Button(root, text='Clear', fg='black', bg='#ADD8E6', 
                    command=self.clear, height=1, width=7) 
        clear.grid(row=5, column='1') 
    
        Decimal= Button(root, text='.', fg='black', bg='#ADD8E6', 
                        command=lambda: self.press('.'), height=1, width=8) 
        Decimal.grid(row=6, column=0) 
        
        self.sqrt = Button(root,  text='√',  fg='black',  bg='#ADD8E6', 
                        command=self.press_sqrt, height=1,  width=8) 
        self.sqrt.grid(row=6,  column=3)
    
    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)
    
    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set("Error")
            self.expression = ""

    def press_sqrt(self):
        try:
            result = eval(self.expression) ** 0.5
            self.equation.set(result)
        except ValueError:
            self.equation.set("Error")
        self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.equation.set('')
        
root = Tk()
calculator = CalculatorApp(root)
root.mainloop()