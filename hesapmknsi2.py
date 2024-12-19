import tkinter as tk
import tkinter.font as tkFont

class CalculatorApp:
    def __init__(self, root):
        
        root.title("Hesap Makinesi")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        
        self.GLineEdit_185 = tk.Entry(root)
        self.GLineEdit_185["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_185["font"] = ft
        self.GLineEdit_185["fg"] = "#333333"
        self.GLineEdit_185["justify"] = "center"
        self.GLineEdit_185.insert(0, "0")
        self.GLineEdit_185.place(x=140, y=100, width=70, height=25)

      
        self.GLineEdit_392 = tk.Entry(root)
        self.GLineEdit_392["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_392["font"] = ft
        self.GLineEdit_392["fg"] = "#333333"
        self.GLineEdit_392["justify"] = "center"
        self.GLineEdit_392.insert(0, "0")
        self.GLineEdit_392.place(x=230, y=100, width=70, height=25)

        
        GLabel_700 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_700["font"] = ft
        GLabel_700["fg"] = "#333333"
        GLabel_700["justify"] = "center"
        GLabel_700["text"] = "Sayı 1"
        GLabel_700.place(x=130, y=60, width=70, height=25)

       
        GLabel_340 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_340["font"] = ft
        GLabel_340["fg"] = "#333333"
        GLabel_340["justify"] = "center"
        GLabel_340["text"] = "Sayı 2"
        GLabel_340.place(x=220, y=60, width=70, height=25)

        
        self.GLabel_395 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.GLabel_395["font"] = ft
        self.GLabel_395["fg"] = "#333333"
        self.GLabel_395["justify"] = "center"
        self.GLabel_395["text"] = "Sonuç"
        self.GLabel_395.place(x=320, y=60, width=70, height=25)

        
        self.result_label = tk.Label(root)
        self.result_label["font"] = ft
        self.result_label["fg"] = "#333333"
        self.result_label["justify"] = "center"
        self.result_label.place(x=320, y=100, width=70, height=25)

        
        self.create_button(root, "+", 90, 160, self.add)
        self.create_button(root, "-", 180, 160, self.subtract)
        self.create_button(root, "*", 270, 160, self.multiply)
        self.create_button(root, "/", 360, 160, self.divide)

    def create_button(self, root, text, x, y, command):
        button = tk.Button(root)
        button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button["font"] = ft
        button["fg"] = "#000000"
        button["justify"] = "center"
        button["text"] = text
        button.place(x=x, y=y, width=70, height=25)
        button["command"] = command

    def add(self):
        num1 = float(self.GLineEdit_185.get())
        num2 = float(self.GLineEdit_392.get())
        result = num1 + num2
        self.result_label["text"] = str(result)

    def subtract(self):
        num1 = float(self.GLineEdit_185.get())
        num2 = float(self.GLineEdit_392.get())
        result = num1 - num2
        self.result_label["text"] = str(result)

    def multiply(self):
        num1 = float(self.GLineEdit_185.get())
        num2 = float(self.GLineEdit_392.get())
        result = num1 * num2
        self.result_label["text"] = str(result)

    def divide(self):
        try:
            num1 = float(self.GLineEdit_185.get())
            num2 = float(self.GLineEdit_392.get())
            result = num1 / num2
            self.result_label["text"] = str(result)
        except ZeroDivisionError:
            self.result_label["text"] = "Hata!"

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
