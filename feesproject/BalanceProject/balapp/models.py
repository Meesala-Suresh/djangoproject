from django.db import models

# Create your models here.
class Balance(models.Model):
    name=models.CharField(max_length=60)
    totalfees=models.FloatField(default='300000')
    paidfees=models.FloatField()
    feebal=models.FloatField(default='0')

    def fee_balance(self):
        feebal=(self.totalfees - self.paidfees)
        return feebal

    def save(self,*args, **kwargs):
        self.feebal = self.fee_balance()
        super().save(*args, **kwargs)
