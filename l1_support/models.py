from django.db import models

# Create your models here.
class error_code(models.Model):
    error_id = models.CharField(max_length =30)
    module = models.CharField(max_length =30)
    url = models.URLField(null =True)
    applies_to = models.TextField(null =True)
    symptoms = models.TextField(null =True)
    cause = models.TextField(null =True)
    solution = models.TextField(null =True)
    last_update = models.TextField(null =True)
    # check_list = models.JSONField(null=True)
    # place_holder = models.JSONField(null =True)

    def __str__(self):
        return self.error_id