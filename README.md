# Ndata
## Tugas 2 PBP Ganjil 23/24

Checklist untuk tugas ini adalah sebagai berikut.

- [X] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
		name sebagai nama item dengan tipe CharField.
		amount sebagai jumlah item dengan tipe IntegerField.
		description sebagai deskripsi item dengan tipe TextField.
- [X] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [X] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [X] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [X] Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

Tautan menuju link adaptable yang telah di deploy [Ndata](https://ndata.adaptable.app/)

## Pertanyaan dan jawaban
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
**Membuat sebuah proyek Django baru**
1. Membuat sebuah Git dan Direktori lokal dengan nama ```Ndata``` 
2. Membuat virtual environment (venv) python untuk mengisolasi python yang digunakan pada proyek ini, mengaktifkan venv dengan memasukkan ```env\Scripts\activate.bat``` pada cmd di direkotori ```Ndata```
3. Membuat file ```requirements.txt``` yang berisi *depedencies* yang dibutuhkan pada proyek ini
4. Install *Depedencies* tadi dengan ```pip intall -r requirements.txt```, lalu membuat proyek django dengan ```django-admin startproject Ndata``` 
5. Membuka ```settings.py```, pada ```ALLOWED_HOST``` jadikan ```["*"]```
6. Mengecek apakah django sudah benar terinstall dengan ```python manage.py runserver```, lalu membuka http://localhost:8000. Jika tidak memunculkan error, maka proyek django berhasil 
7. Nonaktifkan server dengan ```CTRL + C``` dan matikan venv dengan ```deactivate```

**Membuat aplikasi dengan nama main pada proyek tersebut.**
1. Masuk kembali ke mode venv dengan  ```env\Scripts\activate.bat```
2. jalankan ```python manage.py startapp main``` untuk membuat folder baru bernama ```main```
3. pada ```settings.py```, menambahkan ```main``` pada ```INSTALLED APPS```

**Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
1. Membuat file ```urls.py``` pada direktori ```main``` 
2. menambahkan kode ini pada ```urls.py```
<img src="assets/urls di main.jpeg" alt="Isi urls.py di main" title="Isi urls.py di main">

**Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.**
1. Buka file ```models.py``` pada ```main```
2. Import ```from django.db import models```
3. lalu tambahkan ```class Product(models.Model):
    name = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()```


* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
* Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
* Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
