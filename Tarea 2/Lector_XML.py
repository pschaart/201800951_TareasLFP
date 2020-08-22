import xml.etree.ElementTree as ET

def LeerDatos(Ruta):
    Archivo = ET.parse(Ruta)
    Registro = Archivo.getroot()

    for x in Registro.findall('Estudiante'):
        print(x.find('Nombre').text)
        print(x.find('Carnet').text)
        print(x.find('Carrera').text)
        print(x.find('DPI').text)
        print('')
