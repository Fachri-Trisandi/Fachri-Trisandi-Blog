from django.db import migrations


POSTS = [
    {
        "order": 1,
        "title": "Pengantar Arsitektur Perangkat Lunak",
        "slug": "pengantar-arsitektur-perangkat-lunak",
        "excerpt": "Dasar untuk memahami peran arsitektur dalam membangun sistem perangkat lunak.",
        "content": """Materi ini menjadi pintu masuk untuk memahami arsitektur perangkat lunak sebagai keputusan desain tingkat tinggi.

Pokok bahasan:
- Pengertian arsitektur perangkat lunak
- Perbedaan desain detail dan desain arsitektur
- Peran arsitek perangkat lunak dalam proyek
- Dampak keputusan arsitektur terhadap kualitas sistem

Catatan belajar:
Fokus utama materi ini adalah melihat sistem sebagai susunan komponen, relasi, batasan, dan keputusan teknis yang membentuk arah pengembangan.""",
    },
    {
        "order": 2,
        "title": "Pola Arsitektur Fundamental: Layered dan Monolith",
        "slug": "pola-arsitektur-fundamental-layered-dan-monolith",
        "excerpt": "Mengenal pola dasar sistem berlapis dan monolith sebagai bentuk arsitektur yang umum ditemui.",
        "content": """Materi ini membahas dua pola yang sering menjadi dasar pembelajaran arsitektur sistem.

Pokok bahasan:
- Konsep layered architecture
- Pemisahan tanggung jawab antar lapisan
- Karakteristik aplikasi monolith
- Kelebihan, kekurangan, dan konteks penggunaan

Catatan belajar:
Layered cocok saat sistem membutuhkan struktur yang mudah dipahami. Monolith cocok untuk sistem awal yang masih sederhana, tetapi perlu dijaga agar tidak sulit dikembangkan ketika fitur bertambah.""",
    },
    {
        "order": 3,
        "title": "Pola Arsitektur Kinerja Tinggi",
        "slug": "pola-arsitektur-kinerja-tinggi",
        "excerpt": "Ringkasan pola dan strategi untuk membuat sistem lebih cepat, stabil, dan siap menangani beban.",
        "content": """Materi ini mengarah pada cara merancang sistem yang mampu melayani banyak pengguna dan proses secara efisien.

Pokok bahasan:
- Skalabilitas dan performa
- Caching
- Load balancing
- Asynchronous processing
- Pemisahan beban baca dan tulis

Catatan belajar:
Kinerja tinggi tidak hanya soal server yang kuat. Keputusan arsitektur, pola komunikasi, strategi penyimpanan data, dan cara mengelola beban juga sangat menentukan.""",
    },
    {
        "order": 4,
        "title": "Visualisasi Arsitektur: UML dan C4 Model",
        "slug": "visualisasi-arsitektur-uml-dan-c4-model",
        "excerpt": "Membuat dokumentasi visual agar struktur sistem mudah dipahami oleh tim teknis dan non-teknis.",
        "content": """Materi ini membahas cara menyampaikan desain sistem menggunakan diagram yang jelas.

Pokok bahasan:
- Fungsi visualisasi arsitektur
- Diagram UML yang umum digunakan
- C4 Model: context, container, component, dan code
- Memilih tingkat detail diagram sesuai audiens

Catatan belajar:
Diagram yang baik bukan yang paling ramai, tetapi yang membantu pembaca memahami keputusan penting dalam sistem.""",
    },
    {
        "order": 5,
        "title": "Architectural Drivers: Mengarahkan Desain Sistem",
        "slug": "architectural-drivers-mengarahkan-desain-sistem",
        "excerpt": "Memahami faktor pendorong yang menentukan bentuk arsitektur sebuah sistem.",
        "content": """Materi ini menjelaskan hal-hal yang menjadi dasar keputusan arsitektur.

Pokok bahasan:
- Functional requirements
- Quality attributes
- Constraints
- Business goals
- Risiko teknis

Catatan belajar:
Architectural drivers membantu tim menentukan prioritas. Sistem yang berbeda bisa membutuhkan arsitektur berbeda karena tujuan, batasan, dan risikonya tidak sama.""",
    },
    {
        "order": 6,
        "title": "Architectural Quality Attributes",
        "slug": "architectural-quality-attributes",
        "excerpt": "Mengenal atribut kualitas seperti maintainability, reliability, scalability, security, dan usability.",
        "content": """Materi ini berfokus pada kualitas sistem yang sering menjadi alasan utama sebuah arsitektur dipilih.

Pokok bahasan:
- Maintainability
- Reliability
- Scalability
- Security
- Usability
- Trade-off antar atribut kualitas

Catatan belajar:
Tidak semua kualitas bisa dimaksimalkan sekaligus. Arsitektur yang baik membantu memilih trade-off yang paling sesuai dengan kebutuhan sistem.""",
    },
    {
        "order": 7,
        "title": "Modern Data Blueprint",
        "slug": "modern-data-blueprint",
        "excerpt": "Gambaran pendekatan modern untuk mengelola alur, penyimpanan, dan pemanfaatan data.",
        "content": """Materi ini membahas rancangan data modern sebagai bagian penting dari arsitektur sistem.

Pokok bahasan:
- Alur data dari sumber ke pengguna
- Penyimpanan data operasional dan analitik
- Integrasi data
- Kualitas dan tata kelola data
- Peran data dalam pengambilan keputusan

Catatan belajar:
Blueprint data membantu tim melihat bagaimana data dikumpulkan, diproses, disimpan, dan digunakan oleh aplikasi maupun proses bisnis.""",
    },
]


def seed_posts(apps, schema_editor):
    Post = apps.get_model("materi", "Post")
    for post in POSTS:
        Post.objects.update_or_create(slug=post["slug"], defaults={**post, "course": "Arsitektur Perangkat Lunak"})


def remove_seed_posts(apps, schema_editor):
    Post = apps.get_model("materi", "Post")
    Post.objects.filter(slug__in=[post["slug"] for post in POSTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("materi", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_posts, remove_seed_posts),
    ]
