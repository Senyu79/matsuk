from django.db import models

class Subscription(models.Model):
    title = models.CharField("Описание", max_length=50)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    expiry_date = models.DateField("Срок истечения")
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Клиент")
    
    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
        ordering = ["expiry_date"]
        indexes = [
            models.Index(fields=["expiry_date"]),
            models.Index(fields=["title"])
        ]
        
    def __str__(self):
        return f"{self.title}"

class Position(models.Model):
    title = models.CharField("Должность", max_length=50, unique=True)
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["salary"])
        ]
    
    def __str__(self):
        return f"{self.title}"
    
class Client(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50, null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=11, unique=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["last_name", "first_name", "father_name"]
        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
            models.Index(fields=["phone_number"])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Trainer(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50, null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=11, unique=True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    cover_url = models.URLField("Фото", blank=True, null=True)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"
        ordering = ["last_name", "first_name", "father_name"]
        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
            models.Index(fields=["phone_number"])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Training(models.Model):
    start_time = models.DateTimeField("Начало")
    end_time = models.DateTimeField("Конец")
    trainer_id = models.ManyToManyField(Trainer, verbose_name="Тренер")
    client_id = models.ManyToManyField(Client, verbose_name="Клиент")

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["start_time"]),
            models.Index(fields=["end_time"])
        ]

    def __str__(self):
        return f"{self.start_time} {self.end_time}"
