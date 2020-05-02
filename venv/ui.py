from tkinter import *

def ui(temperature, humidity, pressure):

    temperature = str(temperature) + ' ' + chr(176) + 'C'
    humidity = str(humidity) + ' %'
    pressure = str(pressure) + ' mmHg'

    root = Tk()
    root.title('Weather Station')
    root.option_add("*Font", 'Calibri 20')
    text_temp = StringVar()
    text_hum = StringVar()
    text_press = StringVar()

    frame_left = Frame(root)
    frame_left.pack(anchor=E, side=LEFT)

    temp_label = Label(frame_left, text='Temperature: ')
    hum_label = Label(frame_left, text='Humidity: ')
    press_label = Label(frame_left, text='Pressure: ')
    temp_label.pack(anchor=E)
    hum_label.pack(anchor=E)
    press_label.pack(anchor=E)

    frame_right = Frame(root)
    frame_right.pack(anchor=E)

    temp = Label(frame_right, textvariable=text_temp)
    hum = Label(frame_right, textvariable=text_hum)
    press = Label(frame_right, textvariable=text_press)

    temp.pack(anchor=W)
    hum.pack(anchor=W)
    press.pack(anchor=W)

    text_temp.set(temperature)
    text_hum.set(humidity)
    text_press.set(pressure)

    root.mainloop()
