from personaje import Personajes

class Alienz(Personajes):
  _galaxia_nacimiento:str
  def __init__(
    self, 
    nombre: str, 
    edad: int, 
    sexo: str, 
    descripcion: str,
    galaxia_nac:str,
  ) -> None:
    super().__init__(nombre, edad, sexo, descripcion)
    self._galaxia_nacimiento = galaxia_nac
    
  @property
  def galaxia_nacimiento(self)->str:
    return self._galaxia_nacimiento

  @galaxia_nacimiento.setter
  def galaxia_nacimiento(self,galaxia:str)->None:
    self._galaxia_nacimiento = galaxia
  
  
  
  
    