import tkinter as tk
from converter import converter
class main():
    def __init__(self):        

        def load():   
            decimal_number =self.entry.get()
            inst = converter()
            roman_number = tk.Label(self.root, text = inst.convert(decimal_number), font=('Aerial', '14'))
            roman_number.grid(row = 3, column = 0)

        def clear():
            label = tk.Label(self.root, text="                                                                                                                                                                  ")
            label.grid(row = 3, column = 0)    

        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.root.title("Decimal to roman number converter")
            
        self.label = tk.Label(self.root, text="Enter a decimal number greater than 0 and lesser than 4000", font=("Aerial", 12))
        self.label.grid(row = 0, column= 0)

        self.entry = tk.Entry(self.root, font = ("Aerial", 15))
        self.entry.grid(row = 1, column = 0)

        self.button = tk.Button(self.root, text = "Convert", command = load)
        self.button.grid(row = 2, column = 0)
       
        self.clear = tk.Button(self.root, text="Clear", command = clear)
        self.clear.grid(row = 4, column = 0)
       
        self.root.mainloop()

main()

    
