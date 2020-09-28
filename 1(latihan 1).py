print('''----
username = SLMN007 
password = sulaiman007
diatas adalah password dan usernamenya jika menginputkan selain kata tersebut maka akan terjadi eror
----''')

userandpass = {'SLMN007': 'sulaiman007', 'aku': 'saya', 'dia': 'mereka'}
chance = 3

while chance != 0:
    user = input('masukkan username: ')
    pss = input('masukkan password: ')

    for cek in userandpass:
        if user == cek and pss == userandpass[cek]:
            print('anda berhasil masuk')
            chance = 0
            break
    else:
        print('maaf user name dan password anda salah')
        chance -= 1
