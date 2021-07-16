# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sneakers.api.utils as skutils
from sneakers.api.composer import Composer


def init_composer():
    tait = e1.get()
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    return True

def expand_composer():
    tait = e1.get()
    news = e2.get()
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    xc.expand_worksheet(int(news))
    return True

def upload_composer():
    tait = e1.get()
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    xc.upload_file()
    return True


def sync_composer():
    tait = e1.get()
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    global a
    url, a = xc.drive_flow_gui()
    #tk.Label(text=url).grid(row=10)
    global syncwindow
    syncwindow = tk.Toplevel(master)
    text = tk.Text(master=syncwindow, height=10, width=30)
    global e5
    e5 = tk.Entry(syncwindow)  # Write To
    e5.grid(row=14, column=12)
    text.grid(column=4, row=12)
    text.insert(tk.END, url)
    tk.Label(syncwindow, text="Code").grid(row=13)
    tk.Button(syncwindow,
              text='Send Code', command=sync_composer_code).grid(row=14,
                                                                 column=10,
                                                                 sticky=tk.W,
                                                                 pady=4)


    #xc.sync_flow_gui_code(cod, a)

    return True

def sync_composer_code():
    cod = e5.get()
    tait = e1.get()
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    xc.sync_worksheet(a, cod)
    tk.Label(syncwindow, text="Successfully Synced").grid(row=15, column=10)
    tk.Button(syncwindow,
              text='Quit',
              command=syncwindow.destroy).grid(row=20,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)


def write_composer(iny=10):
    tait = e1.get()
    frm = e3.get()
    tom = e4.get()
    newaddr = [int(frm),int(tom)]
    titl = skutils.composer_title('composer', tait)
    xc = Composer(titl)
    xc.write_wb_xl(newaddr,iny)
    return True


if __name__ == '__main__':
    import tkinter as tk

    master = tk.Tk()
    master.title("Sneakers Composer")
    tk.Label(master, text="Title").grid(row=0)
    tk.Label(master, text="Expand Size").grid(row=1)

    tk.Label(text="Write Options:").grid(row=2)
    tk.Label(master, text="From").grid(row=3)
    tk.Label(master, text="To").grid(row=4)


    e1 = tk.Entry(master) # Title
    e2 = tk.Entry(master) # Expand Size
    e3 = tk.Entry(master) # Write From
    e4 = tk.Entry(master)  # Write To


    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)





    # Buttons

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=20,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Init Composer', command=init_composer).grid(row=5,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)

    tk.Button(master,
              text='Expand', command=expand_composer).grid(row=6,
                                                                column=1,
                                                                sticky=tk.W,
                                                                pady=4)
    tk.Button(master,
              text='Write', command=write_composer).grid(row=7,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)
    tk.Button(master,
              text='Upload to Drive', command=upload_composer).grid(row=8,
                                                         column=1,
                                                         sticky=tk.W,
                                                         pady=4)
    tk.Button(master,
              text='Sync to Drive', command=sync_composer).grid(row=9,
                                                                    column=1,
                                                                    sticky=tk.W,
                                                                    pady=4)



    master.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
