from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_id = models.AutoField
    emp_name = models.CharField(max_length=122, null=True, blank=True)
    emp_email = models.CharField(max_length=122, null=True, blank=True)
    country = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="blog/images", null=True, blank=True)

    def __str__(self):
        return str(self.emp_name)