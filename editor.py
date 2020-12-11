import tkinter as tk
import os

def get_whole_file(path):
    return ''.join(list(open(path,'r')))
    
class first:
    def __init__(self,root):
        self.root=root
        self.label=tk.Label(self.root,text='banana')
        #self.label.pack()
        self.path_box=tk.Entry(self.root)
        self.path_box.pack()
        self.button1=tk.Button(self.root,text='get stuff',command=lambda :self.display_file(self.path_box.get()))
        self.button1.pack()
        self.save_button=tk.Button(self.root,text='save',command=lambda: self.save())
        self.main_field=tk.Text(width=60,height=40)
        self.main_field.pack()
        self.resize_label=tk.Label(self.root,text='resize')
        self.resize_label.pack(side=tk.LEFT)
        self.new_shape=tk.Entry(self.root)
        self.new_shape.pack(side=tk.LEFT)
        self.resize_button=tk.Button(self.root,text='apply',command=lambda: self.resize(self.new_shape.get()))
        self.resize_button.pack(side=tk.LEFT)
        self.has_console=False
    def log(self,thing):
        if not self.has_console:
            print('go')
            self.console=tk.Text()
            self.console.insert(1.0,str(thing))
            print(tk.BOTTOM,type(tk.BOTTOM),tk.END,tk.LEFT)
            self.console.pack(side=tk.BOTTOM)
            self.has_console=True
            self.clear_console=tk.Button(text='clear_console',command=lambda: self.clear_console())
            self.clear_console.pack(side=tk.BOTTOM)
        else:
            self.console.config(text=str(thing))
    def clear_console(self):
        self.console.forget()
        self.has_console=False
    def get_files(self,path):
        return list(os.listdir(path))
    def display_file(self,path):
        self.main_field.insert(1.0,get_whole_file(path))
        #self.log(self.main_field.get(1.0,tk.END))
        self.path=path
    def save(self):
        with open(self.path,'w') as f:
            f.write(self.main_field.get(1.0,tk.END))
    def resize(self,new):
        width,height=new.split(',')
        self.main_field.config(width=int(width),height=int(height))
    def run(self):
        try:
            exec(self.main_field.get(1.0,tk.END).replace('print','self.log'))
        except Exception as e:
            log(e)

master=tk.Tk()
gui=first(master)
master.mainloop()