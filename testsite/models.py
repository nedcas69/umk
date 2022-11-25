from django.db import models
from django.urls import reverse


class ProfTest(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование Профессии')

    def get_absolute_url(self):
        return reverse('professional', kwargs= {'professional_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        
class Questions(models.Model):
    question_text = models.CharField(max_length=255, verbose_name='Вопросы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    professional = models.ForeignKey('ProfTest', on_delete=models.PROTECT, verbose_name='Профессия', blank=True)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    question_number = models.PositiveSmallIntegerField( verbose_name='Номер')
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос'
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.PROTECT)
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice_text
    
    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
    
class Answers(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    true_answer = models.IntegerField(default=0)
    
    def __str__(self):
        return self.answer_text