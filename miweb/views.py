from django.shortcuts import render, HttpResponse

def inicio(request):
    
    return render(request, "inicio.html")


def contacto(request):
    return render(request, "contacto.html")

def Lascondes(request):   
    ordcompetidores = ["Clínica Cordillera", "Clínica Las Condes", "Clínica San Carlos de Apoquindo", "Clínica Universidad de los Andes", "Hospital FACH", "Cesfam Apoquindo", "Integramedica Alto las Condes", "Integramedica Los Dominicos", "Integramedica Manquehue", "Hospital Dipreca", "Centro Médico Medicien", "Clínica Psiquiatrica Creser", "Pensionado San José", "Centro Médico y Dental Megasalud Arauco", "Centro Médico y Dental Megasalud Padre Hurtado", "Central Odontológica de la Fuerzas Armadas y de Orden", "Centro Médico Militar Rosa O'Higgins", "Centro Odontológico Uno Salud Dental Las Condes", "Clínica Milano", "Centro de Salud Familiar Apoquindo", "Centro de Salud Familiar Aníbal Ariztía", "Clínica Arauco Salud","Centro Asistencial AChS Las Condes", "Centro Médico y Dental Megasalud Kennedy", "Darvax Salud", "COSAM Las Condes", "SAPU Aníbal Ariztía", "Instituto Oftalmológico Puerta del Sol", "Clínica Paris SpA", "Centro Vida Integra de Las Condes", "VidaIntegra (El Bosque Norte)", "Integramedica  calle Neveria"]
    context = {"Place": ordcompetidores, "numcompetidores": len(ordcompetidores)}
    return render(request, "hlascondes.html", context)


def vitacura(request):
    vitacura = ["Clínica Tabancura", "Clínica Alemana", "COSAM Vitacura", "Centro de Salud Familiar Vitacura", "Clínica Lo Curro"]
    context = {"Place": vitacura, "numcompetidores": len(vitacura)}
    return render(request, "hvitacura.html", context)

def lobarnechea(request):
    lo_barnechea = ["SAPU Lo Barnechea","Centro Comunitario de Salud Familiar Bicentenario(Calle Getsemani 229)","Centro Comunitario de Salud Familiar Bicentenario(Calle Circunvalación Norte 5040)","Centro de Salud Familiar Lo Barnec"]
    context = {"Place": lo_barnechea, "numcompetidores": len(lo_barnechea)}
    return render(request, "hbarnechea.html", context)

def lareina(request):
    la_reina = ["fhuehief"]
    context = {"Place": la_reina, "numcompetidores": len(la_reina)}
    return render(request, "hlareina.html", context)


def formulario2(request):
    return render(request, "formulario2.html")

def respuesta(request):
    #context = 
    return render(request,"respform.html")
    