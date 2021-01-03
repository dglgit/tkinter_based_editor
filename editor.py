import tkinter as tk
import os
import keyword
import string
import time
class fkeypress:
    def __init__(self,ks):
        self.keysym=ks
        self.char=char
def get_whole_file(path):
    return ''.join(list(open(path,'r')))
def get_spaces(line):
    return line.count(' ')
def rsearch(s,target):
    idxs=[]
    start=0
    found=s.find(target)
    while found!=-1:
        idxs.append(found)
        found=s.find(target,idxs[-1]+1)
    return idxs
def search(string,word):
    idxs=[]
    #print(string,word)
    if string.count(word)==0:
        return []
    for i in range(len(string)-len(word)+1):
     #   print(string[i:i+len(word)],'dfnshfbshdb',string[i:i+len(word)]==word)
        if string[i:i+len(word)]==word:
            idxs.append(i)
    return idxs
def get_corresponding(line,target):
    for i in range(len(line)):
        if line[i]==target:
            return i
def relu(x):
    return 0 if x<0 else x
def to_num(x,num_type=int):
    return [num_type(i) for i in x]
class tab:
    def __init__(self,root,path,text):
        self.root=root
        self.nwin=tk.Toplevel(self.root)
        self.path=path
        self.label=tk.Label(self.nwin,text=self.path)
        self.label.grid()
        self.save_button=tk.Button(self.nwin,command=self.save,text='save')
        self.save_button.grid()
        self.main_field=tk.Text(self.nwin)
        self.main_field.insert('1.0',text)
        self.main_field.grid()
        
    def save(self):
        with open(self.path,'w') as f:
            f.write(self.main_field.get('1.0',tk.END))
