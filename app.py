import tkinter as tk
import numpy as np
import os
from tkinter.messagebox import showerror

class CustomError(Exception):
    pass

root = tk.Tk()
root.title("setting initial conditions")
root.minsize(1020, 450)
root.geometry("1020x450+450+50")
tk.Label(root, text ='Setting initial conditions and processing', font=("Comic Sans", 10, "bold")).pack()
#making frame for setting numerical values
frame = tk.Frame(root, width=530, height=320)
frame.configure(background="grey")
tk.Label(frame, text ='Setting numeric values', bg="grey", font=("Comic Sans", 8, "bold")).place(x=150, y=5)
frame.place(x=15, y= 40)
#making frame for processing settings
frame2 = tk.Frame(root, width=450, height=320)
frame2.configure(background="grey")
tk.Label(frame2, text =' Processing setup', bg="grey", font=("Comic Sans", 8, "bold")).place(x=130, y=5)
frame2.place(x=550, y= 40)
#making textfields and labels for setting boundary values and other numeric values
tmin_lb = tk.Label(frame, text='t min [s]', bg="grey")
tmin_lb.place(x=125, y=50)

tmax_lb = tk.Label(frame, text='t max [s]', bg="grey")
tmax_lb.place(x=125, y=80)

tmin_tf = tk.Entry(frame, width=10)
tmin_tf.place(x=40, y=50)

tmax_tf = tk.Entry(frame, width=10)
tmax_tf.place(x=40, y=80)

xmin_lb = tk.Label(frame, text='x min [m]', bg="grey")
xmin_lb.place(x=125, y=110)

xmax_lb = tk.Label(frame, text='x max [m]', bg="grey")
xmax_lb.place(x=125, y=140)

xmin_tf = tk.Entry(frame, width=10)
xmin_tf.place(x=40, y=110)

xmax_tf = tk.Entry(frame, width=10)
xmax_tf.place(x=40, y=140)

ymin_lb = tk.Label(frame, text='y min [m]', bg="grey")
ymin_lb.place(x=125, y=170)

ymax_lb = tk.Label(frame, text='y max [m]', bg="grey")
ymax_lb.place(x=125, y=200)

ymin_tf = tk.Entry(frame, width=10)
ymin_tf.place(x=40, y=170)

ymax_tf = tk.Entry(frame, width=10)
ymax_tf.place(x=40, y=200)

zmin_lb = tk.Label(frame, text='z min [m]', bg="grey")
zmin_lb.place(x=125, y=230)

zmax_lb = tk.Label(frame, text='z max [m]', bg="grey")
zmax_lb.place(x=125, y=260)

zmin_tf = tk.Entry(frame, width=10)
zmin_tf.place(x=40, y=230)

zmax_tf = tk.Entry(frame, width=10)
zmax_tf.place(x=40, y=260)

fps_lb = tk.Label(frame, text='Frames per second', bg="grey")
fps_lb.place(x=335, y=50)

fps_tf = tk.Entry(frame, width=10)
fps_tf.place(x=250, y=50)

Nx_lb = tk.Label(frame, text='Mesh grid number for x', bg="grey")
Nx_lb.place(x=335, y=80)

Nx_tf = tk.Entry(frame, width=10)
Nx_tf.place(x=250, y=80)

Ny_lb = tk.Label(frame, text='Mesh grid number for y', bg="grey")
Ny_lb.place(x=335, y=110)

Ny_tf = tk.Entry(frame, width=10)
Ny_tf.place(x=250, y=110)

g_lb = tk.Label(frame, text='Gravitational acceleration [m/s^2]', bg="grey")
g_lb.place(x=335, y=140)

g_tf = tk.Entry(frame, width=10)
g_tf.place(x=250, y=140)

