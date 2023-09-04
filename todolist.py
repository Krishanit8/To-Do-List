from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from  tkinter import messagebox, simpledialog
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    win = tk.Tk()
    app = Todolist(win)
    win.mainloop()

class Todolist:
    def __init__(self,root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.resizable(0,0)
        self.root.wm_iconbitmap(resource_path('images\\icon.ico'))
        self.tasks = []

        # BACKGROUND IMG====
        img = Image.open(resource_path('images\\todo.jpg'))
        imgsize = img.resize((600,700))
        self.imgbg = ImageTk.PhotoImage(imgsize)

        img_lbl = Label(self.root, image=self.imgbg)
        img_lbl.pack()

        # ADD BTN===
        addimg = Image.open(resource_path('images\\add.jpeg'))
        addimgsize = addimg.resize((57, 57))
        self.addimgbg = ImageTk.PhotoImage(addimgsize)

        img_btn = Button(self.root, image=self.addimgbg,bg='white',border=0,command=self.add_task)
        img_btn.place(x=150, y=250)
        img_lbl = Button(self.root, text='ADD',bg='white',border=0,command=self.add_task)
        img_lbl.place(x=165, y=310)

        # UPDATE BTN ====
        Upimg = Image.open(resource_path('images\\update.jpg'))
        Upimgsize = Upimg.resize((58, 58))
        self.Upimgbg = ImageTk.PhotoImage(Upimgsize)

        img_btn1 = Button(self.root, image=self.Upimgbg,bg='white',border=0,command=self.edit_task)
        img_btn1.place(x=255, y=250)
        img_lbl1 = Button(self.root, text='Update', bg='white', border=0,command=self.edit_task)
        img_lbl1.place(x=263, y=310)

        # DELETE BTN =====
        delimg = Image.open(resource_path('images\\delete.png'))
        delimgsize = delimg.resize((54, 54))
        self.delimgbg = ImageTk.PhotoImage(delimgsize)

        img_btn2 = Button(self.root, image=self.delimgbg,bg='white',border=0,command=self.delete_task)
        img_btn2.place(x=360,y=250)
        img_lbl2 = Button(self.root, text='Delete', bg='white', border=0,command=self.delete_task)
        img_lbl2.place(x=370, y=310)

        self.entry = StringVar()
        self.entrybox = Entry(self.root,textvariable=self.entry,width=26,border=0,font=('Arial',18))
        self.entrybox.place(x=126,y=187,height=50)

        self.listbox = Listbox(self.root,width=24,border=0,background='white',font=('Arial Rounded MT Bold',18))
        self.listbox.place(x=130,y=348,height=245)

        self.load_tasks

        # FUNCTIONS======================

    def add_task(self):
        task_text = self.entrybox.get()
        if task_text.strip():
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.entrybox.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "Task cannot be empty!")

    def edit_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            selected_task = self.listbox.get(selected_task_index)
            edited_task_text = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task)
            # edited_task_text = selected_task.set(self.entry)
            if edited_task_text and edited_task_text.strip():
                self.tasks[selected_task_index] = edited_task_text
                self.update_task_listbox()


            elif edited_task_text == '':
                tk.messagebox.showwarning("Warning", "Task cannot be empty!")

            else:
                return
        else:
            tk.messagebox.showwarning("Warning", "No task selected for editing.")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def load_tasks(self):
        # You can implement saving/loading tasks to a file or database for persistence.
        # For simplicity, we will add some initial tasks as an example.
        self.tasks = ["Buy groceries", "Finish project", "Call mom"]
        self.update_task_listbox()


if __name__=='__main__':
     main()


