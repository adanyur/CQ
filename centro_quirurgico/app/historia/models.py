from django.db import models

# Create your models here.
class Historia(models.Model):
    hc_numhis = models.CharField(max_length=10,primary_key=True)
    hc_apepat = models.CharField(max_length=50)
    hc_apemat = models.CharField(max_length=50)
    hc_nombre = models.CharField(max_length=50)
    hc_fecnac = models.CharField(max_length=10)
    hc_sexo  = models.CharField(max_length=1)
    hc_estadoreg = models.CharField(max_length=1)
    hc_estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'historias'
