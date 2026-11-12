from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    imagen_url = models.URLField(max_length=500, blank=True, null=True, help_text="Enlace a la imagen del producto")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        return self.nombre