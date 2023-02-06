from django.shortcuts import render, redirect 
from . models import Personaje
from . models import Universo
from django.contrib import messages

# Create your views here.
def home(request):
    personajes = Personaje.objects.all() 
    universos = Universo.objects.all()
    contexto = {"personajes":personajes,"universos":universos}
    return render(request,"principal.html",contexto)

#-------------------------------------//-----------------------------------#

def registrarPersonaje(request):
    universos = Universo.objects.all()
    return render(request,"formpersonajes.html",{"universos":universos})

#-------------------------------------//-----------------------------------#

def crearPersona(request):

    try:
        id = request.POST["selector"] 
        universo = Universo.objects.get(id=id)
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        descripcion = request.POST["descripcion"]
        edad = request.POST["edad"]
        nacionalidad = request.POST["nacionalidad"]
        raza = request.POST["raza"]
        imagen = request.POST["imagen"]

        personaje =  Personaje.objects.create(codigo=codigo,nombre=nombre,apellido=apellido,edad=edad,nacionalidad=nacionalidad,descripcion=descripcion,raza=raza,image_url=imagen,universo=universo)
        messages.success(request, "Personaje Creado Correctamente")
        return redirect("../infoPersonaje/"+codigo)
    except Exception as e:
        messages.success(request,"Esto no se pudo guardar")
        universos = Universo.objects.all()
        return render(request,"formpersonajes.html",{"universos":universos})
            

#-------------------------------------//-----------------------------------#

def modificarPersona(request,codigo):
    persona = Personaje.objects.get(codigo=codigo)
    universos = Universo.objects.all()
    contexto = {"persona":persona,"universos":universos}
    return render(request,"editarpersona.html",contexto)


def editarPersona(request):

    try:
        id = request.POST["selector"]
        universo = Universo.objects.get(id=id)
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        descripcion = request.POST["descripcion"]
        edad = request.POST["edad"]
        nacionalidad = request.POST["nacionalidad"]
        raza = request.POST["raza"]
        imagen = request.POST["imagen"]

        personaje = Personaje.objects.get(codigo=codigo)
        personaje.universo = universo
        personaje.nombre = nombre
        personaje.apellido = apellido
        personaje.edad = edad
        personaje.nacionalidad = nacionalidad
        personaje.raza = raza
        personaje.image_url = imagen
        personaje.descripcion = descripcion
        personaje.save()
        messages.success(request, "Personaje editado correctamente")
        return redirect("../infoPersonaje/"+codigo)
    except Exception as e:
        messages.success(request, "Error al editar el personaje")
        return redirect("../modificarPersona/"+codigo)

#-------------------------------------//-----------------------------------#
def registrarUniverso(request):
    return render(request,"formuniversos.html")

#-------------------------------------//-----------------------------------#
def crearUniverso(request):

    try:
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        imagen = request.POST["imagen"]

        universo = Universo.objects.create(id=codigo,nombre=nombre,descripcion=descripcion,image_url=imagen)
        messages.success(request, "Universo Creado Correctamente")
        return redirect("../infoUniverso/"+codigo)
    except:
        messages.success(request,"Esto no se pudo guardar")
        return redirect("/registrarUniverso/")

#-------------------------------------//-----------------------------------#

def modificarUniverso(request,codigo):
    universo = Universo.objects.get(id=codigo)
    return render(request,"editaruniverso.html",{"universo":universo})

#-------------------------------------//-----------------------------------#

def editarUniverso(request):

    try:
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        imagen = request.POST["imagen"]

        universo = Universo.objects.get(id=codigo)
        universo.nombre = nombre
        universo.descripcion = descripcion 
        universo.image_url = imagen
        universo.save()

        messages.success(request, "Universo editado Correctamente")
        return redirect("../infoUniverso/"+codigo)
    except:
        messages.success(request, "Error al editar el universo")
        return redirect("../modificarUniverso/"+codigo)

#-------------------------------------//-----------------------------------#

def eliminarPersona(request,codigo):
    persona = Personaje.objects.get(codigo=codigo)
    messages.success(request,"Eliminado")
    persona.delete()
    return redirect('/')

#-------------------------------------//-----------------------------------#

def eliminarUniverso(request,codigo):
    universo = Universo.objects.get(id=codigo)
    messages.success(request,"Eliminado")
    universo.delete()
    return redirect('/')

#-------------------------------------//-----------------------------------#

def infoUniverso(request,codigo):
    universo = Universo.objects.get(id=codigo)
    return render(request,"informacionuniverso.html",{"universo":universo})

def infoPersonaje(request,codigo):
    personaje = Personaje.objects.get(codigo=codigo)
    return render(request,"informacionPersonaje.html",{"persona":personaje})
