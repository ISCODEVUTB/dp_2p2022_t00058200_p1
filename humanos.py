
from personaje import Personajes

class Humanos(Personajes):
  _continente_nacimiento:str
  _color_piel:str
  def __init__(
    self, 
    nombre: str, 
    edad: int, 
    sexo: str, 
    descripcion: str,
    cont_nac:str,
    color:str
  ) -> None:
    super().__init__(nombre, edad, sexo, descripcion)
    self._continente_nacimiento = cont_nac
    self._color_piel = color
    
  @property
  def continente_nacimiento(self)->str:
    return self._continente_nacimiento

  @continente_nacimiento.setter
  def continente_nacimiento(self)->None:
    return self._continente_nacimiento
  
  @property
  def color(self)->str:
    return self._color_piel

  @color.setter
  def color(self,color:str)->None:
    self._color_piel = color

  
  
  
  
    