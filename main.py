import random
# from tkinter import *
from tkinter import ttk, PhotoImage, Button, Label, Tk, Toplevel
from tkinter.ttk import *

from playsound import playsound

root = Tk()
root.title("Розвиваюча гра")
root.iconbitmap("icon.ico")
root.geometry("1000x600")
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.add(tab2, text="Вторая")


def no():
    playsound(r"Sounds\no_sound.wav")


def choose():
    playsound(r"Sounds\choose.wav")


def yes():
    playsound(r"Sounds\yes_sound.wav")


def first_last():
    playsound(r"Sounds\first-last.wav")


def oh_no():
    playsound(r"Sounds\oh_no.wav")


def kolobok():
    playsound(r"Sounds\kolobok.wav")

def kids():
    playsound(r"Sounds\kids.wav")

def boy_happy():
    playsound(r"Sounds\boy_happy.wav")

def girl_happy():
    playsound(r"Sounds\girl_happy.wav")

def boy_scared():
    playsound(r"Sounds\boy_scared.wav")

def boy_sad():
    playsound(r"Sounds\boy_sad.wav")

def boy_hat():
    playsound(r"Sounds\boy_hat.wav")

def girl_laught():
    playsound(r"Sounds\girl_laught.wav")

def girl_umbrella():
    playsound(r"Sounds\girl_umbrella.wav")

def one1():
    playsound(r"Sounds\one1.wav")

def one3():
    playsound(r"Sounds\one3.wav")
def one4():
    playsound(r"Sounds\one4.wav")
def one5():
    playsound(r"Sounds\one5.wav")
def one6():
    playsound(r"Sounds\one6.wav")
def one7():
    playsound(r"Sounds\one7.wav")
def one8():
    playsound(r"Sounds\one8.wav")
def one9():
    playsound(r"Sounds\one9.wav")
def one10():
    playsound(r"Sounds\one10.wav")

def two1():
    playsound(r"Sounds\two1.wav")
def two2():
    playsound(r"Sounds\two2.wav")
def two3():
    playsound(r"Sounds\two3.wav")
def two4():
    playsound(r"Sounds\two4.wav")
def two5():
    playsound(r"Sounds\two5.wav")
def two6():
    playsound(r"Sounds\two6.wav")
def two7():
    playsound(r"Sounds\two7.wav")
def two8():
    playsound(r"Sounds\two8.wav")
def two9():
    playsound(r"Sounds\two9.wav")
def two10():
    playsound(r"Sounds\two10.wav")

def three1():
    playsound(r"Sounds\three1.wav")
def three2():
    playsound(r"Sounds\three2.wav")
def three3():
    playsound(r"Sounds\three3.wav")
def three4():
    playsound(r"Sounds\three4.wav")
def three5():
    playsound(r"Sounds\three5.wav")
def three6():
    playsound(r"Sounds\three6.wav")
def three7():
    playsound(r"Sounds\three7.wav")
def three8():
    playsound(r"Sounds\three8.wav")
def three9():
    playsound(r"Sounds\three9.wav")
def three10():
    playsound(r"Sounds\three10.wav")

