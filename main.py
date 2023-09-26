print("ini display dokter")
print("mari  kita buat program display")



from flask import Flask, render_template
import pandas as pd  # Untuk membaca data dari Excel

app = Flask(_name_)

# Fungsi untuk membaca data dokter dari file Excel
def baca_data_dokter():
    # Ubah nama file dan lokasi sesuai dengan file Excel Anda
    file_excel = 'data_dokter.xlsx'
    data = pd.read_excel(file_excel)
    return data

@app.route('/')
def tampil_jadwal_dokter():
    # Panggil fungsi untuk membaca data dokter
    data_dokter = baca_data_dokter()
    
    # Kirim data dokter ke template HTML
    return render_template('jadwal_dokter.html', data_dokter=data_dokter)

if _name_ == '_main_':
    app.run(debug=True)

