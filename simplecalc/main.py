from tkinter import *
from tkinter import ttk

LAYOUT = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
]

CALC_SYMBOLS = ('+', '-', '*', '/', '**', '//')


class CalcApp(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.exp_list = ['0']
        self.create_style()
        self.create_widgets()

    def create_style(self):
        style = ttk.Style()
        style.configure(
            'TLabel', font=('Helvetica', 20),
            foreground='black'
        )
        style.configure('TButton', font=('Helvetica', 20))

    def create_widgets(self):
        # Initialize result area
        self.display_var = StringVar()
        self.display_var.set('0')

        # area displaying result
        display_label = ttk.Label(self, textvariable=self.display_var)
        display_label.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))

        # create layout
        for y, row in enumerate(LAYOUT, start=1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text=char)
                button.grid(column=x, row=y, sticky=(N, S, E, W))
                button.bind('<Button-1>', self.calc)
        self.grid(column=0, row=0, sticky=(N, S, E, W))

        # setting top widget position
        self.grid(column=0, row=0, sticky=(N, S, E, W))

        # expand column 1:1:1
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # expand row
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # expand top widget
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def calc(self, event):
        char = event.widget['text']

        last = self.exp_list[-1]

        if char == '=':
            if last in CALC_SYMBOLS:
                self.exp_list.pop()
            exp = eval(''.join(self.exp_list))
            self.exp_list = [str(exp)]

        elif char == 'C':
            self.exp_list = ['0']

        elif char in CALC_SYMBOLS:
            if last == char == '/':
                self.exp_list[-1] += '/'
            elif last == char == '*':
                self.exp_list[-1] += '*'
            elif last in CALC_SYMBOLS:
                self.exp_list[-1] = char
            else:
                self.exp_list.append(char)

        else:
            if last == '0':
                self.exp_list[-1] = char
            elif last in CALC_SYMBOLS:
                self.exp_list.append(char)
            else:
                self.exp_list[-1] += char



        self.display_var.set(' '.join(self.exp_list))


def main():
    root = Tk()
    root.title('Simple Calculator')
    CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()

