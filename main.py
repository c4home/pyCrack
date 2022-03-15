# The programe to collect the information from all Step's folders
import csv
import os
import subprocess
from itertools import zip_longest as zip_longest
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def running(step, path):
    your_Step = 0
    crack_Front = []
    j_Integral = []
    k_Mode1 = []
    k_Mode2 = []
    k_Mode3 = []
    Da = []
    Dn = []
    step_increment = []
    for your_Step in range(int(step)+1):
        print(your_Step)
        localpath = path + "/step" + str(your_Step) + "/sifs-1.txt"
        f = open(localpath, "r")
        lines = f.readlines()[1:]
        for x in lines:
            your_Step += 0.001
            step_increment.append('% s' % (str(your_Step)))
            n = 0
            for word in x.split():
                if '.' in word and n == 1:
                    crack_Front.append(word)
                if '.' in word and n == 5:
                    j_Integral.append(word)
                if '.' in word and n == 6:
                    k_Mode1.append(word)
                if '.' in word and n == 7:
                    k_Mode2.append(word)
                if '.' in word and n == 8:
                    k_Mode3.append(word)
                n += 1
    for your_Step in range(int(step)):
        localpath = path + "/step" + str(your_Step) + "/InfoPropa.txt"
        f = open(localpath, "r")
        lines = f.readlines()[1:]
        for x in lines:
            n = 0
            for word in x.split():
                if '.' in word and n == 9:
                    Da.append(word)
                if '.' in word and n == 10:
                    Dn.append(word)
                n += 1
        f.close()

    # Guarante the data having the same dimension
    crack_Front = crack_Front[:len(step_increment)]
    j_Integral = j_Integral[:len(step_increment)]
    k_Mode1 = k_Mode1[:len(step_increment)]
    k_Mode2 = k_Mode2[:len(step_increment)]
    k_Mode3 = k_Mode3[:len(step_increment)]
    Da = Da[:len(step_increment)]
    Dn = Dn[:len(step_increment)]

    # Plot the graph
    # ax = plt.axes()
    # ax.plot(step_increment, k_Mode1, label=str(), color='g')
    # ax.yaxis.set_major_locator(plt.NullLocator())
    # ax.xaxis.set_major_locator(plt.MaxNLocator(int(step)))
    # ax.xaxis.set_major_formatter(plt.NullFormatter())
    # plt.show()

    # Draw K1 critical
    x_critical = [0.001, 0.002]
    y_critical = [1741, 1741]

    figure3 = plt.Figure(figsize=(5, 4), dpi=100)
    ax = plt.axes()
    ax.plot(x_critical, y_critical, color='r')
    ax.scatter(step_increment, k_Mode1, color='g')
    ax.legend(['K1'])
    ax.set_xlabel('Step')
    ax.set_title('Stress concentration factor K1')
    ax.yaxis.set_major_locator(plt.MaxNLocator(20))
    ax.xaxis.set_major_locator(plt.MaxNLocator(int(step)))
    plt.show()

    # figure3 = plt.Figure(figsize=(5, 4), dpi=100)
    #
    # ax3 = figure3.add_subplot(111)
    # ax3.scatter(step_increment, k_Mode1,label=str(), color='g')
    #
    # scatter3 = FigureCanvasTkAgg(figure3, root)
    # scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)
    # ax3.legend(['K1'])
    # ax3.set_xlabel('Step')
    # ax3.set_title('Stress concentration factor K1')

    # figure4 = plt.Figure(figsize=(5, 4), dpi=100)
    # ax4 = figure4.add_subplot(111)
    # ax4.scatter(step_increment, Da, color='r')
    # scatter4 = FigureCanvasTkAgg(figure4, root)
    # scatter4.get_tk_widget().pack(side=LEFT, fill=BOTH)
    # ax4.legend(['Da'])
    # ax4.set_xlabel('Step')
    # ax4.set_title('Increment Size Da')

    # Write data to the InfoAll
    # data = [step_increment, crack_Front, j_Integral, k_Mode1, k_Mode2, k_Mode3, Da, Dn]
    # export_data = zip_longest(*data, fillvalue='')
    # with open('InfoAll.csv', 'wb') as myfile:
    #     wr = csv.writer(myfile)
    #     wr.writerow(("Step", "Crack_Front", "J_Integral", "K_mode1", "K_mode2", "K_mode3", "Da", "Dn"))
    #     wr.writerows(export_data)


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def openFolder(url):
    subprocess.Popen('explorer %s' % url)


root = Tk()
root.eval('tk::PlaceWindow . center')
root.configure(background='white')
root.title('pyCrack')

frame = Frame(root, bg='white')
frame.pack(side=TOP, anchor=NW, fill='x')

step_var = StringVar()
path_var = StringVar()
Server_frame = Frame(frame, bd=0)
Server_frame.grid(row=0, column=1)

Folder_Adresse = Label(frame, text="Folder Adresse :   ", bg="white")
Folder_Adresse.grid(row=3, column=0, sticky='w')

f_Folder_Adresse = Entry(frame, width=80, textvariable=path_var)
f_Folder_Adresse.grid(row=3, column=1, sticky='w')

Step_label = Label(frame, text="Step Number :   ", bg="white")
Step_label.grid(row=0, column=0, sticky='w')

Step_Number_entry = Entry(frame, textvariable=step_var)
Step_Number_entry.grid(row=0, column=1, sticky='w')

open_btn = Button(frame, text="Go to Output Folder ", bg=rgb_hack((31, 127, 188)),
                  command=lambda: openFolder(os.getcwd()),
                  fg='white')
open_btn.grid(row=4, column=1, columnspan=10, pady=(5, 1))

run_btn = Button(frame, text="OK", bg=rgb_hack((31, 127, 188)),
                 command=lambda: running(step_var.get(), path_var.get()),
                 fg='white')
run_btn.grid(row=4, column=2, columnspan=10, pady=(5, 1))

frame.pack()

root.mainloop()
