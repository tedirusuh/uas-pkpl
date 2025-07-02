import pytest
from app import app as flask_app # Mengimpor aplikasi dari app.py

# `pytest.fixture` adalah fungsi persiapan yang dijalankan sebelum tes
@pytest.fixture
def client(app):
    # Membuat "klien palsu" untuk simulasi akses browser
    return app.test_client()

def test_home_page(client):
    # Fungsi tes utama
    response = client.get('/') # Mensimulasikan akses ke halaman utama
    assert response.status_code == 200 # 1. Memastikan halaman berhasil diakses (HTTP 200 OK)
    assert b"Selamat Datang" in response.data # 2. Memastikan konten halaman berisi teks yang diharapkan