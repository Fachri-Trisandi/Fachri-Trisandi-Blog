# Blog Fahri

Project Django sederhana untuk blog materi perkuliahan.

## Menjalankan Project

```powershell
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py createsuperuser
.venv\Scripts\python.exe manage.py runserver
```

Buka halaman utama di `http://127.0.0.1:8000/`.

## Mengelola Materi

1. Buat akun admin dengan `createsuperuser`.
2. Jalankan server.
3. Buka `http://127.0.0.1:8000/admin/`.
4. Tambah atau edit materi melalui menu `Posts`.

## Hosting ke Railway

Project ini sudah disiapkan untuk deploy ke Railway dengan file `railway.json`.

Langkah umum:

1. Push project ini ke GitHub.
2. Masuk ke Railway.
3. Buat project baru, lalu pilih `Deploy from GitHub repo`.
4. Pilih repository GitHub project ini.
5. Tambahkan service database PostgreSQL di Railway.
6. Pada service aplikasi, isi environment variables:

```text
SECRET_KEY=isi dengan secret key acak
DEBUG=false
PGDATABASE=${{Postgres.PGDATABASE}}
PGUSER=${{Postgres.PGUSER}}
PGPASSWORD=${{Postgres.PGPASSWORD}}
PGHOST=${{Postgres.PGHOST}}
PGPORT=${{Postgres.PGPORT}}
```

7. Deploy aplikasi.
8. Buka tab `Settings` atau `Networking`, lalu pilih `Generate Domain`.
9. Untuk membuat akun admin di hosting, buka Railway Shell lalu jalankan:

```bash
python manage.py createsuperuser
```

Konfigurasi deploy ada di `railway.json`:

```text
Build Command: python -m pip install -r requirements.txt && python manage.py collectstatic --noinput
Pre-deploy Command: python manage.py migrate
Start Command: gunicorn blog_fahri.wsgi:application --bind 0.0.0.0:$PORT
```
