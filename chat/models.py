from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


    text = models.CharField(max_length=200, null=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.text)



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.question.text} - {self.text}'