no1 = PhotoImage(file=r"Images\no1.png")
yes1 = PhotoImage(file=r"Images\yes1.png")
no2 = PhotoImage(file=r"Images\no2.png")
yes2 = PhotoImage(file=r"Images\yes2.png")
no3 = PhotoImage(file=r"Images\no3.png")
yes3 = PhotoImage(file=r"Images\yes3.png")
no4 = PhotoImage(file=r"Images\no4.png")
yes4 = PhotoImage(file=r"Images\yes4.png")
no5 = PhotoImage(file=r"Images\no5.png")
yes5 = PhotoImage(file=r"Images\yes5.png")
no6 = PhotoImage(file=r"Images\no6.png")
yes6 = PhotoImage(file=r"Images\yes6.png")
pos1_1 = PhotoImage(file=r"Images\pos1_1.png")
pos1_2 = PhotoImage(file=r"Images\pos1_2.png")
pos1_3 = PhotoImage(file=r"Images\pos1_3.png")
pos2_1 = PhotoImage(file=r"Images\pos2_1.png")
pos2_2 = PhotoImage(file=r"Images\pos2_2.png")
pos2_3 = PhotoImage(file=r"Images\pos2_3.png")
pos3_1 = PhotoImage(file=r"Images\pos3_1.png")
pos3_2 = PhotoImage(file=r"Images\pos3_2.png")
pos3_3 = PhotoImage(file=r"Images\pos3_3.png")
pos4_1 = PhotoImage(file=r"Images\pos4_1.png")
pos4_2 = PhotoImage(file=r"Images\pos4_2.png")
pos4_3 = PhotoImage(file=r"Images\pos4_3.png")
pos5_1 = PhotoImage(file=r"Images\pos5_1.png")
pos5_2 = PhotoImage(file=r"Images\pos5_2.png")
pos5_3 = PhotoImage(file=r"Images\pos5_3.png")
pos6_1 = PhotoImage(file=r"Images\pos6_1.png")
pos6_2 = PhotoImage(file=r"Images\pos6_2.png")
pos6_3 = PhotoImage(file=r"Images\pos6_3.png")
p1_1 = PhotoImage(file=r"Images\1_1.png")
p1_2 = PhotoImage(file=r"Images\1_2.png")
p1_3 = PhotoImage(file=r"Images\1_3.png")
p1_4 = PhotoImage(file=r"Images\1_4.png")
p2_1 = PhotoImage(file=r"Images\2_1.png")
p2_2 = PhotoImage(file=r"Images\2_2.png")
p2_3 = PhotoImage(file=r"Images\2_3.png")
p2_4 = PhotoImage(file=r"Images\2_4.png")
p3_1 = PhotoImage(file=r"Images\3_1.png")
p3_2 = PhotoImage(file=r"Images\3_2.png")
p3_3 = PhotoImage(file=r"Images\3_3.png")
p3_4 = PhotoImage(file=r"Images\3_4.png")
p4_1 = PhotoImage(file=r"Images\4_1.png")
p4_2 = PhotoImage(file=r"Images\4_2.png")
p4_3 = PhotoImage(file=r"Images\4_3.png")
p4_4 = PhotoImage(file=r"Images\4_4.png")
p5_1 = PhotoImage(file=r"Images\5_1.png")
p5_2 = PhotoImage(file=r"Images\5_2.png")
p5_3 = PhotoImage(file=r"Images\5_3.png")
p5_4 = PhotoImage(file=r"Images\5_4.png")
p6_1 = PhotoImage(file=r"Images\6_1.png")
p6_2 = PhotoImage(file=r"Images\6_2.png")
p6_3 = PhotoImage(file=r"Images\6_3.png")
p6_4 = PhotoImage(file=r"Images\6_4.png")
p7_1 = PhotoImage(file=r"Images\7_1.png")
p7_2 = PhotoImage(file=r"Images\7_2.png")
p7_3 = PhotoImage(file=r"Images\7_3.png")
p7_4 = PhotoImage(file=r"Images\7_4.png")
p8_1 = PhotoImage(file=r"Images\8_1.png")
p8_2 = PhotoImage(file=r"Images\8_2.png")
p8_3 = PhotoImage(file=r"Images\8_3.png")
p8_4 = PhotoImage(file=r"Images\8_4.png")
p9_1 = PhotoImage(file=r"Images\9_1.png")
p9_2 = PhotoImage(file=r"Images\9_2.png")
p9_3 = PhotoImage(file=r"Images\9_3.png")
p9_4 = PhotoImage(file=r"Images\9_4.png")
p10_1 = PhotoImage(file=r"Images\10_1.png")
p10_2 = PhotoImage(file=r"Images\10_2.png")
p10_3 = PhotoImage(file=r"Images\10_3.png")
p10_4 = PhotoImage(file=r"Images\10_4.png")
p11_1 = PhotoImage(file=r"Images\11_1.png")
p11_2 = PhotoImage(file=r"Images\11_2.png")
p11_3 = PhotoImage(file=r"Images\11_3.png")
p11_4 = PhotoImage(file=r"Images\11_4.png")
p12_1 = PhotoImage(file=r"Images\12_1.png")
p12_2 = PhotoImage(file=r"Images\12_2.png")
p12_3 = PhotoImage(file=r"Images\12_3.png")
p12_4 = PhotoImage(file=r"Images\12_4.png")
p13_1 = PhotoImage(file=r"Images\13_1.png")
p13_2 = PhotoImage(file=r"Images\13_2.png")
p13_3 = PhotoImage(file=r"Images\13_3.png")
p13_4 = PhotoImage(file=r"Images\13_4.png")
p14_1 = PhotoImage(file=r"Images\14_1.png")
p14_2 = PhotoImage(file=r"Images\14_2.png")
p14_3 = PhotoImage(file=r"Images\14_3.png")
p14_4 = PhotoImage(file=r"Images\14_4.png")
p15_1 = PhotoImage(file=r"Images\15_1.png")
p15_2 = PhotoImage(file=r"Images\15_2.png")
p15_3 = PhotoImage(file=r"Images\15_3.png")
p15_4 = PhotoImage(file=r"Images\15_4.png")
p16_1 = PhotoImage(file=r"Images\16_1.png")
p16_2 = PhotoImage(file=r"Images\16_2.png")
p16_3 = PhotoImage(file=r"Images\16_3.png")
p16_4 = PhotoImage(file=r"Images\16_4.png")
p17_1 = PhotoImage(file=r"Images\17_1.png")
p17_2 = PhotoImage(file=r"Images\17_2.png")
p17_3 = PhotoImage(file=r"Images\17_3.png")
p17_4 = PhotoImage(file=r"Images\17_4.png")
p18_1 = PhotoImage(file=r"Images\18_1.png")
p18_2 = PhotoImage(file=r"Images\18_2.png")
p18_3 = PhotoImage(file=r"Images\18_3.png")
p18_4 = PhotoImage(file=r"Images\18_4.png")
p19_1 = PhotoImage(file=r"Images\19_1.png")
p19_2 = PhotoImage(file=r"Images\19_2.png")
p19_3 = PhotoImage(file=r"Images\19_3.png")
p19_4 = PhotoImage(file=r"Images\19_4.png")
p20_1 = PhotoImage(file=r"Images\20_1.png")
p20_2 = PhotoImage(file=r"Images\20_2.png")
p20_3 = PhotoImage(file=r"Images\20_3.png")
p20_4 = PhotoImage(file=r"Images\20_4.png")
k1 = PhotoImage(file=r"Images\k1.png")
k2 = PhotoImage(file=r"Images\k2.png")
k3 = PhotoImage(file=r"Images\k3.png")
k4 = PhotoImage(file=r"Images\k4.png")
k5 = PhotoImage(file=r"Images\k5.png")
k6 = PhotoImage(file=r"Images\k6.png")
kr1 = PhotoImage(file=r"Images\kr1.png")
kr2 = PhotoImage(file=r"Images\kr2.png")
kr3 = PhotoImage(file=r"Images\kr3.png")
kr4 = PhotoImage(file=r"Images\kr4.png")
kr5 = PhotoImage(file=r"Images\kr5.png")
kr6 = PhotoImage(file=r"Images\kr6.png")
r1 = PhotoImage(file=r"Images\r1.png")
r2 = PhotoImage(file=r"Images\r2.png")
r3 = PhotoImage(file=r"Images\r3.png")
r4 = PhotoImage(file=r"Images\r4.png")
r5 = PhotoImage(file=r"Images\r5.png")
r6 = PhotoImage(file=r"Images\r6.png")
q1 = PhotoImage(file=r"Images\q1.png")
o1_1 = PhotoImage(file=r"Images\o1_1.png")
o1_2 = PhotoImage(file=r"Images\o1_2.png")
o1_3 = PhotoImage(file=r"Images\o1_3.png")
q2 = PhotoImage(file=r"Images\q2.png")
o2_1 = PhotoImage(file=r"Images\o2_1.png")
o2_2 = PhotoImage(file=r"Images\o2_2.png")
o2_3 = PhotoImage(file=r"Images\o2_3.png")
q3 = PhotoImage(file=r"Images\q3.png")
o3_1 = PhotoImage(file=r"Images\o3_1.png")
o3_2 = PhotoImage(file=r"Images\o3_2.png")
o3_3 = PhotoImage(file=r"Images\o3_3.png")
q4 = PhotoImage(file=r"Images\q4.png")
o4_1 = PhotoImage(file=r"Images\o4_1.png")
o4_2 = PhotoImage(file=r"Images\o4_2.png")
o4_3 = PhotoImage(file=r"Images\o4_3.png")
q5 = PhotoImage(file=r"Images\q5.png")
o5_1 = PhotoImage(file=r"Images\o5_1.png")
o5_2 = PhotoImage(file=r"Images\o5_2.png")
o5_3 = PhotoImage(file=r"Images\o5_3.png")
q6 = PhotoImage(file=r"Images\q6.png")
o6_1 = PhotoImage(file=r"Images\o6_1.png")
o6_2 = PhotoImage(file=r"Images\o6_2.png")
o6_3 = PhotoImage(file=r"Images\o6_3.png")
q7 = PhotoImage(file=r"Images\q7.png")
o7_1 = PhotoImage(file=r"Images\o7_1.png")
o7_2 = PhotoImage(file=r"Images\o7_2.png")
o7_3 = PhotoImage(file=r"Images\o7_3.png")
q8 = PhotoImage(file=r"Images\q8.png")
o8_1 = PhotoImage(file=r"Images\o8_1.png")
o8_2 = PhotoImage(file=r"Images\o8_2.png")
o8_3 = PhotoImage(file=r"Images\o8_3.png")
q9 = PhotoImage(file=r"Images\q9.png")
o9_1 = PhotoImage(file=r"Images\o9_1.png")
o9_2 = PhotoImage(file=r"Images\o9_2.png")
o9_3 = PhotoImage(file=r"Images\o9_3.png")
q10 = PhotoImage(file=r"Images\q10.png")
o10_1 = PhotoImage(file=r"Images\o10_1.png")
o10_2 = PhotoImage(file=r"Images\o10_2.png")
o10_3 = PhotoImage(file=r"Images\o10_3.png")
photo_fin = PhotoImage(file=r"Images\the_end.png")
t1 = "Чому хлопчик щасливий?"
t2 = "Чому дівчинка сміється?"
t3 = "Чому хлопчик сумний?"
t4 = "Чому хлопчик щасливий?"
t5 = "Чому хлопчик насить капелюх?"
t6 = "Чому дівчинка щаслива?"
t7 = "Чому хлопчик наляканий?"
t8 = "Чому діти носять теплі куртки?"
t9 = "Чому хлопчик наляканий?"
t10 = "Для чого дівчинці парасолька?"

