# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia crear las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.


class Person:
    def __init__(self,name,birthDate,nationality,dni) :
        self.name = name
        self.nationality = nationality
        self.__dni = dni 
        self.__birthDate = birthDate

    def privateInfo(self):
        return {
            "DNI":self.__dni,
            "Fecha de nacimiento":self.__birthDate
        }

class Student(Person):    
    def __init__(self,course,name,birthDate,nationality,dni ):
        self.course = course
        # invoking  __init__ of the parent class
        Person.__init__(self,name,birthDate,nationality,dni)
        

    def info(self):      
        studend ={
                    "Nombre":self.name,
                    "Curso":self.course,              
                    "Nacionalidad":self.nationality, 
                }
        for k, v in studend.items():
            print(f"{k}: {v}")

    def privateInfo(self):
        # private info 
        privateInfo = super().privateInfo()

        print("-----Información Privada------")   
        for k, v in privateInfo.items():
            print(f"{k}: {v}")

class Teacher(Person):
    def __init__(self,socSecurity,ctsAccount,name,birthDate,nationality,dni):
        self.__socSecurity = socSecurity
        self.__ctsAccount = ctsAccount
        super().__init__(name,birthDate,nationality,dni)

    def info(self):
        print(            
                "Nombre:",self.name,"\n"
                "Nacionalidad:",self.nationality,          
        )

    def privateInfo(self):
        privateInfo = super().privateInfo()

        print("-----Información Privada------")        
        print("DNI:",privateInfo["DNI"])
        print("birthDate:",privateInfo["Fecha de nacimiento"])
        print("Cuenta CTS:",self.__ctsAccount)
        print("Seguro Social:",self.__socSecurity)



print("Estudiante")
student1 = Student("Quimica","Juan","2000-01-13","Perú","123456789")
student1.info()
student1.privateInfo()
print()

print("Profesor")
profesor1 = Teacher("12-ad","123-da","Alberto","1990-02-22","Perú","232452345" )
profesor1.info()
profesor1.privateInfo()
