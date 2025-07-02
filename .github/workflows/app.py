from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/')
def home():
    """Menampilkan pesan selamat datang."""
    return "<h1>Selamat Datang di Proyek UAS PKPL!</h1><p>Aplikasi ini berhasil berjalan.</p>"

if __name__ == '__main__':
    # Menjalankan aplikasi di semua antarmuka pada port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)