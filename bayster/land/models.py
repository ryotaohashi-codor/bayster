from django.db import models

# Create your models here.

class Land(models.Model):
  title = models.CharField(max_length = 40)
  address = models.TextField()
  size = models.FloatField()
  purchase_price = models.IntegerField()
  estimated_profit = models.IntegerField()
  cost = models.IntegerField()
  project_background = models.TextField()
  applied_date = models.DateField(auto_now=True)
  STATUS_CHOICE = ((0,'申請中'),(1, '承認'),(2, '却下'))
  status = models.IntegerField(choices=STATUS_CHOICE, default=0)

  def __str__(self):
    return self.title


class LandReview(models.Model):
  comment = models.TextField()
  land = models.OneToOneField(
    Land,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.land.title