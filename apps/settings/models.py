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
        
class Skills(models.Model):
    skill = models.CharField(
        max_length=100,
        verbose_name="Скилл"
    )
    procent = models.CharField(
        max_length=100,
        verbose_name="Процент"
    )

    def __str__(self) -> str:
        return f"{self.skill}"
    
    class Meta:
        verbose_name= "Скилы"
        verbose_name_plural = "Скилл"

class Work(models.Model):
    work_time = models.CharField(
        max_length=100,
        verbose_name="Годы работы"
    )
    job_title = models.CharField(
        max_length=100,
        verbose_name="Должность"
    )
    company = models.CharField(
        max_length=100,
        verbose_name="компания где работал"
    )
    comment = models.CharField(
        max_length=100,
        verbose_name="comment"
    )
    def __str__(self) -> str:
        return f"{self.job_title} - {self.company}"
    
    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыты работы"

class Education(models.Model):
    year = models.CharField(
        max_length=100,
        verbose_name="Год окончаеия"
    )
    education = models.CharField(
        max_length=255,
        verbose_name="Научный стенпень"
    )
    h_e_i = models.CharField(
        max_length=100,
        verbose_name="ВУЗ"
    )
    comment = models.TextField(
        max_length=100,
        verbose_name="Комментарии"
    )
    def __str__(self) -> str:
        return f"{self.education} - {self.h_e_i}"
    
    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образовании"

class Contact(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=255
    ) 
    email= models.EmailField(
        verbose_name="Электронная почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"