from django.db import models

# Create your models here.
class InfoUser(models.Model):
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name="Загрузите фотографию"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Введите ФИО"
    )
    work = models.CharField(
        max_length=50,
        verbose_name="Вввдите профессию"
    )
    descriptions = models.TextField(
        verbose_name="Введите биографию"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Информация пользователя"
        verbose_name_plural = "Информации пользователей"
        
class About(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )
    age = models.CharField(
        max_length=3,
        verbose_name="Возраст"
    )
    nation = models.CharField(
        max_length=255,
        verbose_name="Нация"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    telegram = models.CharField(
        max_length=255,
        verbose_name="Username телеграм"
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Знание языка"
    )
    year = models.CharField(
        max_length=255,
        verbose_name="Годы опыта"
    )
    projects = models.CharField(
        max_length=255,
        verbose_name='Завершенные проекты'
    )
    clients = models.CharField(
        max_length=255,
        verbose_name="Счастливые клиенты"
    )
    awards = models.CharField(
        max_length=255,
        verbose_name="Полученные награды"
    )
    
    def __str__(self):
        return f'{self.first_name}  -  {self.last_name}'
    
    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"
        