#making processing settings
#setting static plot
stt_lb = tk.Label(frame2, text='Exact time', bg="grey")
stt_lb.place(x=100, y=120)
stt_tf = tk.Entry(frame2, width=10)
stt_tf.place(x=15, y=120)
#setting static quiver plot
sttq_lb = tk.Label(frame2, text='Exact time', bg="grey")
sttq_lb.place(x=100, y=210)
sttq_tf = tk.Entry(frame2, width=10)
sttq_tf.place(x=15, y=210)
#saving static plot
def stat():
    if stb.get():
        stat.configure(text="Save static quiver plot: Yes")
    else:
        stat.configure(text="Save static quiver plot: No")
stb = tk.BooleanVar()
stat = tk.Checkbutton(
    frame2,
    text="Save static quiver plot: No",
    command=stat,
    variable=stb,
    bg="grey",
)
stat.place(x=15, y=90)

#saving static quiver plot
def statq():
    if stbq.get():
       statq.configure(text="Save static quiver plot: Yes")
    else:
        statq.configure(text="Save static quiver plot: No")

stbq = tk.BooleanVar()
statq = tk.Checkbutton(
    frame2,
    text="Save static quiver plot: No",
    command=statq,
    variable=stbq,
    bg="grey",
)
statq.place(x=15, y=180)
#quiver plot
def quiv():
    if quivb.get():
        quivcheck.configure(text="Save quiver animation: Yes")
    else:
        quivcheck.configure(text="Save quiver animation: No")

quivb = tk.BooleanVar()
quivcheck = tk.Checkbutton(
    frame2,
    text="Save quiver animation:No",
    command=quiv,
    variable=quivb,
    bg="grey",
)
quivcheck.place(x=15, y=150)

#enable or disable output
def outpt():
    if outptb.get():
        outptcheck.configure(text='Output enabled')
    else:
        outptcheck.configure(text='Output disbled')


outptb = tk.BooleanVar()
outptcheck = tk.Checkbutton(
    frame2,
    text="Output disabled",
    command=outpt,
    variable=outptb,
    bg="grey",
)
outptcheck.place(x=15, y=60)

#checkbox for animated plot of water level
def wtrlv():
    if wtrlvb.get():
        wtrlvcheck.configure(text="Animated plot for water level:Yes")
    else:
        wtrlvcheck.configure(text="Animated plot for water level:No")


wtrlvb = tk.BooleanVar()
wtrlvcheck = tk.Checkbutton(
    frame2,
    text="Animated plot for water level:No",
    command=wtrlv,
    variable=wtrlvb,
    bg="grey",
)
wtrlvcheck.place(x=15, y=240)
# making checkboxes for borders b-border
#xmin 
def bxmin():
    if xminb.get():
        xmincheck.configure(text='x=xmin: Wall')
    else:
        xmincheck.configure(text='x=xmin: Extrap')


xminb = tk.BooleanVar()
xmincheck = tk.Checkbutton(
    frame2,
    text="x=xmin: Extrap",
    command=bxmin,
    variable=xminb,
    bg="grey",
)
xmincheck.place(x=250, y=60)
#xmax
def bxmax():
    if xmaxb.get():
        xmaxcheck.configure(text='x=xmax: Wall')
    else:
        xmaxcheck.configure(text='x=xmax: Extrap')


xmaxb = tk.BooleanVar()
xmaxcheck = tk.Checkbutton(
    frame2,
    text="x=xmax: Extrap",
    command=bxmax,
    variable=xmaxb,
    bg="grey",
)
xmaxcheck.place(x=250, y=90)

#ymin 
def bymin():
    if yminb.get():
        ymincheck.configure(text='y=ymin: Wall')
    else:
        ymincheck.configure(text='y=ymin: Extrap')


yminb = tk.BooleanVar()
ymincheck = tk.Checkbutton(
    frame2,
    text="y=ymin: Extrap",
    command=bymin,
    variable=yminb,
    bg="grey",
)
ymincheck.place(x=250, y=120)
#ymax 
def bymax():
    if ymaxb.get():
        ymaxcheck.configure(text='y=ymax: Wall')
    else:
        ymaxcheck.configure(text='y=ymax: Extrap')


