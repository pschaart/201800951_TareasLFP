class persona:
    def __init__(self,Nombre,Edad,Activo,Saldo):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Activo = Activo
        self.Saldo = Saldo


import webbrowser
jack = persona('Jack',20,'true',10000)
Marta = persona('Marta',20,'true',10000)
Grecia = persona('Grecia',20,'true',10000)
Federico = persona('Federico',20,'true',10000)
Raul = persona('Raul',20,'true',10000)
Willy = persona('Willy',20,'true',10000)
Fernando = persona('Fernando',20,'true',10000)
Canelo = persona('Canelo',20,'true',10000)
Ramon = persona('Ramon',20,'true',10000)
Carla = persona('Carla',20,'true',10000)



Lista =[jack,Marta,Grecia,Federico,Raul,Willy,Fernando,Canelo,Ramon,Carla]
f = open('lista.html','w')
f.write("""<html>
<head></head>
<body>""")
for i in Lista:
    mensaje = f"""
                <p>Nombre: {i.Nombre}</p>
                <p>Edad: {i.Edad}</p>
                <p>Activo: {i.Activo}</p>
                <p>Saldo: {i.Saldo}</p>
                <br>
                """
    f.write(mensaje)
f.write("""</body>
</html>""")
f.close()
webbrowser.open_new_tab('lista.html')