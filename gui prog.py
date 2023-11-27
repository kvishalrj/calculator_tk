from tkinter import *
from subprocess import call
import time


root = Tk()
#button_9 = Button(label_key,text='9',height=3,width=5,font=('Helvetica','12'))
#button_9.grid(row=0,column=0)
class Calculator:
    def click_button(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self, event=None):
        self.entry.delete(0,END)
        self.operator =""

    ''' def delete(self):
        self.operator = str(self.entry.delete(len(self.entry.get())-1))
    '''

    def evaluate(self):
        self.answer =eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)

    def click_effect(self, l, text, text_c, bg_c, bd_c='black'):
        if bg_c=='white':
            l.create_oval(5, 5, 50, 50, outline = bd_c, fill = 'black', width = 4)
            l.create_text(27, 29, text=text, font=('Helvetica', '16', 'bold'), fill='white')
            root.update()
            time.sleep(0.2)  # Adjust the duration of the effect
            l.create_oval(5, 5, 50, 50, outline = bd_c, fill = bg_c, width = 4)
            l.create_text(27, 29, text=text, font=('Helvetica', '16', 'bold'), fill=text_c)
        else:
            l.create_oval(5, 5, 50, 50, outline = bd_c, fill = 'white', width = 4)
            l.create_text(27, 29, text=text, font=('Helvetica', '16', 'bold'), fill='black')
            root.update()
            time.sleep(0.2)  # Adjust the duration of the effect
            l.create_oval(5, 5, 50, 50, outline = bd_c, fill = bg_c, width = 4)
            l.create_text(27, 29, text=text, font=('Helvetica', '16', 'bold'), fill=text_c)


    def __init__(self,master):

        self.operator = ""        
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=45 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='black', fg='white',width=9,insertwidth=4,justify='right',font=('arial',40), bd=5)
        self.entry.pack()
        self.t = Text(self.entry,height=40)


        label_key = Label(root, height=15, width=30, bg='gold', bd=10)
        label_key.pack(expand=True)


        label_7 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_7.grid(row=1, column=0)
        label_7.create_oval(5, 5, 50, 50, fill = "black")
        label_7.create_text(27, 29, text='7', font=('Helvetica', '16', 'bold'), fill='white')
        label_7.bind('<Button-1>', lambda event: (self.click_button(7), self.click_effect(label_7, '7', 'white', 'black')))
        

        label_8 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_8.grid(row=1, column=1)
        label_8.create_oval(5, 5, 50, 50,fill = "black")
        label_8.create_text(27, 29, text='8', font=('Helvetica', '16', 'bold'), fill='white')
        label_8.bind('<Button-1>', lambda event: (self.click_button(8), self.click_effect(label_8, '8', 'white', 'black')))

        label_9 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_9.grid(row=1, column=2)
        label_9.create_oval(5, 5, 50, 50, fill = "black")
        label_9.create_text(27, 29, text='9', font=('Helvetica', '16', 'bold'), fill='white')
        label_9.bind('<Button-1>', lambda event: (self.click_button(9), self.click_effect(label_9, '9', 'white', 'black')))

        label_4 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_4.grid(row=2, column=0, padx=10, pady=10)
        label_4.create_oval(5, 5, 50, 50, fill = "black")
        label_4.create_text(27, 29, text='4', font=('Helvetica', '16', 'bold'), fill='white')
        label_4.bind('<Button-1>', lambda event: (self.click_button(4), self.click_effect(label_4, '4', 'white', 'black')))

        label_5 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_5.grid(row=2, column=1)
        label_5.create_oval(5, 5, 50, 50, fill = "black")
        label_5.create_text(27, 29, text='5', font=('Helvetica', '16', 'bold'), fill='white')
        label_5.bind('<Button-1>', lambda event: (self.click_button(5), self.click_effect(label_5, '5', 'white', 'black')))

        label_6 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_6.grid(row=2, column=2)
        label_6.create_oval(5, 5, 50, 50, fill = "black")
        label_6.create_text(27, 29, text='6', font=('Helvetica', '16', 'bold'), fill='white')
        label_6.bind('<Button-1>', lambda event: (self.click_button(6), self.click_effect(label_6, '6', 'white', 'black')))

        label_1 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_1.grid(row=3, column=0)
        label_1.create_oval(5, 5, 50, 50, fill = "black")
        label_1.create_text(27, 29, text='1', font=('Helvetica', '16', 'bold'), fill='white')
        label_1.bind('<Button-1>', lambda event: (self.click_button(1), self.click_effect(label_1, '1', 'white', 'black')))

        label_2 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_2.grid(row=3, column=1)
        label_2.create_oval(5, 5, 50, 50, fill = "black")
        label_2.create_text(27, 29, text='2', font=('Helvetica', '16', 'bold'), fill='white')
        label_2.bind('<Button-1>', lambda event: (self.click_button(2), self.click_effect(label_2, '2', 'white', 'black')))

        label_3 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_3.grid(row=3, column=2)
        label_3.create_oval(5, 5, 50, 50, fill = "black")
        label_3.create_text(27, 29, text='3', font=('Helvetica', '16', 'bold'), fill='white')
        label_3.bind('<Button-1>', lambda event: (self.click_button(3), self.click_effect(label_3, '3', 'white', 'black')))

        label_0 = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_0.grid(row=4, column=0, padx=10, pady=10)
        label_0.create_oval(5, 5, 50, 50,fill = "black")
        label_0.create_text(27, 29, text='0', font=('Helvetica', '16', 'bold'), fill='white')
        label_0.bind('<Button-1>', lambda event: (self.click_button(0), self.click_effect(label_0, '0', 'white', 'black')))

        label_deci = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_deci.grid(row=4, column=1)
        label_deci.create_oval(5, 5, 50, 50, fill = "black")
        label_deci.create_text(27, 25, text='.', font=('Helvetica', '16', 'bold'), fill='white')
        label_deci.bind('<Button-1>', lambda event: (self.click_button('.'), self.click_effect(label_deci, '.', 'white', 'black')))

        label_equal = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_equal.grid(row=4, column=2)
        label_equal.create_oval(5, 5, 50, 50, outline = "white", fill = "chocolate", width = 4)
        label_equal.create_text(27, 29, text='=', font=('Helvetica', '16', 'bold'), fill='white')
        label_equal.bind('<Button-1>', lambda event: (self.evaluate(), self.click_effect(label_equal, '=', 'white', 'chocolate', 'white')))


        label_C = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_C.grid(row=0, column=0, padx=10, pady=10)
        label_C.create_oval(5, 5, 50, 50, outline = "white", fill = "chocolate", width = 4)
        label_C.create_text(27, 29, text='C', font=('Helvetica', '16', 'bold'), fill='white')
        label_C.bind('<Button-1>', lambda event: (self.clear(), self.click_effect(label_C, 'C', 'white', 'chocolate', 'white')))

        '''label_del = Label(label_key, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()'''
        
        call(["python", "PySimpleGUIWeb\\PyGUI.py"])

        label_mod = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_mod.grid(row=0, column=3)
        label_mod.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_mod.create_text(27, 29, text='%', font=('Helvetica', '16', 'bold'), fill='black')
        label_mod.bind('<Button-1>', lambda event: (self.click_button('%'), self.click_effect(label_mod, '%', 'black', 'white')))

        label_div = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_div.grid(row=1, column=3)
        label_div.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_div.create_text(27, 29, text='/', font=('Helvetica', '16', 'bold'), fill='black')
        label_div.bind('<Button-1>', lambda event: (self.click_button('/'), self.click_effect(label_div, '/', 'black', 'white')))

        label_mul = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_mul.grid(row=2, column=3)
        label_mul.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_mul.create_text(27, 29, text='x', font=('Helvetica', '16', 'bold'), fill='black')
        label_mul.bind('<Button-1>', lambda event: (self.click_button('*'), self.click_effect(label_mul, 'x', 'black', 'white')))

        label_sub = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_sub.grid(row=3, column=3)
        label_sub.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_sub.create_text(27, 29, text='-', font=('Helvetica', '16', 'bold'), fill='black')
        label_sub.bind('<Button-1>', lambda event: (self.click_button('-'), self.click_effect(label_sub, '-', 'black', 'white')))

        label_add = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_add.grid(row=4, column=3)
        label_add.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_add.create_text(27, 29, text='+', font=('Helvetica', '16', 'bold'), fill='black')
        label_add.bind('<Button-1>', lambda event: (self.click_button('+'), self.click_effect(label_add, '+', 'black', 'white')))

        label_lbrace = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_lbrace.grid(row=0, column=1)
        label_lbrace.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_lbrace.create_text(27, 29, text='(', font=('Helvetica', '16', 'bold'), fill='black')
        label_lbrace.bind('<Button-1>', lambda event: (self.click_button('('), self.click_effect(label_lbrace, '(', 'black', 'white')))

        label_rbrace = Canvas(label_key, bg='gold', width=52, height=52, highlightthickness=0)
        label_rbrace.grid(row=0, column=2, padx=10, pady=10)
        label_rbrace.create_oval(5, 5, 50, 50, outline = "black", fill = "white", width = 4)
        label_rbrace.create_text(27, 29, text=')', font=('Helvetica', '16', 'bold'), fill='black')
        label_rbrace.bind('<Button-1>', lambda event: (self.click_button(')'), self.click_effect(label_rbrace, ')', 'black', 'white')))

c = Calculator(root)
root.title("Python Calculator Challenge")
root.mainloop()
