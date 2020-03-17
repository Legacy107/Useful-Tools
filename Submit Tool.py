#! python3
from tkinter import *
from datetime import *
import os, shelve, shutil

data = shelve.open('.\data\submitdata')
data.setdefault('dic', {})
data.setdefault('datemod', {})
data.setdefault('force', 0)
datemod = data['datemod']
dic = data['dic']


def move(s):
    top = Toplevel()
    top.title('Log')
    top.geometry('540x300+405+150')
    T = Text(top, width=60, height=20, font='consolas', fg='lime', bg='black')
    T.pack(side=LEFT)
    if (not os.path.exists(dic[s][0])) or (not os.access(dic[s][1], os.W_OK)):
        T.insert(END, 'Error: Invalid path')
        return
    flag = True
    for folderName, subfolders, filenames in os.walk(dic[s][0]):
        for filename in filenames:
            if filename.split('.')[1] == 'cpp' and filename[0]!='#':
                fullname = ' '.join({folderName, filename})  # get full file name
                ftime = os.path.getmtime(os.path.join(folderName, filename))  # last modify
                fdate = datetime.utcfromtimestamp(ftime).strftime('%d %m %Y')  # current date
                if data['force'] or datemod.get(fullname, 0) != ftime:
                    #print(str(ftime) + ' ' + str(datemod.get(fullname, 0)) + '\n') #debug
                    name = os.path.split(folderName)
                    shutil.copy(os.path.join(folderName, filename),
                                os.path.join(dic[s][1], name[len(name) - 1].split()[0] + '.cpp'))
                    T.insert(END, 'Copied' + folderName.replace('\\\\', '\\') + '.cpp\n')
                    datemod[fullname] = ftime  # last modification
                    flag = False
    #print(datemod)
    if flag:
        T.insert(END, 'Nothing to move')


def change(s, m1, m2):
    dic[s][0] = m1.get('1.0', END).replace('\\', '\\').strip()
    dic[s][1] = m2.get('1.0', END).replace('\\', '\\').strip()
    restart()


def delete(s):
    del (dic[s])
    restart()


def setforce():
    data['force'] ^= True


def add():
    dic[new.get()] = [NONE, NONE]
    restart()


def create():
    global main, new
    main = Tk()
    main.geometry('%sx%s+400+130' % (550, len(dic) * 75 + 65))
    main.title('Submit Tool (Copyright © 2019 by Legacy107)')
    main.config(bg='silver')
    main.focus_force()
    i = 0  # count
    for s in dic:
        # ------------- "move" button & path ---------------------
        action = lambda x=s: move(x)
        but1 = Button(main, text=s, width=10, height=3, bg='grey', fg='lime', command=action)
        but1.grid(row=i, column=0, sticky=W, pady=2)
        Label(main, text='From:', bg='lightgreen').grid(row=i, column=1, padx=5)
        Label(main, text='To:', bg='lightgreen').grid(row=i, column=3, padx=5)
        mes1 = Text(main, width=23, height=4)
        mes1.grid(row=i, column=2, pady=2)
        mes1.insert(END, dic[s][0].replace('\\\\', '\\'))
        mes2 = Text(main, width=23, height=4)
        mes2.grid(row=i, column=4, pady=2)
        mes2.insert(END, dic[s][1].replace('\\\\', '\\'))

        # ------------- delete & reload button ---------------------
        action1 = lambda x=s, m1=mes1, m2=mes2: change(x, m1, m2)
        action2 = lambda x=s: delete(x)
        but2 = Button(main, text='U', width=1, height=1, fg='yellow', bg='green', command=action1)
        but2.grid(row=i, column=0, sticky=E)
        but2 = Button(main, text='X', width=1, height=1, fg='yellow', bg='red', command=action2)
        but2.grid(row=i, column=0, sticky=W)

        i += 1

    # ------------- add button ---------------------
    but1 = Button(main, text='Add', width=10, height=2, bg='lightgreen', command=add)
    but1.grid(row=i, column=0, sticky=W, pady=2)
    new = Entry(main, width=15)
    new.grid(row=i, column=1, columnspan=2, sticky=W, padx=5)

    # ------------- force option ---------------------
    chVarDis = IntVar()
    checkforce = Checkbutton(main, text='Force Mode', fg='black', bg='orange', activeforeground='lightgreen',
                activebackground='orange', variable=chVarDis, command=setforce)
    if data['force']: checkforce.select()
    checkforce.grid(row=i, column=4, pady=20)
    #Label(main, text=str(data['force'])).grid(row=i, column=4, sticky=E)
    main.mainloop()


def restart():
    main.destroy()
    create()


###########---------main---------- ###############

create()
data['datemod'] = datemod
data['dic'] = dic
data.close()

##################################################
