import re
import Lector_Json

print('--------------------------------------------------\n'
      'Bienvenido a SimpleQL\n'
      'Utilize el comando CARGAR,SELECCIONAR,MAXIMO,MINIMO,SUMA,CUENTA,REPORTAR\n'
      '---------------------------------------------------')

comando = input()
Accion = re.split('\s',comando,maxsplit=1)

if Accion[0].lower() == 'cargar':
      Interpretada = re.split(',|\s',comando)
      print(Interpretada)
      for i in range(1,len(Interpretada),1):
            if Interpretada[i] == '':
                  print('')
            else:
                  Lector_Json.CargarDatos(Interpretada[i])

if Accion[0].lower() == 'seleccionar':
      SPL1 = re.split(' donde ', Accion[1])
      SPL2 = re.split(' = ',SPL1[1])
      RECN = re.search('nombre',SPL1[0].lower())
      RECE = re.search('edad',SPL1[0].lower())
      RECA = re.search('activo',SPL1[0].lower())
      RECP = re.search('promedio',SPL1[0].lower())
      Lector_Json.MostrarDatos(SPL2[0],SPL2[1])
      for f in range(len(Lector_Json.matrizAmostra)):
            for c in range(len(Lector_Json.matrizAmostra[0])):
                  print(Lector_Json.matrizAmostra[f][c],end='')
            print()