ymaxb = tk.BooleanVar()
ymaxcheck = tk.Checkbutton(
    frame2,
    text="y=ymax: Extrap",
    command=bymax,
    variable=ymaxb,
    bg="grey",
)
ymaxcheck.place(x=250, y=150)


#defining functions that submit inserted values
def submit_lim(mins, maxs, min_lb, max_lb):
    try:
        minv=float(mins)
        maxv=float(maxs)
        if maxv>minv:
            return np.array([minv,maxv])
        else:
            raise ValueError
    except ValueError:
        try:
            minv = float(mins)
            maxv = float(maxs)
            showerror(title="Error", message=f'Minimal value {min_lb} must be greater than maximal value {max_lb}')
        except ValueError:
            showerror(title="Error", message=f'Textfields {min_lb} and {max_lb} must be convertible to float')

def submit_valuef(value_s, value_lb):
    try:
        value_v=float(value_s)
        if value_v<0:
            raise ValueError
        else:
            return value_v
    except ValueError:
        try:
            value_v=float(value_s)
            showerror(title="Error", message=f'{value_lb} value must be positive')
        except ValueError:
            showerror(title="Error", message=f'Textfield {value_lb}  must be convertible to float')

def submit_valuei(value_s, value_lb):
    try:
        value_v=int(value_s)
        if value_v<0:
            raise ValueError
        else:
            return value_v
    except ValueError:
        try:
            value_v=float(value_s)
            showerror(title="Error", message=f'{value_lb} value must be positive')
        except ValueError:
            showerror(title="Error", message=f'Textfield {value_lb}  must be convertible to integer')

def submit():
    test_a=False #testing if file with initial conditions exists in work directory
    test_b=False
    test_c=False
    try:
        init_test = open('uinit.py', 'r')
        init_test.close()
        test_a=True
    except FileNotFoundError:
        showerror(title="Error", message='There is no file setting initial conditions in work directory')
    if test_a:
        try:
            from uinit import init
            test_b=True
        except ImportError:
            showerror(title="Error", message='There is no init function in initial conditions file')
    if test_b:
        try:
            init(0,0)
            test_c=True
        except TypeError:
            showerror(title="Error", message='Function from initial condition file must have 2 arguments')
    if test_c:
        try:
            init(0,0)
        except Exception:
            showerror(title="Error", message='Something went wrong with function from initial condition file')
    

            TypeError
    tlim = submit_lim(tmin_tf.get(), tmax_tf.get(), 't min', 't max')
    xlim = submit_lim(xmin_tf.get(), xmax_tf.get(), 'x min', 'x max')
    ylim = submit_lim(ymin_tf.get(), ymax_tf.get(), 'y min', 'y max')
    zlim = submit_lim(zmin_tf.get(), zmax_tf.get(), 'y min', 'y max')
    fps = submit_valuei(fps_tf.get(), 'Frames per second')
    nx = submit_valuei(Nx_tf.get(), 'Meshgrid number for x')
    ny = submit_valuei(Ny_tf.get(), 'Meshgrid number for y')
    g = submit_valuef(g_tf.get(), 'Gravitational accceleration')

    if stb.get():
        stat_time = submit_valuef(stt_tf.get(),'Exact time of static plot')
    if quivb.get():#use for future quiver animation

        if stbq.get():
            statq_time = submit_valuef(sttq_tf.get(), 'Exact time of static quiver plot')
    if outptb.get():
        pass 

    if wtrlvb.get():
        pass 
    #bool values for borders
    xminbool=xminb.get()
    xmaxbool=xmaxb.get()
    yminbool=yminb.get()
    ymaxbool=ymaxb.get()





submit_button= tk.Button(root, text='submit', command = submit)
submit_button.place(x=450, y=400)
root.mainloop()
