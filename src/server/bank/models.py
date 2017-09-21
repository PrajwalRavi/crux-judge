from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

#1. Problems: id,title, statement, output, uploadedby
#2. Admins: id, name, email, passwordhash
#3. Students: id, name, email, passwordhash
@python_2_unicode_compatible
class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,unique=False)
    statement = models.TextField(max_length=3000,unique=False)
    input_file = models.FileField()
    output_file = models.FileField()
    uploadedby = models.ForeignKey(User,verbose_name="problem-setter")
    
    def __str__(self):
        return "{} : {}".format(self.problem_id,self.title)
    class Meta:
        verbose_name='problem'
        ordering = ['problem_id']
