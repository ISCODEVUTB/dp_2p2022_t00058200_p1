from personaje import Personajes

class Artificiales(Personajes):
  
  _laboratorio_creacion:str
  def __init__(
    self, 
    nombre: str, 
    edad: int, 
    sexo: str, 
    descripcion: str,
    laboratorio:str
  ) -> None:
    super().__init__(nombre, edad, sexo, descripcion)
    self._laboratorio_creacion = laboratorio
    
  @property
  def laboratorio(self)->str:
    return self._laboratorio_creacion

  @laboratorio.setter
  def laboratorio(self,laboratorio:str)->None:
    self._laboratorio_creacion = laboratorio

  
  
  
  
    