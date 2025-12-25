from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.nom} - {self.code}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class Competences(models.Model):
    NIVEAUX = [
        (1, 'Debutant'),
        (2, 'Intermediaire'),
        (3, 'Avance'),
        (4, 'Expert'),
        (5, 'Maître'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    niveau = models.IntegerField(choices=NIVEAUX, default=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.titre