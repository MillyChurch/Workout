from django.db import models

# Create your models here.

class Aluno(models.Model):
    nomeAluno = models.CharField(max_length=100, null=False, blank=False)
    


# CREATE TABLE Aluno (
#     idAluno INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
#     nomeAluno VARCHAR(100) NOT NULL,
#     tipoDePlano INT NOT NULL,
#     FOREIGN KEY (tipoDePlano) REFERENCES TiposDePlano(idPlano)
# );    