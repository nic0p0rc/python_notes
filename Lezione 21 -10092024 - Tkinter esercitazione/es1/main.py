from Application import Application
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Prova widget Tkinter")
    root.geometry("400x250+1350+450")
    myapp=Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()