from django.db import models

class Candidate(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title        

class Skill(models.Model):
    title = models.CharField(max_length=200)
    candidates = models.ManyToManyField(Candidate)
    jobs = models.ManyToManyField(Job)

    def __str__(self):
        return self.title 



   