def test5():
    quest_lib = [boy_happy, girl_laught, boy_sad, boy_happy, boy_hat, girl_happy, boy_scared, kids, boy_scared, girl_umbrella]
    text = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    dict_new = [o1_1, o1_2, o1_3, o2_1, o2_2, o2_3, o3_1, o3_2, o3_3, o4_1, o4_2, o4_3, o5_1, o5_2, o5_3, o6_1, o6_2, o6_3, o7_1, o7_2, o7_3, o8_1, o8_2, o8_3, o9_1, o9_2, o9_3, o10_1, o10_2, o10_3,]
    quest = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    sound_lib1 = [one1, one1, one3, one4, one5, one6, one7, one8, one9, one10]
    sound_lib2 = [two1, two2, two3, two4, two5, two6, two7, two8, two9, two10]
    sound_lib3 = [three1, three2, three3, three4, three5, three6, three7, three8, three9, three10]

    def right_choice():
        sound_lib3[reload.counter]()
        but_next.config(state='normal', command = lambda: [yes(), reload()])

    def reload():
        reload.counter += 1
        but_next.config(state='disabled')
        question.config(image="")
        lab.config(text="")
        if dict_new != []:
            for i in all_buttons:
                i.config(image="")
            randomise()
            insert_image()

        else:
            lab_fin.place(x=300, y=30, heigh=400, width=400)
            for but in all_buttons:
                but.destroy()
            lab.destroy()
            question.destroy()
            but_next.destroy()

    def randomise():
        arrange = [80, 200, 320]
        ran = random.sample(arrange, len(arrange))
        question.place(x=100, y=100, height=300, width=300)
        but1.place(x=500, y=ran[0], height=100, width=100)
        but2.place(x=500, y=ran[1], height=100, width=100)
        but3.place(x=500, y=ran[2], height=100, width=100)

    def insert_image():
        for j in all_buttons:
            if j.cget('image') == "":
                j.config(image=dict_new[0])
                dict_new.pop(0)
        if question.cget('image') == "":
            question.config(image=quest[0])
            quest.pop(0)
        if lab.cget('text') == "":
            lab.config(text=text[0])
            text.pop(0)


    def change_sound():
        quest_lib[reload.counter]()

    def wrong_choice1():
        sound_lib1[reload.counter]()
        but_next.config(state='normal', command = no)


    def wrong_choice2():
        sound_lib2[reload.counter]()
        but_next.config(state='normal', command = no)

    reload.counter = 0
    win = Toplevel(root)
    win.geometry("1010x600")
    win.title("Правильно/неправильно")
    lab_fin = Label(win, text="Кінець гри", image=photo_fin)
    lab = Button(win, text="", command="")
    lab.place(x=180, y=75)
    but_next = Button(win, text="Далі", state='disabled')
    question = Label(win, image="")
    but1 = Button(win, image="")
    but2 = Button(win, image="")
    but3 = Button(win, image="")
    all_buttons = [but1, but2, but3]
    but_next.place(x=700, y=200, height=100, width=100)
    insert_image()
    lab.config(command=lambda: change_sound())
    but1.config(command=lambda: wrong_choice1())
    but2.config(command=lambda: wrong_choice2())
    but3.config(command=lambda: right_choice())
    randomise()


