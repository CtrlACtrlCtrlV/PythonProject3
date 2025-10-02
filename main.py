import os
import tkinter as tk

def expand(s:str):
  for k in os.environ:
    s = s.replace("$" + k, os.environ[k])
  return s

def run_cmd():
    raw = expand(entry.get())
    text.insert(tk.END, f"vfs> {raw}\n")
    cmd, *args = raw.split()
    if cmd == "exit":
        root.destroy()
    if cmd == "ls":
        text.insert(tk.END, f"ls {args}\n")
    if cmd == "cd":
        text.insert(tk.END, f"cd {args}\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("vfs")
text = tk.Text(root, height=10, width=50)
text.pack()
entry = tk.Entry(root, width=50)
entry.pack()
entry.bind('<Return>', lambda e: run_cmd())
tk.Button(root, text="Run", command=run_cmd).pack()
root.mainloop()
