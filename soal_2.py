import pandas as pd

data = {
    'Mahasiswa': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)

print('Data Mahasiswa dan Nilai:')
print(df)
print()

rata_algoritma = df['Algoritma dan Struktur Data'].mean()
rata_matematika = df['Matematika Numerik'].mean()

print(f'Rata-rata nilai Algoritma dan Struktur Data: {rata_algoritma}')
print(f'Rata-rata nilai Matematika Numerik: {rata_matematika}')
print()

df['Rata-rata Nilai'] = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean(axis=1)
print('Rata-rata nilai untuk setiap mahasiswa:')
print(df[['Mahasiswa', 'Rata-rata Nilai']])



