from django.db import models

# Create your models here.

class Subscription(models.Model):
    title = models.CharField("Описание", max_length=50)
    price = models.IntegerField ("Цена")
    expiry_date = models.DateField("Срок истечения")
    
    class Meta:
        verbose_name = "Абонимент" # название таблицы
        verbose_name_plural = "Абонименты" # название таблицы в мн. ч.
        ordering = ["price"] # сортировка
        indexes = [
            models.Index(fields=["expiry_date"]), # для быстрого поиска
            models.Index(fields=["price"]),
            models.Index(fields=["title"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["price", "title"],
                condition = models.Q(desc = "expiry_date"),
                name = "unique_surname_bio"
            ),
            ]
        
    def __str__(self):
        return f"{self.surname} {self.name}"

class Position(models.Model):
    title = models.CharField("Должность", unique=True)
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        indexes = [
            models.Index(fields=["Должность"])
        ]
    def __str__(self):
        return f"{self.surname} {self.name}"
    
class Client(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=11)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["last_name, first_name, father_name"]
        indexes = [
            models.Index(fields=["Имя"]), # для быстрого поиска
            models.Index(fields=["Фамилия"]),
            models.Index(fields=["Номер телефона"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            ]
    def __str__(self):
        return f"{self.surname} {self.name}"
    
class Trainer(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=11)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"
        ordering = ["last_name, first_name, father_name"]
        indexes = [
            models.Index(fields=["Имя"]), # для быстрого поиска
            models.Index(fields=["Фамилия"]),
            models.Index(fields=["Номер телефона"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            ]
    def __str__(self):
        return f"{self.surname} {self.name}"

class Training(models.Model):
    start_time = models.DateTimeField ("Начало")
    end_time = models.DateTimeField ("Конец")
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тренеровка"
        verbose_name_plural = "Тренеровки"
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["start_time"]), # для быстрого поиска
            models.Index(fields=["end_time"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            ]
    def __str__(self):
        return f"{self.surname} {self.name}"
