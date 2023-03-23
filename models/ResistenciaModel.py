class Resistencia:

  bandas = [
      {'color': 'negro', 'valor': 0, 'clase': 'background-color: black;'},
      {'color': 'marron', 'valor': 1, 'clase': 'background-color: brown;'},
      {'color': 'rojo', 'valor': 2, 'clase': 'background-color: red;'},
      {'color': 'naranja', 'valor': 3, 'clase': 'background-color: orange;'},
      {'color': 'amarillo', 'valor': 4, 'clase': 'background-color: yellow;'},
      {'color': 'verde', 'valor': 5, 'clase': 'background-color: green;'},
      {'color': 'azul', 'valor': 6, 'clase': 'background-color: blue;'},
      {'color': 'violeta', 'valor': 7, 'clase': 'background-color: purple;'},
      {'color': 'gris', 'valor': 8, 'clase': 'background-color: gray;'},
      {'color': 'blanco', 'valor': 9, 'clase': 'background-color: white;'},
    ]
  tolerancias = [
      {'color': 'oro', 'valor': 1.05, 'clase': 'background-color: yellow;'},
      {'color': 'plata', 'valor': 1.10, 'clase': 'background-color: gray;'},
    ]

  @classmethod
  def colores(cls):
    colores = []
    for banda in cls.bandas:
      colores.append(banda['color'])
    return colores
  
  @classmethod
  def valores(cls):
    valores = []
    for banda in cls.bandas:
      valores.append(banda['valor'])
    return valores
  
  @classmethod
  def colorTolerancias(cls):
    colorTolerancias = []
    for tolerancia in cls.tolerancias:
      colorTolerancias.append(tolerancia['color'])
    return colorTolerancias
  
  @classmethod
  def colorTolerancias(cls):
    colores = []
    for tolerancia in cls.tolerancias:
      colores.append(tolerancia['color'])
    return colores
  
  @classmethod
  def multiplicadores(cls):
    multiplicadores = []
    for banda in cls.bandas:
      multiplicadores.append(banda['valor']*'0')
    return multiplicadores
  
  @classmethod
  def clases(cls):
    clases = []
    for banda in cls.bandas:
      clases.append(banda['clase'])
    return clases
  
  @classmethod
  def clasesTolerancia(cls):
    clases = []
    for tolerancia in cls.tolerancias:
      clases.append(tolerancia['clase'])
    return clases