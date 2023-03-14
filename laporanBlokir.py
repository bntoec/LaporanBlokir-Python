from dotenv import load_dotenv
from os import getenv
from alright import WhatsApp
import time

if __name__ == "__main__":
    print()
    print("\t\t=================================================")
    print("\t\t          Program Laporan Blokir ke WA")
    print("\t\t               Created by bntoec      ")
    print("\t\t=================================================")
    print()

    load_dotenv()

    messenger = WhatsApp()

    # Rubah pake no Telp sendiri
    messenger.find_user(getenv("NOMER_HP_MU"))

    with open('DataBlokir.txt', 'r') as file:
        data = file.read().split('"=============================')
        for i in range(0, len(data)):
            messenger.send_message(data[i]) 
            time.sleep(1)

    print()
    print()
    print("Laporan telah selesai di kirim, mohon untuk di cek kembali")
    print("Jika sudah OK, silahkan foward ke grup")
    print()
    print("Console ini sudah dapat di tutup (CTRL+C)")
    # ini script biar logout setelah kirim
    # messenger.logout()