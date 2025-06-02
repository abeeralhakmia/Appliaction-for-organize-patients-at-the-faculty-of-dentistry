from django.db import models

# نموذج الطبيب
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# نموذج الطالب
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    year = models.IntegerField()

    def __str__(self):
        return self.name

# نموذج المريض
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# نموذج طلب المعاينة
class AppointmentRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# نموذج المعاينة
class Examination(models.Model):
    appointment = models.ForeignKey(AppointmentRequest, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    notes = models.TextField()
    evaluation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# نموذج الإعلان
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# نموذج النصيحة
class Advice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

