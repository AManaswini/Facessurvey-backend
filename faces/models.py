import json
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    data = models.TextField()
    pub_date = models.DateTimeField('Date published',default=now,editable=False)
    def __str__(self):
        print(type(self.data))
        # with open('results.txt','w') as f:
        #     f.write(json.dumps(self.data))
        return self.data