class first:
    def __init__(self,root):
        self.root=root
        self.label=tk.Label(self.root,text='')
        #self.label.grid(column=0)
        self.path_box=tk.Entry(self.root)
        self.path_box.grid()
        self.button1=tk.Button(self.root,text='get stuff',command=lambda :self.display_file(self.path_box.get()))
        self.button1.grid()
        self.save_button=tk.Button(self.root,text='save',command=lambda: self.save())
        self.save_button.grid()
        self.main_field=tk.Text(width=100,height=40)
        self.main_height=40
        self.main_field.grid()
        self.dir_button=tk.Button
        '''self.resize_label=tk.Label(self.root,text='resize')
        self.resize_label.grid(row=5)
        self.new_shape=tk.Entry(self.root,width=10)
        self.new_shape.grid()
        self.resize_button=tk.Button(self.root,text='apply',command=lambda: self.resize(self.new_shape.get()))
        self.resize_button.grid(row=5)'''
        self.has_console=False
        self.run_button=tk.Button(self.root,text='run',command=self.run)
        self.run_button.grid(row=5)
        self.selbutton=tk.Button(self.root,text='sel',command=self.sel_text)
        self.selbutton.grid()
        self.main_field.bind('<Key>',self.press)
        self.main_field.bind('<Button-1>',self.leftclick)
        self.main_field.bind('<Return>',self.return_handle)
        self.just_written=''
        self.arrows=['Left','Right','Up','Down']
        self.scpos=None
        self.do=True
        self.kws=[i for i in keyword.kwlist]
        #del self.kws[self.kws.index('def')]
        self.tab_amount=2
        #self.begining_height=self.root.winfo.screenheight()
        #self.beginning_width=self.root.winfo.screenwidth()
        #self.root.bind("<Configure>", self.handle_config)
    def log(self,thing):
        if not self.has_console:
            print('go')
            self.console=tk.Text(width=50,height=20)
            self.console.insert(1.0,str(thing))
            print(tk.BOTTOM,type(tk.BOTTOM),tk.END,tk.LEFT)
            self.console.grid()
            self.has_console=True
            self.clear_console=tk.Button(text='clear_console',command=lambda: self.clear_console_)
            self.clear_console.grid()
        else:
            self.console.config(text=str(thing))
    def get_line(self,index):
        return self.main_field.get('1.0',tk.END).split('\n')[index]
    def clear_console_(self):
        self.console.forget()
        self.has_console=False
    def get_files(self,path):
        return list(os.listdir(path))
    def display_file(self,path):
        self.path=path
        if os.path.isdir(path):
            self.path_field=tk.Text(width=30)
            for i in os.listdir(path):
                self.path_field.insert('1.0',i+'\n')
            self.path_field.config(width=min(map(len,os.listdir(path)))+10)
            self.path_field.grid(row=3,column=2)
            self.new_button=tk.Button(text='new window',command=self.new_tab)
            self.new_button.grid(column=2,row=4)
            self.new_tab_path=tk.Entry()
            self.new_tab_path.grid(column=3,row=4)
        else:
            try:
                self.main_field.insert(1.0,get_whole_file(path))
            except Exception as e:
                print(e)
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
            self.log(e)
    def handle_config(self, event):
        print(self.root.geometry())
    def new_tab(self):
        n_tab=tab(self.root,self.new_tab_path.get(),self.main_field.get('1.0',tk.END))
    def sel_text(self):
        print('ghfbdshf')
        #self.main_field.tag_configure('thing',foreground='red')
        #self.main_field.tag_add('thing','1.0','1.3')
        print(self.main_field.search('yeet','1.0',tk.END),len(self.main_field.search('yeet','1.0',tk.END)))
        line=self.main_field.get(f'{2}.{0}',f'{2}.end')
        print(line)
        for i in range(len(line)-len('return')+1):
            print(line[i:i+len('return')],line[i:i+len('return')]=='return')
        self.highlight()
    def indent_no_line(self,idx,indent):
        print(self.cpos,'cpossssss')
    def return_handle(self,e):
        '''replaces standard func'''
        self.highlight()
        print('return')
        self.cpos=self.main_field.index(tk.INSERT)
        row,col=to_num(self.cpos.split('.'))
        self.acum_spaces=self.main_field.get(f'{row}.0',f'{row}.end').count(' ')
        print(self.main_field.index(tk.INSERT),self.acum_spaces,'acum')
        self.main_field.insert(self.cpos,' ')
        if 'def ' in self.main_field.get(f'{row}.0',f'{row}.end'):
            if len(self.main_field.get(f'{row+1}.0'))==0:
                #self.press(fkeypress('shift',''))
                print('no new line')
                self.indent_no_line(1,1)
                self.next_indent=' '*self.tab_amount+' '*self.acum_spaces
            print('inserting',f'{row+1}.0',self.main_field.get(f'{row+1}.0'))
            self.main_field.insert(f'{row+1}.0','g')#,' '*self.tab_amount+' '*self.acum_spaces)
        elif 'return ' in self.main_field.get(f'{row}.0',f'{row}.end'):
            print('2elif')
            if len(self.main_field.get(f'{row+1}.0'))==0:
                #self.press(fkeypress('shift',''))
                print('no new line')
                self.indent_no_line(1,1)
                self.next_indent=' '*relu(self.acum_spaces-self.tab_amount)
            else:
                self.main_field.insert(self.cpos,' '*relu(self.acum_spaces-self.tab_amount))
        else:
            print('else')
            if len(self.main_field.get(f'{row+1}.0'))==0:
                #self.press(fkeypress('shift',''))
                print('no new line')
                self.indent_no_line(1,1)
                self.next_indent=' '*self.acum_spaces
            else:
                self.main_field.insert(self.cpos,' '*self.acum_spaces)
    def press(self,e):
        #print(e)
        self.e=e
        if self.do:
            print(e,type(e),e.__class__)
            self.do=False
        self.cpos=self.main_field.index(tk.INSERT)#cursor pos
        row,col=to_num(self.cpos.split('.'))
        curr_line=self.main_field.get(f'{row}.{col}',f'{row}.end')
        whole_line=self.main_field.get(f'{row}.0',f'{row}.end')
        self.highlight2()
        if hasattr(self,'next_indent'):
            self.main_field.insert(f'{row}.{col}',self.next_indent)
            del self.next_indent
        if e.keysym=='parenleft' and 'def ' in whole_line:
            print('functype')
            self.main_field.tag_configure('func',foreground='purple')
            self.main_field.tag_add('func',self.scpos,self.cpos)
        if e.keysym not in self.arrows and e.keysym in string.printable:
            self.just_written+=e.char
        elif e.keysym=='BackSpace':
            self.just_written=self.just_written[:-1]#self.main_field.get(self.scpos,self.cpos)
            if not len(self.just_written):
                pass
        else:
            self.just_written=''
        print(self.just_written)
        self.acum_spaces=self.main_field.get(f'{row}.0',f'{row}.end').count(' ')
        print(e.keysym,'keysym, ',self.cpos,'cpos')
        if self.scpos is None or e.char==' ' or self.cpos[0]!=self.scpos[0]:
            self.just_written=''
            self.scpos=self.cpos
        if e.char=="'" or e.char=='"':
            print('quote',self.get_line(row),self.main_field.get('1.0',tk.END),self.main_field.get('1.0',tk.END).split('\n'))
            print("'" in self.get_line(row))
            #self.quote_highlight(self.get_line(row))
            '''
            print(string.printable)
            char_idxs=search(whole_line,e.char)
            print('char',char_idxs,'|',self.main_field.get('1.0',tk.END))
            if len(char_idxs)>1:
                for idx in range(0,len(char_idxs),2):
                    print(idx)
                    self.main_field.tag_configure('string',foreground='green')
                    self.main_field.tag_add('string',f'{row}.{char_idxs[idx]}',f'{row}.{char_idxs[idx+1]}')
            else:
                self.main_field.tag_configure('string',foreground='green')
                self.main_field.tag_add('string',f'{row}.{char_idxs[0]}',f'{row}.end')'''
        #print(e,e.x_root,e.y_root,e.x,e.y,e.state)
        #if e in string.ascii_letters:
         #   pass
    def press2(self,e):
        self.e=e
        self.cpos=self.main_field.index(tk.INSERT)#cursor pos
        row,col=to_num(self.cpos.split('.'))
        if e.char==' ' or e.keysym=='Return' or e.keysym=='BackSpace':
            self.highlight()
    def leftclick(self,e):
        #print(e)
        self.cpos=self.main_field.index(tk.INSERT)
        self.just_written=''
        self.scpos=self.cpos
    def highlight(self,line_num=None):
        if line_num is None:
            stop=len(self.main_field.get('1.0',tk.END).split('\n'))
            start=1
        else:
            stop=line_num
            start=line_num-1
        print(lines,'gsdggf')
        for i in range(start,stop):
            curr_idx=0
            line=self.main_field.get(f'{i}.{0}',f'{i}.end')
            print(line)
            #print(line)
            for kw in self.kws:
                if kw=='def':
                    print('oh no')
                idxs=search(line,kw)
                #print(idxs)
                for j in idxs:
                    self.main_field.tag_configure('thing',foreground='red')
                    self.main_field.tag_add('thing',f'{i}.{j}',f'{i}.{j+len(kw)}')
            if 'def ' in line:
                start=line.index(' ')+1
                stop=line.index('(')
                self.main_field.tag_configure('func',foreground='blue')
                self.main_field.tag_add('func',f'{i}.{start}',f'{i}.{stop}')
            for syn in ('""',"'"):
                idxs=search(line,syn)
                if idxs:
                    self.main_field.tag_configure('string',foreground='green')
                    if len(idxs)>1:
                        for ii in range(0,len(idxs),2):
                            print(idxs,idxs[ii],idxs[ii+1])
                            self.main_field.tag_add('string',f'{i}.{idxs[ii]}',f'{i}.{idxs[ii+1]+1}')
                    else:
                        self.main_field.tag_add('string',f'{i}.{idxs[0]}',f'{i}.end')
        
    def quote_highlight(self,line,qtype):
        idxs=search(line,qtype)
        if not idxs:
            self.main_field.insert()
            self.main_field.tag_configure('string',foreground='green')
            if len(idxs)>1:
                for ii in range(0,len(idxs),2):
                    self.main_field.tag_add('string',f'{i}.{idxs[ii]}',f'{i}.{idxs[ii+1]}')
                else:
                    self.main_field.tag_add('string',f'{i}.{idxs[0]}',f'{i}.end')
    def highlight2(self):
        r'''experimental'''
        if self.just_written in self.kws:
            #row,col=self.scpos.split('.')
            #stop=f'row.{col+(int(row)+len(self.just_written))/10}'
            print(self.just_written)
            self.main_field.tag_configure('thing',foreground='red')
            self.main_field.tag_add('thing',self.scpos,self.cpos)
        if self.just_written=='def' and self.e.char==' ':
            self.main_field.tag_configure('def',foreground='yellow')
            self.main_field.tag_add('def',self.scpos,self.cpos)
            
            
master=tk.Tk()
gui=first(master)
master.mainloop()
