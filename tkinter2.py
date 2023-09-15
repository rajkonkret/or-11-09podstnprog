import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_505 = tk.Button(root)
        GButton_505["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_505["font"] = ft
        GButton_505["fg"] = "#000000"
        GButton_505["justify"] = "center"
        GButton_505["text"] = "Button"
        GButton_505.place(x=0, y=80, width=70, height=25)
        GButton_505["command"] = self.GButton_505_command

        GLabel_63 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_63["font"] = ft
        GLabel_63["fg"] = "#333333"
        GLabel_63["justify"] = "center"
        GLabel_63["text"] = "label"
        GLabel_63.place(x=230, y=130, width=70, height=25)

        GCheckBox_950 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_950["font"] = ft
        GCheckBox_950["fg"] = "#333333"
        GCheckBox_950["justify"] = "center"
        GCheckBox_950["text"] = "CheckBox"
        GCheckBox_950.place(x=90, y=230, width=70, height=25)
        GCheckBox_950["offvalue"] = "0"
        GCheckBox_950["onvalue"] = "1"
        GCheckBox_950["command"] = self.GCheckBox_950_command

        GRadio_842 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_842["font"] = ft
        GRadio_842["fg"] = "#333333"
        GRadio_842["justify"] = "center"
        GRadio_842["text"] = "RadioButton"
        GRadio_842.place(x=240, y=280, width=85, height=25)
        GRadio_842["command"] = self.GRadio_842_command

        GLineEdit_318 = tk.Entry(root)
        GLineEdit_318["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_318["font"] = ft
        GLineEdit_318["fg"] = "#333333"
        GLineEdit_318["justify"] = "center"
        GLineEdit_318["text"] = "Entry"
        GLineEdit_318.place(x=90, y=70, width=145, height=129)

        GListBox_484 = tk.Listbox(root)
        GListBox_484["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_484["font"] = ft
        GListBox_484["fg"] = "#333333"
        GListBox_484["justify"] = "center"
        GListBox_484.place(x=340, y=120, width=80, height=25)

    def GButton_505_command(self):
        print("command")

    def GCheckBox_950_command(self):
        print("command")

    def GRadio_842_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
