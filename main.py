import tkinter
import tkinter.messagebox

class GUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('360x250')
        self.main_window.title("Pizza Cost")

        # create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.btm_frame = tkinter.Frame(self.main_window)
        self.btn_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top', fill='x')
        self.mid_frame.pack(side='top', fill='x')
        self.btm_frame.pack(side='top', fill='x')
        self.btn_frame.pack(side='top')

        self.top_frame.configure(background='blue')
        self.btn_frame.configure(background='red')

        # create labels
        self.lbl1 = tkinter.Label(self.top_frame, text='Name Your Pizza:')
        self.lbl2 = tkinter.Label(self.mid_frame, text='Pick your toppings:')
        self.lbl3 = tkinter.Label(self.btm_frame, text='Pick your crust:')

        self.lbl1.pack(side='left')
        self.lbl2.pack(side='top', fill='x')
        self.lbl3.pack(side='top', fill='x')

        self.lbl1.configure(background='blue', font='arial', fg='white')
        self.lbl2.configure(background='red', font='arial', fg='white')
        self.lbl3.configure(background='red', font='arial', fg='white')

        # create input box
        self.input_box = tkinter.Entry(self.top_frame, width=25)

        self.input_box.pack(side='left')

        self.input_box.configure(background='white', font='arial', fg='black')

        # create buttons
        self.button = tkinter.Button(self.btn_frame, text='Create Pizza', command= self.create_pizza)
        self.quit_btn = tkinter.Button(self.btn_frame, text='Quit', command=self.main_window.destroy)

        self.button.pack(side='left')
        self.quit_btn.pack(side='left')

        # create radio buttons
        self.rb_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.btm_frame, text='Thin Crust $1', variable=self.rb_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.btm_frame, text='Thick Crust $2', variable=self.rb_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.btm_frame, text='Cheese Crust $3', variable=self.rb_var, value=3)

        self.rb1.pack(side='top')
        self.rb2.pack(side='top')
        self.rb3.pack(side='top')

        # create check boxes
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.mid_frame, text='Pepperoni $1.50', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.mid_frame, text='Sausage $1.75', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.mid_frame, text='Pineapple $3.25', variable=self.cb_var3)

        self.cb1.pack(side='top')
        self.cb2.pack(side='top')
        self.cb3.pack(side='top')

        tkinter.mainloop()

    def create_pizza(self):
        name = self.input_box.get()

        price = 8.0
        price += float(self.rb_var.get())

        if self.cb_var1.get():
            price += 1.5
        if self.cb_var2.get():
            price += 1.75
        if self.cb_var3.get():
            price += 3.25

        tkinter.messagebox.showinfo("Your Pizza", name + '\n\tThis pizza costs: ' + "${:,.2f}".format(price))

def main():
    gui = GUI()

main()
