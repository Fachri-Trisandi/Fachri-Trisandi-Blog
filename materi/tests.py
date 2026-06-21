from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostPagesTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Contoh Materi",
            slug="contoh-materi",
            course="Arsitektur Perangkat Lunak",
            excerpt="Ringkasan materi contoh.",
            content="Isi materi contoh.",
            order=1,
        )

    def test_index_page_shows_post(self):
        response = self.client.get(reverse("materi:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contoh Materi")

    def test_detail_page_shows_post_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Isi materi contoh.")

    def test_index_search_filters_posts(self):
        Post.objects.create(
            title="Materi Lain",
            slug="materi-lain",
            course="Arsitektur Perangkat Lunak",
            excerpt="Ringkasan lain.",
            content="Isi yang berbeda.",
            order=2,
        )

        response = self.client.get(reverse("materi:index"), {"q": "Contoh Materi"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contoh Materi")
        self.assertContains(response, "1 materi ditemukan")
        self.assertNotContains(response, "Ringkasan lain.")
