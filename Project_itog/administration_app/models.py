from django.db import models

class Category(models.Model): # Категории: кошки, собаки, котята, щенки. Сделано с возможностью расширения в будущем
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'

class Gender(models.Model): # пол животного
    gender = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.gender}'

class Animal(models.Model): # создание экземпляра класса "Животное"
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='animal_photos/')
    description = models.TextField(default='')
    age = models.IntegerField(default=1,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,default='', on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.age}, {self.category}, {self.description}'

class New(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1800)
    date_added = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title