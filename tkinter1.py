# biblioteka do aplikacji okienkowych
import tkinter


class MyGui:
    def __init__(self):  # konstrukor
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Witaj świecie')
        self.label2 = tkinter.Label(self.main_window, text='Python')
        self.label3 = tkinter.Label(self.main_window, text='góra')
        self.label4 = tkinter.Label(self.main_window, text='dół')

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')

        tkinter.mainloop()
        # dodoac 3 labelki z innym tekstem, umiescic bottom,right,top


my_gui = MyGui()
# python tkinter1.py
# pip install pyinstaller
# pyinstaller .\tkinter1.py
# pip freeze > requinments.txt
# pip install -r .\requinments.txt
