import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

#Inisialisasi
window = tkinter.Tk()
window.configure(bg="#17a589")
icon_img = PhotoImage(file='D:\Python_1\Aset\planting.png')
window.iconphoto(False, icon_img)
window.geometry("300x300")
window.resizable(False,False)
window.title("Pendaftaran SOBAT BPS")

#Header
header_label = ttk.Label(window, text="Pengisian Formulir", font=(20), background="sky blue", foreground="#17202a")
header_label.pack(pady=20)

#Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT = tkinter.StringVar()
JURUSAN = tkinter.StringVar()
SEMESTER = tkinter.StringVar()
UNIVERSITAS = tkinter.StringVar()
#Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not ALAMAT.get() or not JURUSAN.get() or not SEMESTER.get() or not UNIVERSITAS.get():     
        showinfo(title="Eror!", message="Mohon lengkapi semua form!")
 else:
    pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
    showinfo(title="Selamat",message=pesan)


#Frame input
style = ttk.Style()
style.configure("Custom.TEntry",fiedbackground="#257cff")
input_frame = ttk.Frame(window)

#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

#Komponen nama lengkap
nama_depan_label = ttk.Label(input_frame, text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP,style="Custom.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#Komponen alamat
alamat_label = ttk.Label(input_frame, text="Alamat :")
alamat_label.pack(padx=10,fill="x",expand=True)
alamat_entry = ttk.Entry(input_frame,textvariable=ALAMAT,style="Custom.TEntry")
alamat_entry.pack(padx=10,fill="x",expand=True)

#Komponen jurusan
jurusan_label = ttk.Label(input_frame, text="Jurusan:")
jurusan_label.pack(padx=10,fill="x",expand=True)
jurusan_entry = ttk.Entry(input_frame,textvariable=JURUSAN,style="Custom.TEntry")
jurusan_entry.pack(padx=10,fill="x",expand=True)
#Komponen semester

semester_label = ttk.Label(input_frame, text="Semester:")
semester_label.pack(padx=10,fill="x",expand=True)
semester_entry = ttk.Entry(input_frame,textvariable=SEMESTER,style="Custom.TEntry")
semester_entry.pack(padx=10,fill="x",expand=True)
#Komponen universitas

universitas_label = ttk.Label(input_frame, text="Universitas:")
universitas_label.pack(padx=10,fill="x",expand=True)
universitas_entry = ttk.Entry(input_frame,textvariable=UNIVERSITAS,style="Custom.TEntry")
universitas_entry.pack(padx=10,fill="x",expand=True)

#Tombol
tombol_daftar = ttk.Button(input_frame, text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)


window.mainloop()