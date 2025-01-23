import tkinter as tk
class oop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Custom Tinker")
        self.create_layout()
    def create_layout(self):
        self.label = tk.Label(self, text="Hello, world!")
        self.label.pack()
        self.button = tk.Button(self, text="Click me!", command=self.click)
        self.button.pack(pady=10)
    def click(self):
        print("Button clicked!")
if __name__ == "__main__":
    app = oop()
    app.mainloop()
    
