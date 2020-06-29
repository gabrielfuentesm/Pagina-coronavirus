from django.shortcuts import render, HttpResponse

def inicio(request):
    
    ordcompetidores = ["Clinica Alemana", "Clinica Las Condes", "Clinica U. Cátolica", "Clinica Universidad de los Andes"]
    context = {"Place": ordcompetidores, "numcompetidores": len(ordcompetidores)}
    return render(request, "inicio.html", context)


def contacto(request):

    
    return render(request, "contacto.html")

def Lascondes(request):
    
    ordcompetidores = ["Clinica Alemana", "Clinica Las Condes", "Clinica U. Cátolica", "Clinica Universidad de los Andes"]
    context = {"Place": ordcompetidores, "numcompetidores": len(ordcompetidores)}
    return render(request, "hlascondes.html", context)



