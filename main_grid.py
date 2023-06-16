import tkinter

window = tkinter.Tk()

LabelNama = tkinter.Label(window, text="Eka Tresna Wati")
LabelKampus = tkinter.Label(window, text="STIMIK TUNAS BANGSA")
LabelProdi = tkinter.Label(window, text="Informatika A")
LabelSemester = tkinter.Label(window, text="Semester 4")

LabelNama.grid(row=0, column=0)
LabelKampus.grid(row=1, column=1)
LabelProdi.grid(row=2, column=0)
LabelSemester.grid(row=3, column=1)


window.mainloop()