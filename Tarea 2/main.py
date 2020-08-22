import Lector_Json
import Lecto_CSV
import Lector_XML

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('-----------Archivos del json------------')
    Lector_Json.CargarDatos('Datos.json')
    print('------------Archivo CSV --------------')
    Lecto_CSV.LeerDatos('Datos.csv')
    print('----------- Archivo XML--------------')
    Lector_XML.LeerDatos('Datos.xml')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