def test1():
    dict_new = [no1, yes1, no2, yes2, no3, yes3, no4, yes4, no5, yes5, no6, yes6]

    def right_choice():
        yes()
        reload()



    def reload():
        if dict_new != []:
            for i in all_buttons:
                i.config(image="")
            randomise()
            insert_image()

        else:
            lab_fin.place(x=300, y=30, heigh=400, width=400)
            for but in all_buttons:
                but.destroy()
            lab.destroy()

    def randomise():
        arrange = [100, 400]
        ran = random.sample(arrange, len(arrange))
        but1.place(x=ran[0], y=80, height=220, width=220)
        but2.place(x=ran[1], y=80, height=220, width=220)

    def insert_image():
        for j in all_buttons:
            if j.cget('image') == "":
                j.config(image=dict_new[0])
                dict_new.pop(0)

    win = Toplevel(root)
    win.geometry("1010x600")
    win.title("Правильно/неправильно")
    lab_fin = Label(win, text="Кінець гри", image=photo_fin)
    lab = Button(win, text="Обери як правильно", command=choose)
    lab.place(x=300, y=30)
    but1 = Button(win, image="")
    but2 = Button(win, image="")
    all_buttons = [but1, but2]
    insert_image()
    but1.config(command=no)
    but2.config(command=lambda: right_choice())
    randomise()


