from tkinter import *
from window import Window

def main():
    window = Tk()
    window.title("Finistra NIC0")
    myapp=Window(window)

    window.mainloop()

if __name__ == "__main__":
    main()