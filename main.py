import tkinter as tk
from tkinter import messagebox
import sqlite3

from camera import start_camera
from database import init_db, add_user
from logs import create_log

init_db()

def register_user():

    window = tk.Toplevel(root)
    window.title("Register User")
    window.geometry("300x200")

    tk.Label(window,text="Enter user name").pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    def save():

        name = entry.get()

        if name == "":
            messagebox.showerror("Error","Enter a name")
            return

        add_user(name)

        messagebox.showinfo("Success",f"{name} registered")

        window.destroy()

    tk.Button(window,text="Save",command=save).pack(pady=20)


def view_logs():

    conn = sqlite3.connect("access_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT user,time,status,watermark FROM logs")

    rows = cursor.fetchall()

    conn.close()

    text = ""
    for row in rows:
        text += f"{row[0]} | {row[1]} | {row[2]} | {row[3]}\n"
    
    if text == "":
        text = "No logs found"

    messagebox.showinfo("Access Logs",text)


def demo_access():

    create_log("Eya","Authorized")

    messagebox.showinfo("Demo","Log created for user Eya")


root = tk.Tk()
root.title("Biometric Access Control System")
root.geometry("400x300")

title = tk.Label(root,text="Access Control System",font=("Arial",16))
title.pack(pady=20)

btn_camera = tk.Button(root,text="Start Camera",width=25,command=start_camera)
btn_camera.pack(pady=10)

btn_register = tk.Button(root,text="Register User",width=25,command=register_user)
btn_register.pack(pady=10)

btn_logs = tk.Button(root,text="View Logs",width=25,command=view_logs)
btn_logs.pack(pady=10)

btn_demo = tk.Button(root,text="Demo Access Log",width=25,command=demo_access)
btn_demo.pack(pady=10)

root.mainloop()