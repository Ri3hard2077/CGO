import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("CGO - Cyberpunk Graphics Optimizer")

    label = tk.Label(root, text="Welkom bij CGO", font=("Arial", 14))
    label.pack(pady=10)

    btn = tk.Button(root, text="Analyseer Mods", command=lambda: print("Analyse gestart..."))
    btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    launch_gui()