def test2():
    dict_new = [p1_1, p1_2, p1_3, p1_4, p2_1, p2_2, p2_3, p2_4, p3_1, p3_2, p3_3, p3_4, p4_1, p4_2, p4_3, p4_4, p5_1,
                p5_2, p5_3, p5_4, p6_1, p6_2, p6_3, p6_4, p7_1, p7_2, p7_3, p7_4, p8_1, p8_2, p8_3, p8_4, p9_1, p9_2,
                p9_3, p9_4, p10_1, p10_2, p10_3, p10_4, p11_1, p11_2, p11_3, p11_4, p12_1, p12_2, p12_3, p12_4, p13_1,
                p13_2, p13_3, p13_4, p14_1, p14_2, p14_3, p14_4, p15_1, p15_2, p15_3, p15_4, p16_1, p16_2, p16_3, p16_4,
                p17_1, p17_2, p17_3, p17_4, p18_1, p18_2, p18_3, p18_4, p19_1, p19_2, p19_3, p19_4, p20_1, p20_2, p20_3,
                p20_4]

    def right_choice(b1, b2):
        def right_choice_last(b):
            yes()
            lab4.config(text="4", image=but4.cget('image'))
            b["state"] = "disabled"
            but_next.place(x=1030, y=250, height=100)

        right_choice.counter += 1
        if right_choice.counter == 1:
            yes()
            lab1.config(text="1", image=but1.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but2, but3))
        elif right_choice.counter == 2:
            yes()
            lab2.config(text="2", image=but2.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but3, but4))
        elif right_choice.counter == 3:
            yes()
            lab3.config(text="3", image=but3.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice_last(b2))

    def reload():
        if dict_new != []:
            for i in all_labels:
                i.config(image="", text="")
            for i in all_buttons:
                i.config(image="", state="active", command=oh_no)
            randomise()
            insert_image()
            right_choice.counter = 0
            but_next.place_forget()
            but1.config(command=lambda: right_choice(but1, but2))
        else:
            lab_fin.place(x=300, y=30, heigh=400, width=400)
            for but in all_buttons:
                but.destroy()
            for l in all_labels:
                l.destroy()
            lab.destroy()
            but_next.destroy()

    def insert_image():
        for j in all_buttons:
            if j.cget('image') == "":
                j.config(image=dict_new[0])
                dict_new.pop(0)

    def randomise():

        arrange = [50, 300, 550, 800]
        ran = random.sample(arrange, len(arrange))

        but1.place(x=ran[0], y=320, height=200, width=200)
        but2.place(x=ran[1], y=320, height=200, width=200)
        but3.place(x=ran[2], y=320, height=200, width=200)
        but4.place(x=ran[3], y=320, height=200, width=200)

    right_choice.counter = 0

    win = Toplevel(root)
    win.geometry("1100x600")
    win.title("Послідовності")
    lab_fin = Label(win, text="Кінець гри", image=photo_fin)
    lab = Button(win, text="Вибери, що йде спочатку, а що потім", command=first_last)
    lab.place(x=400, y=30)
    lab1 = Label(win, background="light gray")
    lab1.place(x=50, y=80, height=200, width=200)
    lab2 = Label(win, background="light gray")
    lab2.place(x=300, y=80, height=200, width=200)
    lab3 = Label(win, background="light gray")
    lab3.place(x=550, y=80, height=200, width=200)
    lab4 = Label(win, background="light gray")
    lab4.place(x=800, y=80, height=200, width=200)
    but1 = Button(win, text="1", image="")
    but2 = Button(win, text="2", image="", command=oh_no)
    but3 = Button(win, text="3", image="", command=oh_no)
    but4 = Button(win, text="4", image="", command=oh_no)
    all_labels = [lab1, lab2, lab3, lab4]
    all_buttons = [but1, but2, but3, but4]
    but_next = Button(win, text="Далі", command=lambda: reload())
    insert_image()
    but1.config(command=lambda: right_choice(but1, but2))
    randomise()


