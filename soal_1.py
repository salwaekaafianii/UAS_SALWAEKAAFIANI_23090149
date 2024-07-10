students = []

while True:
    nim = input('Masukkan NIM: ')
    nama = input('Masukkan Nama: ')

    students.append({'NIM': nim, 'Nama': nama})

    tambah_lagi = input('Ingin tambah lagi? (ya/tidak): ').strip().lower()
    if tambah_lagi != 'ya':
        break

print('\nData Mahasiswa:')
for student in students:
    print(f'NIM: {student['NIM']}, Nama: {student['Nama']}')

print('End')

