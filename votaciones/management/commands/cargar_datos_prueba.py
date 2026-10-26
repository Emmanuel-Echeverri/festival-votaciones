import datetime
from django.core.management.base import BaseCommand
from votaciones.models import Edicion, Categoria, Votacion, Opcion

U = "https://images.unsplash.com/photo-%s?auto=format&fit=crop&w=%d&q=85"

CATEGORIAS = [
    ("Cantante", "La voz del festival", "Celebra las voces que hacen vibrar cada verso y llevan el vallenato a nuevas generaciones.", "1517230878791-4d28214057c2",
     ["Valeria Campo", "Samuel Cotes", "Mariana Díaz", "Andrés Ariza", "Lucía Mendoza", "Julián Maestre"]),
    ("Comparsa", "Ritmo y tradición", "Color, movimiento y alegría en escena. Elige la comparsa que mejor representa nuestra cultura.", "1786027298573-aae33f51b9a1",
     ["Raíces del Cesar", "Son de mi Tierra", "Alma Guajira", "Herencia Caribe", "Danza del Río", "Colores del Valle"]),
    ("Acordeón", "El alma vallenata", "Maestros y nuevas promesas se encuentran para demostrar su destreza en el instrumento rey.", "1563823265119-6221c184a333",
     ["Mateo Carrillo", "Elena Daza", "Nicolás Oñate", "Sara Gutiérrez", "Tomás Zuleta", "Camila Guerra"]),
    ("Vestuario", "Identidad que se viste", "Diseños que entretejen historia, territorio y creatividad en cada detalle de su confección.", "1718119617938-2a3b376fb7d6",
     ["Casa Macondo", "Taller Cañaguate", "Arte de mi Valle", "Origen Caribe", "Manos del Cesar", "Tierra Bonita"]),
    ("Agrupación", "Juntos suena mejor", "Conjuntos que mezclan talento y complicidad para crear el sonido que nos une como región.", "1779037805741-e3f45e84af95",
     ["Los Herederos", "Canto del Valle", "Nueva Provincia", "La Parranda Real", "Son Vallenato", "Aires del Cesar"]),
]
FOTOS = ["1648113825706-2dfec36f1578", "1526218626217-dc65a29bb444", "1565277028057-5c7b9a2da373",
         "1608319917470-9d9179430f8d", "1719579002882-1537d31b7721", "1595422656857-ced3a4a0ce25"]


class Command(BaseCommand):
    help = "Carga datos de prueba basados en el diseño del frontend."

    def handle(self, *args, **opts):
        ed, _ = Edicion.objects.get_or_create(
            anio=2027, defaults={"nombre": "59.º Festival de la Leyenda Vallenata", "activa": True,
                                 "lugar": "Valledupar", "fecha_inicio": datetime.date(2027, 4, 29),
                                 "fecha_fin": datetime.date(2027, 5, 2)})
        Edicion.objects.get_or_create(anio=2026, defaults={"nombre": "58.º Festival de la Leyenda Vallenata"})

        for nombre, lema, desc, foto, participantes in CATEGORIAS:
            cat, _ = Categoria.objects.get_or_create(
                edicion=ed, nombre=nombre,
                defaults={"lema": lema, "descripcion": desc, "imagen_url": U % (foto, 1200)})
            vot, _ = Votacion.objects.get_or_create(
                categoria=cat, titulo=f"Votación {nombre} {ed.anio}")
            for i, p in enumerate(participantes, start=1):
                Opcion.objects.get_or_create(
                    votacion=vot, numero=i,
                    defaults={"nombre": p, "procedencia": "Valledupar, Cesar" if i % 2 == 0 else "La Paz, Cesar",
                              "descripcion": "Una propuesta que une tradición, creatividad y el orgullo de nuestras raíces.",
                              "imagen_url": U % (FOTOS[i - 1], 900)})
        self.stdout.write(self.style.SUCCESS("Datos de prueba cargados."))