def test3():
    kol = [k1, k2, k3, k4, k5, k6, r1, r2, r3, r4, r5, r6, kr1, kr2, kr3, kr4, kr5, kr6]

    def right_choice(b1, b2):
        def right_choice_last(b):
            yes()
            lab6.config(text="6", image=but6.cget('image'))
            b["state"] = "disabled"
            but_next.place(x=1340, y=250, height=100)

        right_choice.counter += 1
        if right_choice.counter == 1:
            yes()
            lab1.config(text="1", image=but1.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but2, but3))
        elif right_choice.counter == 2:
            yes()
            lab2.config(text="2", image=but2.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but3, but4))
        elif right_choice.counter == 3:
            yes()
            lab3.config(text="3", image=but3.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but4, but5))
        elif right_choice.counter == 4:
            yes()
            lab4.config(text="4", image=but4.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but5, but6))
        elif right_choice.counter == 5:
            yes()
            lab5.config(text="5", image=but5.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice_last(b2))

    def reload():
        if kol != []:
            for i in all_labels:
                i.config(image="", text="")
            for i in all_buttons:
                i.config(image="", state="active", command=oh_no)
            randomise()
            insert_image()
            right_choice.counter = 0
            but_next.place_forget()
            but1.config(command=lambda: right_choice(but1, but2))
        else:
            lab_fin.place(x=300, y=30, heigh=400, width=400)
            for but in all_buttons:
                but.destroy()
            for l in all_labels:
                l.destroy()
            lab.destroy()
            but_next.destroy()

    def insert_image():
        for j in all_buttons:
            if j.cget('image') == "":
                j.config(image=kol[0])
                kol.pop(0)

    def randomise():

        arrange = [20, 240, 460, 680, 900, 1120]
        ran = random.sample(arrange, len(arrange))

        but1.place(x=ran[0], y=320, height=200, width=200)
        but2.place(x=ran[1], y=320, height=200, width=200)
        but3.place(x=ran[2], y=320, height=200, width=200)
        but4.place(x=ran[3], y=320, height=200, width=200)
        but5.place(x=ran[4], y=320, height=200, width=200)
        but6.place(x=ran[5], y=320, height=200, width=200)

    right_choice.counter = 0

    win = Toplevel(root)
    win.geometry("1100x600")
    win.title("Казки")
    lab_fin = Label(win, text="Кінець гри", image=photo_fin)
    lab = Button(win, text="Розкажи казку за картинками", command=kolobok)
    lab.place(x=600, y=30)
    lab1 = Label(win, background="light gray")
    lab1.place(x=20, y=80, height=200, width=200)
    lab2 = Label(win, background="light gray")
    lab2.place(x=240, y=80, height=200, width=200)
    lab3 = Label(win, background="light gray")
    lab3.place(x=460, y=80, height=200, width=200)
    lab4 = Label(win, background="light gray")
    lab4.place(x=680, y=80, height=200, width=200)
    lab5 = Label(win, background="light gray")
    lab5.place(x=900, y=80, height=200, width=200)
    lab6 = Label(win, background="light gray")
    lab6.place(x=1120, y=80, height=200, width=200)
    but1 = Button(win, text="1", image="")
    but2 = Button(win, text="2", image="", command=oh_no)
    but3 = Button(win, text="3", image="", command=oh_no)
    but4 = Button(win, text="4", image="", command=oh_no)
    but5 = Button(win, text="5", image="", command=oh_no)
    but6 = Button(win, text="6", image="", command=oh_no)
    all_labels = [lab1, lab2, lab3, lab4, lab5, lab6]
    all_buttons = [but1, but2, but3, but4, but5, but6]
    but_next = Button(win, text="Готово", command=lambda: reload())
    insert_image()
    but1.config(command=lambda: right_choice(but1, but2))
    randomise()


