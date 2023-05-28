import pyautogui
import time


print("                                                                               \n")
print("###################     ##################   ##################    ##        ##")
print("###################     ##################   ##################     ##      ##")
print("##                      ##               ##  ##              ##      ##    ##")
print("##                      ##               ##  ##              ##       ##  ##")
print("##                      ##               ##  ##              ##        ####")
print("##                      ##              ##   ##              ##         ##")
print("##                      ################     ##################         ##")
print("###################     ##             ##    ##              ##         ##          TARAFINDAN YAPILDI")
print("###################     ##             ##    ##              ##         ##")
print("##                      ##             ##    ##              ##         ##")
print("##                      ##             ##    ##              ##         ##")
print("##                      ##             ##    ##              ##         ##")
print("##                      ##             ##    ##              ##         ##")
print("##                      ##             ##    ##              ##         ##")
print("###################     ##             ##    ##              ##         ##")
print("###################     ##             ##    ##              ##         ##\n")
print("Konusu: Sonsuz mesaj yollama programı.\n")



mesaj = input("Yollayacağınız mesaj: ")


print("[+] Başlatılıyor, lütfen bekleyin... \n")

time.sleep(8)
print("Not: Program 5 saniye içerisinde başlatılacaktır.\n")

time.sleep(9)
print("Arkadaşına on bin tane mesaj yollamak istiyorsan bu program tam sana göre!\n")

time.sleep(10)
print("Sonsuz mesaj yollama aracı!\n")

time.sleep(11)
print("Not: Ctrl+c programı durdurur.\n")



time.sleep(12)



def msj():
    pyautogui.press("enter")
    pyautogui.write(mesaj)



while True:
    msj()
    time.sleep(0)