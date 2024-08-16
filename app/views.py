from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Teclado, Mouse, Auricular, Mousepad
from .forms import TecladoForm, MouseForm, AuricularForm, MousepadForm
from django.contrib.auth.decorators import login_required

# Vistas para Teclado

def inicio(request):
    return render(request, 'app/index.html')


@login_required
def teclado_list(request):
    teclados = Teclado.objects.all()
    return render(request, 'app/teclado_list.html', {'teclados': teclados})

@login_required
def teclado_detail(request, pk):
    try:
        teclado = Teclado.objects.get(pk=pk)
    except Teclado.DoesNotExist:
        return HttpResponseNotFound("Teclado no encontrada")
    return render(request, 'app/teclado_detail.html', {'teclado': teclado})

@login_required
def teclado_create(request):
    if request.method == "POST":
        form = TecladoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teclado_list')
    else:
        form = TecladoForm()
    return render(request, 'app/teclado_form.html', {'form': form, 'title': 'Crear Teclado'})

@login_required
def teclado_update(request, pk):
    try:
        teclado = Teclado.objects.get(pk=pk)
    except Teclado.DoesNotExist:
        return HttpResponseNotFound("Teclado no encontrado")
    
    if request.method == "POST":
        form = TecladoForm(request.POST, instance=teclado)
        if form.is_valid():
            form.save()
            return redirect('teclado_list')
    else:
        form = TecladoForm(instance=teclado)
    return render(request, 'app/teclado_form.html', {'form': form, 'title': 'Actualizar Teclado'})

@login_required
def teclado_delete(request, pk):
    try:
        teclado = Teclado.objects.get(pk=pk)
    except Teclado.DoesNotExist:
        return HttpResponseNotFound("Teclado no encontrada")
    
    if request.method == "POST":
        teclado.delete()
        return redirect('teclado_list')
    return render(request, 'app/teclado_confirm_delete.html', {'teclado': teclado})

# Vistas para Mouse
@login_required
def mouse_list(request):
    mouses = Mouse.objects.all()
    return render(request, 'app/mouse_list.html', {'mouses': mouses})

@login_required
def mouse_detail(request, pk):
    try:
        mouse = Mouse.objects.get(pk=pk)
        print(mouse)
    except Mouse.DoesNotExist:
        return HttpResponseNotFound("Mouse no encontrado")
    return render(request, 'app/mouse_detail.html', {'mouse': mouse})

@login_required
def mouse_create(request):
    if request.method == "POST":
        form = MouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mouse_list')
    else:
        form = MouseForm()
    return render(request, 'app/mouse_form.html', {'form': form, 'title': 'Crear Mouse'})

@login_required
def mouse_update(request, pk):
    try:
        mouse = Mouse.objects.get(pk=pk)
    except Mouse.DoesNotExist:
        return HttpResponseNotFound("Mouse no encontrado")
    
    if request.method == "POST":
        form = MouseForm(request.POST, instance=mouse)
        if form.is_valid():
            form.save()
            return redirect('mouse_list')
    else:
        form = MouseForm(instance=mouse)
    return render(request, 'app/mouse_form.html', {'form': form, 'title': 'Actualizar Mouse'})

@login_required
def mouse_delete(request, pk):
    try:
        mouse = Mouse.objects.get(pk=pk)
    except Mouse.DoesNotExist:
        return HttpResponseNotFound("Mouse no encontrado")
    
    if request.method == "POST":
        mouse.delete()
        return redirect('mouse_list')
    return render(request, 'app/mouse_confirm_delete.html', {'mouse': mouse})

# Vistas para Auricular
@login_required
def auricular_list(request):
    auriculares = Auricular.objects.all()
    return render(request, 'app/auricular_list.html', {'auriculares': auriculares})

@login_required
def auricular_detail(request, pk):
    try:
        auricular = Auricular.objects.get(pk=pk)
    except Auricular.DoesNotExist:
        return HttpResponseNotFound("Auricular no encontrado")
    return render(request, 'app/auricular_detail.html', {'auricular': auricular})

@login_required
def auricular_create(request):
    if request.method == "POST":
        form = AuricularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auricular_list')
    else:
        form = AuricularForm()
    return render(request, 'app/auricular_form.html', {'form': form, 'title': 'Crear Auricular'})

@login_required
def auricular_update(request, pk):
    try:
        auricular = Auricular.objects.get(pk=pk)
    except Auricular.DoesNotExist:
        return HttpResponseNotFound("Auricular no encontrado")
    
    if request.method == "POST":
        form = AuricularForm(request.POST, instance=auricular)
        if form.is_valid():
            form.save()
            return redirect('auricular_list')
    else:
        form = AuricularForm(instance=auricular)
    return render(request, 'app/auricular_form.html', {'form': form, 'title': 'Actualizar Auricular'})

@login_required
def auricular_delete(request, pk):
    try:
        auricular = Auricular.objects.get(pk=pk)
    except Auricular.DoesNotExist:
        return HttpResponseNotFound("Auricular no encontrado")
    
    if request.method == "POST":
        auricular.delete()
        return redirect('auricular_list')
    return render(request, 'app/auricular_confirm_delete.html', {'auricular': auricular})

# Vistas para Mousepad
@login_required
def mousepad_list(request):
    mousepads = Mousepad.objects.all()
    return render(request, 'app/mousepad_list.html', {'mousepads': mousepads})

@login_required
def mousepad_detail(request, pk):
    try:
        mousepad = Mousepad.objects.get(pk=pk)
    except Mousepad.DoesNotExist:
        return HttpResponseNotFound("Mousepad no encontrada")
    return render(request, 'app/mousepad_detail.html', {'mousepad': mousepad})

@login_required
def mousepad_create(request):
    if request.method == "POST":
        form = MousepadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mousepad_list')
    else:
        form = MousepadForm()
    return render(request, 'app/mousepad_form.html', {'form': form, 'title': 'Crear Mousepad'})

@login_required
def mousepad_update(request, pk):
    try:
        mousepad = Mousepad.objects.get(pk=pk)
    except Mousepad.DoesNotExist:
        return HttpResponseNotFound("Mousepad no encontrada")
    
    if request.method == "POST":
        form = MousepadForm(request.POST, instance=mousepad)
        if form.is_valid():
            form.save()
            return redirect('mousepad_list')
    else:
        form = MousepadForm(instance=mousepad)
    return render(request, 'app/mousepad_form.html', {'form': form, 'title': 'Actualizar Mousepad'})

@login_required
def mousepad_delete(request, pk):
    try:
        mousepad = Mousepad.objects.get(pk=pk)
    except Mousepad.DoesNotExist:
        return HttpResponseNotFound("Mousepad no encontrada")
    
    if request.method == "POST":
        mousepad.delete()
        return redirect('mousepad_list')
    return render(request, 'app/mousepad_confirm_delete.html', {'mousepad': mousepad})

