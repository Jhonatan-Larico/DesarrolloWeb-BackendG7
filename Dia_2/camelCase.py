class CamelCase(): 
    def __init__(self, string):
        self.string = string 

    def hump(self):
        split = self.string.split(" ")
        s = ' '.join([x.capitalize() for x in split ])        
        return(s)
        

resultado = CamelCase("hola como estan")
print(resultado.hump())