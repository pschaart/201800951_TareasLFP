import json
import ClasePersona

ListaPersonas = []
matrizAmostra = []

def CargarDatos(ruta):
    with open(ruta) as contenido:
        Datos = json.load(contenido)
        for atributo in Datos:
            personaN = ClasePersona.Persona(atributo.get('nombre'),atributo.get('edad'),atributo.get('activo'),atributo.get('promedio'))
            ListaPersonas.append(personaN)

def MostrarDatos(condicion,valor):
    matrizAmostra = []
    auxcont = 0
    if condicion == 'nombre':
        for i in ListaPersonas:
            if ListaPersonas[i].Nombre == valor:
                matrizAmostra[auxcont][0] = ListaPersonas[i].Nombre
                matrizAmostra[auxcont][1] = ListaPersonas[i].Edad
                matrizAmostra[auxcont][2] = ListaPersonas[i].Activo
                matrizAmostra[auxcont][3] = ListaPersonas[i].Promedio
                auxcont = auxcont + 1
    elif condicion == 'edad':
        for i in ListaPersonas:
            if ListaPersonas[i].Edad == valor:
                matrizAmostra[auxcont][0] = ListaPersonas[i].Nombre
                matrizAmostra[auxcont][1] = ListaPersonas[i].Edad
                matrizAmostra[auxcont][2] = ListaPersonas[i].Activo
                matrizAmostra[auxcont][3] = ListaPersonas[i].Promedio
                auxcont = auxcont + 1
    elif condicion == 'activo':
        for i in ListaPersonas:
            if ListaPersonas[i].Activo == valor:
                matrizAmostra[auxcont][0] = ListaPersonas[i].Nombre
                matrizAmostra[auxcont][1] = ListaPersonas[i].Edad
                matrizAmostra[auxcont][2] = ListaPersonas[i].Activo
                matrizAmostra[auxcont][3] = ListaPersonas[i].Promedio
                auxcont = auxcont + 1
    elif condicion == 'promedio':
        for i in ListaPersonas:
            if ListaPersonas[i].Promedio == valor:
                matrizAmostra[auxcont][0] = ListaPersonas[i].Nombre
                matrizAmostra[auxcont][1] = ListaPersonas[i].Edad
                matrizAmostra[auxcont][2] = ListaPersonas[i].Activo
                matrizAmostra[auxcont][3] = ListaPersonas[i].Promedio
                auxcont = auxcont + 1
