from django.test import TestCase
from django.urls import reverse
from .models import Image, Category
from datetime import date

class GalleryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        self.image = Image.objects.create(
            title='Test Image',
            image='test.jpg',
            created_date=date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_with_category_filter(self):
        response = self.client.get(reverse('gallery'), {'category': 'Nature'})
        self.assertContains(response, 'Test Image')

    def test_image_detail_view(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')
