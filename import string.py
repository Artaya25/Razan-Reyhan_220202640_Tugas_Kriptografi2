import string
abjad = string.ascii_letters + string.digits + string.punctuation + ' '

def enkrip(pesan):
    global abjad
    key = int(input('Masukkan Kunci: '))
    cipher = ''  # Inisialisasi teks cipher
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)
            k = (k + key) % len(abjad)
            cipher += abjad[k]
        else:
            cipher += i
    return cipher

def dekrip(cipher):
    global abjad
    key = int(input('Masukkan Kunci: '))
    pesan = ''  # Inisialisasi teks hasil dekripsi
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key) % len(abjad)
            pesan += abjad[k]
        else:
            pesan += i
    return pesan

if __name__ == '__main__':
    print('------------------------------------')
    print('---Oleh Razan Reyhan. (220202649)---')
    print('------------------------------------')

    pilihan = int(input('1. Enkripsi\n2. Dekripsi\nPilih Opsi: '))
    if pilihan == 1:
        pesan = input('Masukkan pesan (Plaintext): ')
        print('Hasil Enkripsi:', enkrip(pesan))
    elif pilihan == 2:
        cipher = input('Masukkan pesan (Chipertext): ')
        print('Hasil Dekripsi:', dekrip(cipher))
    else:
        print('Masukkan opsi 1 atau 2!')
