from django.db import migrations


EXPANDED_POSTS = {
    "pengantar-arsitektur-perangkat-lunak": {
        "excerpt": "Dasar untuk memahami arsitektur sebagai keputusan penting yang membentuk struktur, kualitas, dan arah pengembangan sistem.",
        "content": """Gambaran umum:
Arsitektur perangkat lunak adalah cara kita menyusun sistem secara menyeluruh. Di dalamnya ada keputusan tentang komponen, hubungan antar komponen, cara data mengalir, batasan teknis, dan prinsip yang dipakai agar sistem tetap mudah dikembangkan. Arsitektur tidak hanya membahas kode, tetapi juga arah besar dari sebuah sistem.

Konsep inti:
- Komponen adalah bagian utama sistem, misalnya antarmuka pengguna, API, service, database, dan modul integrasi.
- Relasi menjelaskan bagaimana komponen saling berkomunikasi.
- Constraint adalah batasan seperti teknologi yang wajib dipakai, waktu pengerjaan, biaya, atau aturan keamanan.
- Quality attribute adalah kualitas yang ingin dicapai, misalnya performa, keamanan, skalabilitas, dan maintainability.

Mengapa arsitektur penting:
Tanpa arsitektur yang jelas, sistem bisa tumbuh tidak terkendali. Fitur mungkin tetap bisa ditambahkan, tetapi lama-lama kode menjadi sulit dirawat, perubahan kecil menimbulkan bug, dan tim sulit memahami alur sistem. Arsitektur membantu memberi peta agar pengembangan tidak hanya berjalan cepat di awal, tetapi tetap sehat dalam jangka panjang.

Contoh sederhana:
Pada blog materi perkuliahan, arsitekturnya bisa dibagi menjadi layer tampilan, layer view/controller, model data, dan database. Template HTML bertugas menampilkan halaman, view Django mengambil data, model Post mendefinisikan struktur materi, dan SQLite menyimpan isi postingan. Pemisahan ini membuat perubahan tampilan tidak langsung mengganggu penyimpanan data.

Hal yang perlu diingat:
Arsitektur yang baik bukan berarti paling rumit. Arsitektur yang baik adalah yang sesuai dengan kebutuhan sistem. Untuk proyek kecil, struktur sederhana lebih cocok. Untuk sistem besar, perlu pembagian komponen yang lebih kuat agar tim bisa bekerja paralel dan sistem tetap mudah dikembangkan.

Kesimpulan:
Pengantar arsitektur perangkat lunak mengajarkan bahwa sebelum menulis banyak kode, kita perlu memahami bentuk besar sistem. Keputusan di awal akan memengaruhi kualitas sistem, cara tim bekerja, dan kemampuan aplikasi untuk berubah di masa depan.""",
    },
    "pola-arsitektur-fundamental-layered-dan-monolith": {
        "excerpt": "Pembahasan pola layered dan monolith sebagai dasar memahami struktur aplikasi yang sederhana, teratur, dan umum digunakan.",
        "content": """Gambaran umum:
Layered architecture dan monolith adalah dua pola fundamental yang sering menjadi titik awal ketika belajar arsitektur perangkat lunak. Keduanya banyak ditemukan dalam aplikasi nyata karena mudah dipahami dan cukup praktis untuk sistem kecil sampai menengah.

Layered architecture:
Layered architecture membagi sistem ke dalam beberapa lapisan. Setiap lapisan punya tanggung jawab yang berbeda. Contoh yang umum adalah presentation layer, business layer, data access layer, dan database layer. Presentation layer mengurus tampilan, business layer mengurus aturan proses, data access layer mengurus komunikasi dengan database, lalu database menyimpan data.

Kelebihan layered:
- Struktur kode lebih rapi karena setiap bagian punya tanggung jawab jelas.
- Lebih mudah dipahami oleh anggota tim baru.
- Perubahan pada satu lapisan bisa lebih mudah dikontrol.
- Cocok untuk aplikasi web sederhana seperti blog, sistem akademik, atau sistem administrasi.

Kekurangan layered:
Jika semua perubahan harus melewati banyak lapisan, sistem bisa terasa lambat atau terlalu formal. Selain itu, jika aturan pemisahan tidak dijaga, logika bisnis bisa bercampur dengan tampilan atau query database sehingga manfaat layer menjadi berkurang.

Monolith:
Monolith adalah pola ketika seluruh fitur utama aplikasi berada dalam satu aplikasi besar. Antarmuka, logika bisnis, dan akses data biasanya dikembangkan, diuji, dan dijalankan dalam satu paket. Django project sederhana seperti blog ini termasuk contoh monolith yang sehat untuk skala kecil.

Kelebihan monolith:
- Mudah dibuat dan dijalankan.
- Deployment lebih sederhana.
- Cocok untuk proyek kuliah, prototype, dan aplikasi awal.
- Debugging lebih mudah karena semua bagian berada dalam satu codebase.

Kekurangan monolith:
Saat aplikasi semakin besar, monolith bisa menjadi sulit dirawat. Perubahan pada satu fitur dapat berdampak pada fitur lain. Tim besar juga bisa saling bertabrakan karena bekerja di codebase yang sama.

Kesimpulan:
Layered membantu merapikan struktur internal sistem, sedangkan monolith membantu menyederhanakan pengembangan awal. Keduanya bukan pola yang buruk. Yang penting adalah mengetahui kapan pola tersebut masih cocok dan kapan sistem perlu dibagi menjadi komponen yang lebih mandiri.""",
    },
    "pola-arsitektur-kinerja-tinggi": {
        "excerpt": "Strategi arsitektur untuk meningkatkan performa sistem melalui caching, load balancing, queue, dan pengelolaan beban.",
        "content": """Gambaran umum:
Arsitektur kinerja tinggi berfokus pada kemampuan sistem untuk merespons cepat, tetap stabil saat banyak pengguna, dan tidak mudah gagal ketika beban meningkat. Performa bukan hanya tentang spesifikasi server, tetapi juga cara sistem dirancang.

Masalah yang sering terjadi:
Sistem lambat biasanya terjadi karena query database berat, terlalu banyak request ke server yang sama, proses panjang dilakukan secara langsung, atau tidak ada mekanisme penyimpanan sementara. Jika semua pekerjaan dilakukan dalam satu jalur, pengguna harus menunggu lebih lama.

Caching:
Caching adalah teknik menyimpan hasil proses atau data yang sering diakses agar tidak dihitung berulang kali. Misalnya halaman materi populer bisa disimpan sementara sehingga server tidak perlu terus mengambil data yang sama dari database. Cache cocok untuk data yang sering dibaca tetapi tidak terlalu sering berubah.

Load balancing:
Load balancer membagi trafik ke beberapa server. Jika satu server menerima terlalu banyak request, load balancer bisa mengarahkan request lain ke server berbeda. Pola ini membantu sistem tetap responsif saat jumlah pengguna meningkat.

Queue dan asynchronous processing:
Tidak semua proses harus dijalankan langsung saat pengguna mengirim request. Proses berat seperti mengirim email, membuat laporan, memproses file, atau sinkronisasi data bisa dimasukkan ke queue. Worker akan memprosesnya di belakang layar, sedangkan pengguna tetap mendapat respons cepat.

Database optimization:
Database sering menjadi titik lambat. Strategi yang bisa dipakai antara lain indexing, pagination, read replica, dan pemisahan data yang sering dibaca. Query juga harus dibuat efisien agar tidak mengambil data terlalu banyak.

Contoh pada aplikasi blog:
Untuk blog materi kuliah, kinerja tinggi belum terlalu dibutuhkan jika pengguna sedikit. Namun konsepnya tetap bisa diterapkan secara ringan, misalnya pagination untuk daftar materi, caching halaman yang jarang berubah, dan optimasi query ketika jumlah postingan semakin banyak.

Kesimpulan:
Kinerja tinggi dicapai dengan mengurangi pekerjaan yang tidak perlu, membagi beban, dan memindahkan proses berat ke jalur yang lebih sesuai. Arsitektur yang baik membuat sistem cepat bukan karena memaksa satu server bekerja keras, tetapi karena beban dikelola dengan cerdas.""",
    },
    "visualisasi-arsitektur-uml-dan-c4-model": {
        "excerpt": "Cara menggunakan UML dan C4 Model untuk menjelaskan struktur sistem kepada pembaca teknis maupun non-teknis.",
        "content": """Gambaran umum:
Visualisasi arsitektur membantu tim memahami sistem tanpa harus membaca seluruh kode. Diagram membuat struktur, alur, dan hubungan antar bagian sistem menjadi lebih mudah dibicarakan. Dua pendekatan yang sering digunakan adalah UML dan C4 Model.

UML:
UML atau Unified Modeling Language adalah standar visual untuk menggambarkan sistem perangkat lunak. UML memiliki banyak jenis diagram, seperti class diagram, sequence diagram, use case diagram, dan activity diagram. Setiap diagram memiliki tujuan yang berbeda.

Contoh penggunaan UML:
Class diagram cocok untuk menunjukkan struktur data dan hubungan antar class. Sequence diagram cocok untuk menunjukkan urutan interaksi, misalnya pengguna membuka halaman blog, view menerima request, model mengambil data, lalu template menampilkan hasil. Use case diagram cocok untuk menggambarkan apa saja yang dapat dilakukan pengguna.

C4 Model:
C4 Model adalah pendekatan visualisasi arsitektur yang terdiri dari empat tingkat: Context, Container, Component, dan Code. Model ini membantu menjelaskan sistem dari gambaran paling besar sampai detail teknis.

Level C4:
- Context menjelaskan sistem berada di lingkungan apa dan siapa penggunanya.
- Container menjelaskan aplikasi utama, database, service, atau sistem eksternal.
- Component menjelaskan bagian penting di dalam container.
- Code menjelaskan detail implementasi jika memang dibutuhkan.

Kapan menggunakan UML dan C4:
UML cocok ketika ingin menjelaskan perilaku atau struktur teknis secara lebih formal. C4 cocok ketika ingin menjelaskan arsitektur sistem secara bertahap kepada audiens yang berbeda. Untuk presentasi kuliah, C4 sering lebih mudah dipahami karena dimulai dari gambaran besar.

Kesalahan umum:
Diagram yang terlalu ramai justru sulit dipahami. Diagram yang baik harus punya tujuan jelas. Jika ingin menjelaskan alur login, jangan campur dengan seluruh struktur database. Jika ingin menjelaskan container, jangan langsung masuk ke detail kode.

Kesimpulan:
Visualisasi arsitektur bukan hanya hiasan dokumentasi. Diagram membantu menyamakan pemahaman, mempercepat diskusi, dan mengurangi salah tafsir. UML dan C4 Model dapat saling melengkapi jika digunakan sesuai kebutuhan.""",
    },
    "architectural-drivers-mengarahkan-desain-sistem": {
        "excerpt": "Faktor pendorong seperti requirement, quality attribute, constraint, risiko, dan tujuan bisnis yang menentukan arah desain sistem.",
        "content": """Gambaran umum:
Architectural drivers adalah faktor-faktor utama yang mengarahkan keputusan arsitektur. Drivers membantu menjawab pertanyaan: sistem ini harus dibuat seperti apa, prioritasnya apa, dan batasannya apa.

Functional requirement:
Functional requirement menjelaskan fitur yang harus dimiliki sistem. Misalnya blog materi harus bisa menampilkan daftar materi, membuka detail materi, melakukan pencarian, dan mengelola postingan melalui admin. Fitur-fitur ini menentukan komponen apa saja yang diperlukan.

Quality attribute:
Quality attribute menjelaskan kualitas yang diharapkan dari sistem. Contohnya performance, security, usability, maintainability, scalability, dan reliability. Dua sistem bisa memiliki fitur yang sama, tetapi arsitekturnya berbeda karena quality attribute yang diprioritaskan berbeda.

Constraint:
Constraint adalah batasan yang harus diterima. Contoh constraint adalah wajib memakai Django, database harus SQLite, waktu pengerjaan terbatas, atau aplikasi hanya berjalan lokal. Constraint tidak selalu buruk. Justru constraint membantu memperjelas ruang desain.

Business goals:
Tujuan bisnis atau tujuan proyek juga memengaruhi arsitektur. Untuk proyek kuliah, tujuan utamanya mungkin demonstrasi konsep dan tampilan yang rapi. Untuk aplikasi komersial, tujuan bisa berupa keamanan transaksi, kemampuan menangani banyak pengguna, dan kemudahan integrasi.

Risiko:
Risiko teknis perlu diperhatikan sejak awal. Misalnya risiko data sulit dicari jika jumlah materi banyak, risiko tampilan tidak responsif di layar kecil, atau risiko struktur kode berantakan saat fitur bertambah. Arsitektur membantu mengurangi risiko tersebut.

Contoh pada blog materi:
Driver utama blog ini adalah kesederhanaan, kemudahan membaca, dan kemudahan mengelola materi. Karena itu, monolith Django dengan model Post, template, static file, dan SQLite sudah cukup. Jika nanti blog dipakai banyak pengguna, driver bisa berubah dan arsitektur perlu ditingkatkan.

Kesimpulan:
Architectural drivers membuat keputusan desain lebih terarah. Tanpa drivers, arsitektur bisa dibuat berdasarkan selera saja. Dengan drivers, setiap keputusan punya alasan yang bisa dijelaskan.""",
    },
    "architectural-quality-attributes": {
        "excerpt": "Pembahasan atribut kualitas arsitektur seperti maintainability, performance, security, scalability, reliability, dan usability.",
        "content": """Gambaran umum:
Architectural quality attributes adalah karakteristik kualitas yang ingin dicapai oleh sistem. Atribut ini sering lebih menentukan bentuk arsitektur dibanding fitur itu sendiri. Sistem tidak cukup hanya berfungsi, tetapi juga harus mudah digunakan, aman, cepat, dan mudah dirawat sesuai kebutuhan.

Maintainability:
Maintainability adalah kemudahan sistem untuk diperbaiki dan dikembangkan. Struktur folder yang jelas, pemisahan view, model, template, dan static file membantu maintainability. Kode yang mudah dipahami akan mempercepat perubahan di masa depan.

Performance:
Performance berkaitan dengan kecepatan respons sistem. Untuk blog, performa terlihat dari seberapa cepat halaman daftar dan detail materi dibuka. Query yang efisien, gambar ringan seperti SVG, dan CSS sederhana membantu halaman terasa cepat.

Security:
Security berkaitan dengan perlindungan data dan akses. Dalam Django, fitur admin harus dilindungi dengan login. Input pengguna perlu divalidasi. Pada aplikasi yang lebih besar, keamanan juga mencakup proteksi CSRF, pengelolaan password, izin akses, dan sanitasi data.

Scalability:
Scalability adalah kemampuan sistem untuk menangani pertumbuhan. Blog sederhana mungkin hanya memiliki beberapa materi, tetapi jika materi bertambah ratusan, sistem perlu pagination, pencarian yang lebih baik, dan optimasi database. Skalabilitas tidak selalu harus disiapkan secara besar dari awal, tetapi perlu dipikirkan arahnya.

Reliability:
Reliability adalah kemampuan sistem tetap berjalan dengan benar. Error handling, backup database, dan pengujian membantu meningkatkan reliability. Test sederhana yang memastikan halaman utama dan detail berjalan adalah langkah awal yang baik.

Usability:
Usability berkaitan dengan kenyamanan pengguna. Tampilan yang bersih, warna yang nyaman, tombol yang jelas, dan pencarian materi membuat sistem lebih mudah dipakai. Untuk blog materi, usability sangat penting karena tujuan utamanya adalah membaca dan belajar.

Trade-off:
Tidak semua atribut kualitas bisa dimaksimalkan bersamaan. Keamanan tinggi bisa menambah kompleksitas. Performa tinggi bisa membutuhkan cache dan infrastruktur tambahan. Maintainability kadang membuat struktur awal lebih panjang. Arsitektur adalah seni memilih trade-off yang paling sesuai.

Kesimpulan:
Quality attributes membantu menilai apakah sistem benar-benar baik, bukan sekadar berjalan. Dalam tugas arsitektur, menyebutkan quality attributes dan trade-off menunjukkan bahwa desain sistem dibuat dengan pertimbangan yang matang.""",
    },
    "modern-data-blueprint": {
        "excerpt": "Gambaran modern tentang alur data dari sumber, ingestion, penyimpanan, transformasi, analitik, hingga dashboard.",
        "content": """Gambaran umum:
Modern Data Blueprint adalah rancangan yang menjelaskan bagaimana data dikumpulkan, diproses, disimpan, dikelola, dan digunakan. Dalam sistem modern, data tidak hanya disimpan untuk transaksi, tetapi juga dimanfaatkan untuk analisis dan pengambilan keputusan.

Sumber data:
Data bisa berasal dari aplikasi, form pengguna, file, API eksternal, sensor, log sistem, atau database lain. Pada blog materi, sumber data utamanya adalah postingan yang dibuat melalui admin. Pada sistem besar, sumber data bisa jauh lebih beragam.

Ingestion:
Ingestion adalah proses memasukkan data dari sumber ke sistem penyimpanan. Proses ini bisa dilakukan secara batch atau streaming. Batch berarti data dikirim dalam periode tertentu, sedangkan streaming berarti data mengalir secara terus-menerus.

Storage:
Data perlu disimpan pada tempat yang sesuai. Database relasional cocok untuk data terstruktur dan transaksi. Data lake atau lakehouse cocok untuk data besar dari berbagai format. Pemilihan storage bergantung pada kebutuhan akses, ukuran data, dan jenis analisis.

Transformation:
Data mentah sering belum siap dipakai. Transformation membersihkan, menggabungkan, mengubah format, dan memperkaya data. Contohnya mengubah log mentah menjadi laporan jumlah pengunjung, atau mengubah data postingan menjadi statistik materi paling sering dibaca.

Analytics dan dashboard:
Setelah data siap, data bisa dianalisis dan divisualisasikan. Dashboard membantu pengguna melihat insight dengan cepat. Pada blog materi, dashboard sederhana bisa menampilkan jumlah materi, kategori paling banyak, atau materi terbaru.

Governance:
Modern data blueprint juga perlu memikirkan kualitas data, keamanan, hak akses, dan dokumentasi. Data yang salah atau tidak jelas sumbernya dapat menghasilkan keputusan yang keliru. Karena itu, data governance menjadi bagian penting.

Contoh penerapan sederhana:
Untuk proyek blog ini, blueprint datanya sederhana: admin memasukkan materi, Django menyimpan ke SQLite, view mengambil data, template menampilkan materi, dan widget menampilkan statistik. Walaupun sederhana, alurnya sudah mencerminkan konsep dasar pipeline data.

Kesimpulan:
Modern Data Blueprint membantu tim memahami perjalanan data dari awal sampai digunakan. Rancangan data yang jelas membuat sistem lebih mudah dikembangkan, dianalisis, dan dipercaya.""",
    },
}


def expand_posts(apps, schema_editor):
    Post = apps.get_model("materi", "Post")
    for slug, data in EXPANDED_POSTS.items():
        Post.objects.filter(slug=slug).update(**data)


def shrink_posts(apps, schema_editor):
    # Keep the expanded content on rollback. The earlier seed migration still
    # owns the initial sample data, so no destructive reverse operation is needed.
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("materi", "0002_seed_initial_posts"),
    ]

    operations = [
        migrations.RunPython(expand_posts, shrink_posts),
    ]
