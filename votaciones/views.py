from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistroForm
from .models import Categoria, Edicion


def _edicion_activa():
    return Edicion.objects.filter(activa=True).first() or Edicion.objects.first()


def inicio(request):
    edicion = _edicion_activa()
    return render(request, "votaciones/inicio.html", {
        "edicion": edicion,
        "total_categorias": edicion.categorias.count() if edicion else 0,
        "ediciones": Edicion.objects.all(),
    })


@login_required
def categorias(request, edicion_id=None):
    edicion = get_object_or_404(Edicion, pk=edicion_id) if edicion_id else _edicion_activa()
    if edicion is None:
        messages.info(request, "Aún no hay ediciones registradas.")
        return redirect("inicio")
    return render(request, "votaciones/categorias.html", {
        "edicion": edicion,
        "categorias": edicion.categorias.all(),
    })


@login_required
def participantes(request, categoria_id):
    categoria = get_object_or_404(Categoria.objects.select_related("edicion"), pk=categoria_id)
    votaciones = categoria.votaciones.prefetch_related("opciones")
    total = sum(v.opciones.count() for v in votaciones)
    return render(request, "votaciones/participantes.html", {
        "categoria": categoria, "votaciones": votaciones, "total_opciones": total,
    })


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada. ¡Bienvenido!")
            return redirect("categorias")
    else:
        form = RegistroForm()
    return render(request, "registration/registro.html", {"form": form})
