from django.db import models
from datetime import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.

class Customer(models.Model):
    bride = models.CharField(max_length=200,blank=True)
    bridefullname = models.CharField(max_length=200,blank=True)
    groom = models.CharField(max_length=200,blank=True)
    groomfullname = models.CharField(max_length=200,blank=True)
    addressline1 = models.CharField(max_length=200,blank=True)
    addressline2 = models.CharField(max_length=200,blank=True)
    addressline3 = models.CharField(max_length=200,blank=True)
    postalcode = models.CharField(max_length=200,blank=True)

    host1 = models.CharField(max_length=200,blank=True)
    host2 = models.CharField(max_length=200,blank=True)
    host3 = models.CharField(max_length=200,blank=True)
    host4 = models.CharField(max_length=200,blank=True)
    
    bridecontactname = models.CharField(max_length=200,blank=True)
    bridecontactname2 = models.CharField(max_length=200,blank=True)
    bridecontactno = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    bridecontactno2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    groomcontactname = models.CharField(max_length=200,blank=True)
    groomcontactname2 = models.CharField(max_length=200,blank=True)
    groomcontactno = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    groomcontactno2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    eventdatetime = models.DateTimeField(default=datetime.now, blank=True)
    
    no_of_guests_attending = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2000)])

    customeremail = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    bridecontact_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    groomcontact_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)],blank=True)
    
    eventstarttime = models.DateTimeField(default=datetime.now, blank=True)
    eventendtime = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.customeremail
  
    class Meta:
        verbose_name_plural = "customerdetails"

class Itinerary(models.Model):
    title = models.CharField(max_length=200,blank=True)
    starttime = models.DateTimeField(default=datetime.now, blank=True)
    endtime = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
 
    def __str__(self):
        return self.title
  
    class Meta:
        verbose_name_plural = "itinerary"

class Wish(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.CharField(max_length=200, blank=True)
  
    def __str__(self):
        return self.title
  
    class Meta:
        verbose_name_plural = "Wish"
	
class Rsvp(models.Model):
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.status
  
    class Meta:
        verbose_name_plural = "RSVP"

class Group(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
  
    class Meta:
        verbose_name_plural = "Group"

class Guestbook(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests_invited = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True)
    no_of_guests_attending = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    contact_number = models.CharField(max_length=20, blank=True)
    rsvp = models.ForeignKey(Rsvp, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
  
    class Meta:
        verbose_name_plural = "Guestbook"
# Create your models here.
