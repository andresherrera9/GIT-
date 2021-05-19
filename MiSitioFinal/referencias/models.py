from django.db import models

class Referencias(models.Model):
    idreferencias = models.IntegerField(primary_key=True)
    referencia = models.CharField(max_length=45, blank=True, null=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    subpartida = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.subpartida, self.referencia, self.marca)

    class Meta:
        managed = True
        db_table = 'referencias'
#Se crea un modelo para insertar info a una base de datos con tres columnas: id, first_name y last_name.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

#Se va a intentar crear un modelo para una registration y login form.