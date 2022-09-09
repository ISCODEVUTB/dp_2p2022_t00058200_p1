from abc import ABC

# clase abstracta que sera usada por los personajes
class Personajes(ABC):
  _nombre:str
  _edad:int
  _sexo:str
  _descripcion:str
  """
  constructor de la clase, 
  """
  def __init__(
    self,
    nombre:str,
    edad:int,
    sexo:str,
    descripcion:str
  ) -> None:
    self._nombre = nombre
    self._edad = edad
    self._sexo = sexo
    self._descripcion = descripcion
    self._liga = []
    
  # getters methods
  @property  
  def nombre(self)->str:
    return self._nombre
  @property    
  def edad(self)->int:
    return self._edad
  @property  
  def sexo(self)->str:
    return self._sexo
  @property  
  def descripcion(self)->str:
    return self._descripcion
  
  #setters methods  
  @nombre.setter  
  def nombre(self,nombre)->None:
    self._nombre = nombre
  @edad.setter    
  def edad(self,edad)->None:
    self._edad = edad
  @sexo.setter  
  def sexo(self,sexo)->None:
    self._sexo = sexo
  @descripcion.setter  
  def descripcion(self,descripcion)->None:
    self._descripcion = descripcion

  