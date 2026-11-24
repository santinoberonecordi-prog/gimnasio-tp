class Socio:
    def __init__(self, dni, nombre, tipo_membresia, dias_restantes):
        self.dni = dni
        self.nombre = nombre
        self.tipo_membresia = tipo_membresia
        self.dias_restantes = dias_restantes
        self.activo = True

    def getInfo(self):
        print("El DNI es:", self.dni)
        print("El nombre es:", self.nombre)
        print("La membresia es:", self.tipo_membresia)
        print("Los dias restantes son:", self.dias_restantes)
        if self.activo and self.dias_restantes > 0:
            print("El estado es: Activo")
        else:
            print("El estado es: Inactivo")

    def restarDia(self):
        if self.dias_restantes > 0:
            self.dias_restantes = self.dias_restantes - 1
        
        if self.dias_restantes <= 0:
            self.activo = False


class Gimnasio:
    def __init__(self, nombre_gimnasio):
        self.nombre_gimnasio = nombre_gimnasio
        self.socios = []  

    def setSocio(self, un_socio):
        
        encontrado = False
        for s in self.socios:
            if s.dni == un_socio.dni:
                encontrado = True
        
        if encontrado:
            print("Ya existe un socio registrado con el DNI:", un_socio.dni)
        else:
            self.socios.append(un_socio)
            print("Socio", un_socio.nombre, "registrado correctamente.")

    def darIngreso(self, dni):
        encontrado = False
        for s in self.socios:
            if s.dni == dni:
                encontrado = True
                if not s.activo or s.dias_restantes <= 0:
                    print("Ingreso denegado. La membresia de", s.nombre, "esta inactiva.")
                else:
                    s.restarDia()
                    print("Ingreso registrado a:", s.nombre)
                    print("Se ha descontado 1 dia. Dias restantes:", s.dias_restantes)
        
        if not encontrado:
            print("El DNI", dni, "no se encuentra registrado en el sistema.")

    def getActivos(self):
        print("LISTA DE SOCIOS ACTIVOS")
        contador = 0
        for s in self.socios:
            if s.activo and s.dias_restantes > 0:
                s.getInfo()
                print("-" * 20)
                contador = contador + 1
        print("Total de socios activos:", contador)

    def getInactivos(self):
        print("LISTA DE SOCIOS INACTIVOS")
        contador = 0
        for s in self.socios:
            if not s.activo or s.dias_restantes <= 0:
                s.getInfo()
                print("-" * 20)
                contador = contador + 1
        print("Total de socios inactivos:", contador)

    def getEstadoGeneral(self):
        print("ESTADO GENERAL:", self.nombre_gimnasio)
        total = len(self.socios)
        activos = 0
        inactivos = 0
        for s in self.socios:
            if s.activo and s.dias_restantes > 0:
                activos = activos + 1
            else:
                inactivos = inactivos + 1
        print("Total de socios registrados:", total)
        print("Socios activos:", activos)
        print("Socios inactivos:", inactivos)
                    
