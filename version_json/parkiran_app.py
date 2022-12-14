import tkinter as tk
import os
from xmlrpc.client import FastMarshaller ; os.system("cls")

from tkinter.font import Font

from main import *

def GUI_MAIN():

    def menu_masuk():
        frame.destroy()
        GUI_MASUK()

    def menu_keluar():
        frame.destroy()
        GUI_KELUAR()

    frame = tk.Tk()
    frame.geometry("400x500+450+80")
    frame.title("PARKING SYSTEM")

    text_font = Font(family="Lucida Console", size=40)

    masuk_button = tk.Button(frame, text="IN", font=text_font, padx=17, bg="green", fg="white", borderwidth=5, command=menu_masuk)
    masuk_button.place(x=45, y=180) 

    keluar_button = tk.Button(frame, text="OUT", font=text_font, bg="red", fg="white", borderwidth=5, command=menu_keluar)
    keluar_button.place(x=215, y=180) 

    frame.mainloop()

def GUI_MASUK():
    frame = tk.Tk()
    frame.geometry("400x500+450+80")
    frame.title("PARKING SYSTEM")

    frame.resizable(False, False)

    title_font = Font(family="Lucida Console", size=16)
    text_font = Font(family="Lucida Console", size=14)
    log_font = Font(family="Lucida Console", size=10)

    judul = tk.Label(frame, text="SELAMAT DATANG", font=title_font)
    judul.place(x=110, y=5)

    no_id_text = tk.Label(frame, text="No ID     :", font=text_font)
    no_id_text.place(x=30, y=50)

    no_id_input = tk.Text(frame, height=1, width=25, borderwidth=2, pady=4)
    no_id_input.place(x=155, y=51)

    kendaraan_text = tk.Label(frame, text="Kendaraan :", font=text_font)
    kendaraan_text.place(x=30, y=85)

    kendaraan_input = tk.Text(frame, height=1, width=25, borderwidth=2, pady=4)
    kendaraan_input.place(x=155, y=86)

    global logExists
    logExists = False

    def placeLog():

        global log_box
        global logExists

        if logExists:
            deleteLog()

        if sudah_terpakai(no_id):
            log_box = tk.Label(frame, text="E-Money Card anda sudah terpakai,\nsilakan gunakan yang lain        ", font=log_font, fg="red")
            log_box.place(x=30, y=140)
            logExists = True

        elif not valid(no_id):
            log_box = tk.Label(frame, text="E-Money anda tidak valid,\nsilakan gunakan yang lain", font=log_font, fg="red")
            log_box.place(x=30, y=140)
            logExists = True

        elif kendaraan not in listKendaraan:
            log_box = tk.Label(frame, text="Jenis kendaraan tidak valid,\npilih (mobil/motor)!        ", font=log_font, fg="red")
            log_box.place(x=30, y=140)
            logExists = True

    def deleteLog():
        global logExists
        log_box.destroy()
        logExists = False

    def callMasuk():

        global no_id

        no_id = no_id_input.get("1.0",'end-1c')

        global kendaraan
        kendaraan = kendaraan_input.get("1.0",'end-1c')
        
        global listKendaraan
        listKendaraan = ["motor", "mobil"]

        if not sudah_terpakai(no_id) and valid(no_id) and kendaraan in listKendaraan:
            masuk(no_id, kendaraan)

            if logExists:
                deleteLog()

            log_box_valid = tk.Label(frame, text="Data anda sudah tercatat", font=log_font, fg="green")
            log_box_valid.place(x=30, y=140)

        else:
            placeLog()


    enter_id = tk.Button(frame, text="Enter", command=callMasuk)
    enter_id.place(x=323, y=120)

    def menu_utama():
        frame.destroy()
        GUI_MAIN()

    back = tk.Button(frame, text="Back", command=menu_utama)
    back.place(x=323, y=400)

    frame.mainloop()

def GUI_KELUAR():

    frame = tk.Tk()
    frame.geometry("400x500+450+80")
    frame.title("PARKING SYSTEM")

    frame.resizable(False, False)

    title_font = Font(family="Lucida Console", size=16)
    text_font = Font(family="Lucida Console", size=14)
    log_font = Font(family="Lucida Console", size=10)

    judul = tk.Label(frame, text="SELAMAT JALAN", font=title_font)
    judul.place(x=110, y=5)

    no_id_text = tk.Label(frame, text="No ID     :", font=text_font)
    no_id_text.place(x=30, y=50)

    no_id_input = tk.Text(frame, height=1, width=25, borderwidth=2, pady=4)
    no_id_input.place(x=155, y=51)

    global logExists
    logExists = False

    def placeLog2():

        global log_box
        global logExists

        if logExists:
            deleteLog()

        if sudah_terpakai(no_id) == False:
            log_box = tk.Label(frame, text="E-Money Card anda tidak terdaftar,\nsilakan gunakan yang lain         ", font=log_font, fg="red")
            log_box.place(x=30, y=140)
            logExists = True

    def deleteLog():
        global logExists
        log_box.destroy()
        logExists = False

    def callKeluar():

        nosaldo_Exists = False

        global no_id

        no_id = no_id_input.get("1.0",'end-1c')

        if sudah_terpakai(no_id):

            lama_parkir = durasi(no_id)
            jenis_kendaraan = data_pengguna[f"{no_id}"]["jenis kendaraan"]
            waktu_masuk = data_pengguna[f"{no_id}"]["waktu masuk"]
            wk = str(datetime.datetime.now())
            wk = datetime.datetime(int(wk[0:4]), int(wk[5:7]), int(wk[8:10]), int(wk[11:13]), int(wk[14:16]), int(wk[17:19]))
            waktu_keluar = wk
            tarif_parkir = int(tarif(lama_parkir, jenis_kendaraan))

            if  data_emoney[f"{no_id}"]["saldo"] >= tarif_parkir:
                keluar(no_id)

                if logExists:
                    deleteLog()

                if nosaldo_Exists:
                    log_box_nosaldo.destroy()
                    nosaldo_Exists = False
                    
                empty = "?????? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ??? ???"
                log_box_valid = tk.Label(frame, text=f"Terima Kasih{empty} ", font=log_font, fg="green")
                log_box_valid.place(x=30, y=140)

            else:
                if logExists:
                    deleteLog()

                log_box_nosaldo = tk.Label(frame, text="Maaf, saldo anda tidak cukup", font=log_font, fg="red")
                log_box_nosaldo.place(x=30, y=140)

                nosaldo_Exists = True

        else:
            placeLog2()


    enter_id = tk.Button(frame, text="Enter", command=callKeluar)
    enter_id.place(x=323, y=120)

    def menu_utama():
        frame.destroy()
        GUI_MAIN()

    back = tk.Button(frame, text="Back", command=menu_utama)
    back.place(x=323, y=400)

    frame.mainloop()

GUI_MAIN()