def test4():
    dict_new = [pos1_1, pos1_2, pos1_3, pos2_1, pos2_2, pos2_3, pos3_1, pos3_2, pos3_3, pos4_1, pos4_2, pos4_3, pos5_1,
                pos5_2, pos5_3, pos6_1, pos6_2, pos6_3]

    def right_choice(b1, b2):
        def right_choice_last(b):
            yes()
            lab3.config(text="3", image=but3.cget('image'))
            b["state"] = "disabled"
            but_next.place(x=800, y=250, height=100)

        right_choice.counter += 1
        if right_choice.counter == 1:
            yes()
            lab1.config(text="1", image=but1.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice(but2, but3))
        elif right_choice.counter == 2:
            yes()
            lab2.config(text="2", image=but2.cget('image'))
            b1["state"] = "disabled"
            b2.config(command=lambda: right_choice_last(b2))

    def reload():
        if dict_new != []:
            for i in all_labels:
                i.config(image="", text="")
            for i in all_buttons:
                i.config(image="", state="active", command=oh_no)
            randomise()
            insert_image()
            right_choice.counter = 0
            but_next.place_forget()
            but1.config(command=lambda: right_choice(but1, but2))
        else:
            lab_fin.place(x=300, y=30, heigh=400, width=400)
            for but in all_buttons:
                but.destroy()
            for l in all_labels:
                l.destroy()
            lab.destroy()
            but_next.destroy()

    def insert_image():
        for j in all_buttons:
            if j.cget('image') == "":
                j.config(image=dict_new[0])
                dict_new.pop(0)

    def randomise():

        arrange = [50, 300, 550]
        ran = random.sample(arrange, len(arrange))

        but1.place(x=ran[0], y=320, height=200, width=200)
        but2.place(x=ran[1], y=320, height=200, width=200)
        but3.place(x=ran[2], y=320, height=200, width=200)

    right_choice.counter = 0

    win = Toplevel(root)
    win.geometry("1100x600")
    win.title("Послідовності2")
    lab_fin = Label(win, text="Кінець гри", image=photo_fin)
    lab = Button(win, text="Вибери, що йде спочатку, а що потім", command=first_last)
    lab.place(x=300, y=30)
    lab1 = Label(win, background="light gray")
    lab1.place(x=50, y=80, height=200, width=200)
    lab2 = Label(win, background="light gray")
    lab2.place(x=300, y=80, height=200, width=200)
    lab3 = Label(win, background="light gray")
    lab3.place(x=550, y=80, height=200, width=200)
    but1 = Button(win, text="1", image="")
    but2 = Button(win, text="2", image="", command=oh_no)
    but3 = Button(win, text="3", image="", command=oh_no)
    all_labels = [lab1, lab2, lab3]
    all_buttons = [but1, but2, but3]
    but_next = Button(win, text="Далі", command=lambda: reload())
    insert_image()
    but1.config(command=lambda: right_choice(but1, but2))
    randomise()


Button(tab1, text="Правильно/неправильно", command=test1).place(x=100, y=50, height=50, width=150)
Button(tab1, text="Послідовності", command=test2).place(x=300, y=50, height=50, width=150)
button_test3 = Button(tab1, text="Казки", command=test3)
button_test3.place(x=100, y=150, height=50, width=150)
button_test4 = Button(tab1, text="Послідовності2", command=test4)
button_test4.place(x=300, y=150, height=50, width=150)
button_test5 = Button(tab1, text="Правильно/неправильно2", command=test5)
button_test5.place(x=100, y=250, height=50, width=150)

lbl1 = Label(tab1, text='Вкладка 1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
root.mainloop()
