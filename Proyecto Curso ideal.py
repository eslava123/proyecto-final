from clase import Datos


def inicio():
    print("\n" + '*'*31 + '\n' + '*'*9 + ' Curso Ideal '  + '*'*9 + '\n' + '*'*31)
    
    id = input("\nIngrese Id: ")
    nombre = input("Ingrese su nombre: ")
    Usuario=Datos(id,nombre)
   
    
    while True:
        print("""
        0. Salir
        1.Empezar a programar Clases
        2.Ver mis clases guardadas
        """
    )

        opcion=int(input("seleccione la opcion: "))
        
        
        
                 
        if opcion==0:
            archivo=open("guardado.txt","a")
            archivo.truncate(0)
            print("registros eliminados")
            break
           

            
        if opcion==1:
            
            while True:
                ubicacion = input("\n---Ingrese municipio de residencia: ")
                if ubicacion == "bucaramanga" or ubicacion == "piedecuesta" or ubicacion == "terrazas" or ubicacion == "floridablanca":
                    
                    break
                else:
                    print("ubicacion invalida, escribala de nuevo")
            if ubicacion == "bucaramanga":
                sede="Jardin"
                print(f"su cede mas cercana es la de {sede}")
            elif ubicacion == "piedecuesta" or ubicacion=="floridablanca":
                sede="El bosque"
                print(f"su cede mas cercana es la de {sede}")
            elif ubicacion=="terrazas":
                sede="CSU"
                print(f"su cede mas cercana es la de {sede}")



            while True:
                materia = input(f"\n---Ingrese Materia que desea agendar en la sede {sede}: ")
                if materia == "calculo integral" or materia == "mecanica y laboratorio" or materia == "matematica financiera":
                    
                    break
                else:
                    print("materia invalida, escribala de nuevo")
                    
            if materia=="calculo integral" and sede=="Jardin":
                profesor="Ivan"
                horario="Lunes 6 a 8am"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="calculo integral" and sede=="CSU":
                profesor="Saul Goodman"
                horario="Miercoles 6 a 8am"
                print("profesor: ",profesor)
                print("horario: ",horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="calculo integral" and sede=="El bosque":
                profesor="Walter White"
                horario="Lunes 6 a 8am"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            


            elif materia=="mecanica y laboratorio" and sede=="Jardin":
                profesor="Martha"
                horario="Martes 6 a 8am"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="mecanica y laboratorio" and sede=="CSU":
                profesor="Daniel Ruiz"
                horario="Miercoles 4 a 6pm"
                print("profesor: ",profesor)
                print("horario: ",horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="mecanica y laboratorio" and sede=="El bosque":
                profesor="Lionel Messi"
                horario="Viernes de 6 a 8m"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")



            elif materia=="matematica financiera" and sede=="Jardin":
                profesor="Jesse Pinkman"
                horario="Miercoles 8 a 11am"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="matematica financiera" and sede=="CSU":
                profesor="Huell babineux"
                horario="jueves 6 a 10pm"
                print("profesor: ",profesor)
                print("horario: ",horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            elif materia=="matematica financiera" and sede=="El bosque":
                profesor="Cristiano Ronaldo"
                horario="Viernes de 5 a 8pm"
                print(profesor)
                print(horario)
                print(f"Su sede mas proxima es {sede} por lo que verá {materia} con el profesor {profesor} en un horario de {horario}")
            
            

         #Aca se guarda en el archivo externo        
            archivo=open("guardado.txt","a")
            archivo.write("-")
            archivo.write(sede)
            archivo.write(",")
            archivo.write(materia)
            archivo.write(",")
            archivo.write(profesor)
            archivo.write(",")
            archivo.write(horario)
            archivo.write("\n")
           
            archivo.close()

            
            
        if opcion==2:
            print(Usuario.ID)
            print("\n Nombre: ",Usuario.nombre)
            print("Las clases que has registrado son las siguientes: ")
            archivo=open("guardado.txt","r")
            leer=archivo.read()
            print(leer)
            
            archivo.close

       
    #Acaba el programa
   




inicio()