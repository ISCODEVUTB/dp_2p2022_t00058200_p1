from personaje import Personajes

class SuperHumanos(Personajes):
  
  _continente_nacimiento:str
  def __init__(
    self, 
    nombre: str, 
    edad: int, 
    sexo: str, 
    descripcion: str,
    cont_nac:str
  ) -> None:
    super().__init__(nombre, edad, sexo, descripcion)
    self._continente_nacimiento = cont_nac
    
  @property
  def continente_nacimiento(self)->str:
    return self._continente_nacimiento

  @continente_nacimiento.setter
  def continente_nacimiento(self,continente_nac)->None:
    self._continente_nacimiento = continente_nac

  
  
  
  
    