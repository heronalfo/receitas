from django.test import TestCase
from .. import models


class TestsRecepsBase(TestCase):
    
    def setUp(self):
        # Cria uma categoria
        self.category = self.make_category(category_name="Teste")
        # Cria uma receita associada à categoria
        self.recipe = self.make_recipe(category=self.category)

    def make_category(self, category_name="Teste"):
        return models.Categories.objects.create(name=category_name)

    def make_recipe(self, category, title="Recipe test"):
        return models.Receps.objects.create(
            title=title,
            category=category,
            portions=1,
            user=self.make_author(),
            description="Recipe test",
            time="1h 20m",
            slug="test-recipe",
            is_published=False
        )

    def make_author(self, password="password", is_superuser=0, username="usertest", last_name="", email="usertest@gmail.com", is_staff=0, is_active=1, first_name=""):
    
        return models.User.objects.create(
            password=password,
            is_superuser=is_superuser,
            username=username,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            first_name=first_name
        )