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