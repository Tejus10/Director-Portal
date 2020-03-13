from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime


doc_type_choices =  [
    ('1','Notesheet'),
    ('2','File'),
    ('3','Letter Pad'),
    ('4','Plain Application'),
    ('5','Form/Leave Application'),
    ('6','Others'),
]

internal_from_choices = [
    ('1','Department'),
    ('2','Section'),
    ('3','Centre'),
    ('4','Others'),
]

external_from_choices = [
 ('1','MHRD'),
 ('2','PMO'),
 ('3','NHPC'),
]


class internal_letter(models.Model):
    def number():
        no = internal_letter.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    si_no = models.IntegerField(default=number)
    in_date = models.DateField(default=datetime.date(datetime.now()))
    doc_type = models.CharField(max_length=1,choices=doc_type_choices)
    reference = models.CharField(max_length=50)
    From = models.CharField(max_length=1,choices=internal_from_choices)
    out_date = models.DateField()
    to = models.CharField(max_length=1,choices=internal_from_choices)
    subject = models.CharField(max_length=50)
    remarks = models.CharField(max_length=500)
    referred_to = models.ForeignKey(User, related_name='ri',blank=True,null=True, on_delete = models.CASCADE)



class external_letter(models.Model):
    def number():
        no = external_letter.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    si_no = models.IntegerField(default=number)
    receipt_date = models.DateField(default=datetime.date(datetime.now()))
    From = models.CharField(max_length=1,choices=external_from_choices)
    subject = models.CharField(max_length=50)
    marked_to = models.CharField(max_length=100)
    action_needed = models.CharField(max_length=300)
    file = models.CharField(max_length=100)
    referred_to = models.ForeignKey(User, related_name='re',blank=True,null=True, on_delete = models.CASCADE)
    remarks = models.CharField(max_length=500)


class internal_past(models.Model):
    comment = models.CharField(max_length=500)
    fro = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    dated = models.DateField()
    file = models.ForeignKey(internal_letter, on_delete=models.CASCADE,blank=True,null=True)
    time = models.TimeField(auto_now=True)

class external_past(models.Model):
    comment = models.CharField(max_length=500)
    fro = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    dated = models.DateField()
    file = models.ForeignKey(external_letter, on_delete=models.CASCADE,blank=True,null=True)    
    time = models.TimeField(auto_now=True)