from django.db import models


class Database(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class QuizQuestion(models.Model):
    baza = models.ForeignKey(Database, on_delete=models.CASCADE, related_name='savol_baza')
    fan=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='fan')
    savol = models.TextField(blank=True, null=True)
    javoblar = models.JSONField(default=list)
    javob = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'QuizQuestion'
        verbose_name_plural = 'QuizQuestions'

    def __str__(self):
        return self.savol


class QuizUser(models.Model):
    ism = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()
    fan=models.ForeignKey(Subject, on_delete=models.CASCADE)
    baza = models.ForeignKey(Database, on_delete=models.CASCADE)
    natija = models.IntegerField()
    urinishlar = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'QuizUser'
        verbose_name_plural = 'QuizUsers'
        unique_together = ('telegram_id', 'baza', 'fan')

    def __str__(self):
        return self.ism
        