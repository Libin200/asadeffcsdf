from django.db import models

# Create your models here.
class abijith(models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salary=models.IntegerField()
    contact_no=models.BigIntegerField()
    class Meta:
        db_table="ABIJITH"

class saaa(models.Model):
    f=models.FileField()
    class Meta:
        db_table="saaa"