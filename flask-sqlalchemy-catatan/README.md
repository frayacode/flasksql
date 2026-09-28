# Flask + SQLAlchemy: Aplikasi Catatan

Contoh proyek dari tutorial **Belajar Python Part 17: Menghubungkan Aplikasi Flask dengan Database**.
Aplikasi catatan sederhana dengan operasi CRUD (tambah, lihat, ubah, hapus) memakai Flask-SQLAlchemy.

## Cara Menjalankan

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000 di browser. Tabel dibuat otomatis saat aplikasi pertama kali dijalankan.

## Konfigurasi Database

Secara default memakai SQLite (`database.db`). Untuk production, set environment variable `DATABASE_URL`:

```bash
export DATABASE_URL="postgresql://username:password@localhost/nama_database"
pip install psycopg2-binary
```

## Struktur Proyek

```
.
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── templates/
    └── index.html
```
