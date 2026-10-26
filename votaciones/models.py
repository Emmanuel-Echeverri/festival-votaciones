from django.db import models


class Edicion(models.Model):
    nombre = models.CharField(max_length=150)
    anio = models.PositiveIntegerField(unique=True, verbose_name="año")
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    lugar = models.CharField(max_length=100, default="Valledupar")
    activa = models.BooleanField(default=False)

    class Meta:
        ordering = ["-anio"]
        verbose_name = "edición"
        verbose_name_plural = "ediciones"

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


class Categoria(models.Model):
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE, related_name="categorias")
    nombre = models.CharField(max_length=120)
    lema = models.CharField(max_length=120, blank=True, help_text="Frase corta sobre la categoría")
    descripcion = models.TextField(blank=True)
    imagen_url = models.URLField(max_length=500, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        unique_together = ("edicion", "nombre")

    def __str__(self):
        return f"{self.nombre} - {self.edicion.anio}"


class Votacion(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="votaciones")
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fecha_apertura = models.DateTimeField(null=True, blank=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    abierta = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "votación"
        verbose_name_plural = "votaciones"

    def __str__(self):
        return self.titulo


class Opcion(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name="opciones")
    numero = models.PositiveIntegerField(default=1)
    nombre = models.CharField(max_length=150)
    procedencia = models.CharField(max_length=120, blank=True)
    descripcion = models.TextField(blank=True)
    imagen_url = models.URLField(max_length=500, blank=True, help_text="Enlace a una imagen (opcional)")

    class Meta:
        ordering = ["numero"]
        verbose_name = "opción"
        verbose_name_plural = "opciones"

    def __str__(self):
        return f"#{self.numero} {self.nombre}"
