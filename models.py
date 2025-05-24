from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    favouritesports=models.CharField(max_length=100)
    user_name=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class section(models.Model):
    name=models.CharField(max_length=100)
    #one img only
    img=models.ImageField(upload_to="section_img")
    ###########################################################
#section1
class sports(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="sportImageLogo")
    type=models.CharField(max_length=100)
    section= models.ForeignKey(section, on_delete=models.CASCADE)

class sportsImage(models.Model):
    img=models.ImageField(upload_to="sportImage")
    sport= models.ForeignKey(sports, on_delete=models.CASCADE)

class sportsvideo(models.Model):
    video=models.FileField(upload_to="sports_video")
    sport= models.ForeignKey(sports, on_delete=models.CASCADE)

class sportadvice(models.Model):
    advice=models.CharField(max_length=100)
    sport= models.ForeignKey(sports, on_delete=models.CASCADE)

class sportsclub(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    sport=models.ForeignKey(sports, on_delete=models.CASCADE)
    ##############################################################################3

########################################################################################
    ###############################################################################
###########################################################################################

#section2
class physicalTherapy(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="physicalTherapyLogo")
    type=models.CharField(max_length=100)
    section= models.ForeignKey(section, on_delete=models.CASCADE)

class physicalImage(models.Model):
    img=models.ImageField(upload_to="physicalImage")
    physical= models.ForeignKey(physicalTherapy, on_delete=models.CASCADE)

class physicalvideo(models.Model):
    video=models.FileField(upload_to="physicalvideo")
    physical= models.ForeignKey(physicalTherapy, on_delete=models.CASCADE)

class physicaladvice(models.Model):
    advice=models.CharField(max_length=100)
    physical= models.ForeignKey(physicalTherapy, on_delete=models.CASCADE) 
    
class physicalCenter(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    physical=models.ForeignKey(physicalTherapy, on_delete=models.CASCADE)
    ################################################################################
    ##############################################################################################3
#section3
class feed(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="feedLogo")
    type=models.CharField(max_length=100)
    section= models.ForeignKey(section, on_delete=models.CASCADE)

class feedImage(models.Model):
    img=models.ImageField(upload_to="physicalImage")
    feed= models.ForeignKey(feed, on_delete=models.CASCADE)

class feedadvice(models.Model):
    advice=models.CharField(max_length=100)
    feed= models.ForeignKey(feed, on_delete=models.CASCADE) 
    ###########################################################################################
