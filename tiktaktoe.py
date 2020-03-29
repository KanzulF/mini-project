## Game TikTakToe 

papan = [1,2,3,4,5,6,7,8,9]
def output():
    for baris in range(0,9,3):
        for kolom in range(3):
            print(papan[kolom+baris],end="\t")
        print("\n\n")

def cek_kemenangan():
    if papan[0] == papan[1] == papan[2] or papan[3] == papan[4] == papan[5] or papan[6] == papan[7] == papan[8] or papan[0] == papan[3] == papan[6] or papan[1] == papan[4] == papan[7] or papan[2] == papan[5] == papan[8] or papan[0] == papan[4] == papan[8] or papan[6] == papan[4] == papan[2]:
        print("-----------------------------Selamat kamu menang")
        return True
    else:
        return False
    
def cek_input():
    if history.count(player) >= 1:
        cek = True
        return False
    else:
        history.append(player)
        cek = False
        return True

history = []
output()
batas_utama = 1
while batas_utama <= 5:
    batas_utama = batas_utama + 1
    cek = True
    while cek:
        player = int(input("Player 1 "))
        if cek_input():
            papan[player-1] = "O"
            output()
            break
    if cek_kemenangan():
        break
    cek = True
    if batas_utama != 5:
        while cek:
            player = int(input("Player 2 "))
            if cek_input():
                papan[player-1] = "X"
                output()
                break
        if cek_kemenangan():
            break
if batas_utama == 6:
    print("PERMAINAN SELESAI DAN KALIAN SERI1")
