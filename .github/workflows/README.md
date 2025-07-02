# Proyek UAS PKPL - Aplikasi Flask

Ini adalah proyek sederhana untuk Ujian Akhir Semester mata kuliah Pengembangan dan Konfigurasi Perangkat Lunak (PKPL).

## Alur Kerja CI/CD

Proyek ini menggunakan GitHub Actions untuk otomatisasi:
1.  **Unit Test**: Setiap kali ada *push* atau *pull request* ke branch `main`, `pytest` akan dijalankan.
2.  **Build Docker Image**: Jika tes berhasil, sebuah Docker image akan dibuat.
3.  **Push ke Docker Hub**: Image yang sudah dibuat akan diunggah ke [Docker Hub](https://hub.docker.com/r/NAMA_USER_DOCKERHUB/NAMA_REPO_ANDA).

## Cara Menjalankan Secara Lokal

1.  **Clone repositori ini.**
2.  **Instal dependensi:** `pip install -r requirement.txt`
3.  **Jalankan aplikasi:** `python app.py`
4.  Buka browser dan akses `https://git.aztech.id/tedirusli/uas-pkpl-app.git`.