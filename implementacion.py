grafo_contenido= {
  "Noticias": ["Maridis", "Luna", "Carlos", "Jose", "Gustavo"],
  "Entretenimiento": ["Maridis", "Ana", "Luna", "Berenice", "Gustavo", "Kevin"],
  "Memes": ["Ana", "Miladis", "Kevin"],
  "Politica": ["Carlos", "Juan"],
  "Educacion": ["Ana", "Berenice", "Carlos", "Jose", "Juan"],
  "Ventas" : ["Miladis", "Jose", "Gustavo"]
}

grafo_amigos={
    "Maridis": ["Ana", "Luna", "Gustavo"],
    "Ana" : ["Maridis"],
    "Luna" : ["Maridis", "Miladis", "Jose"],
    "Miladis": ["Luna", "Kevin"],
    "Berenice": ["Jose"],
    "Carlos": ["Juan"],
    "Jose": ["Luna","Berenice"],
    "Gustavo": ["Maridis"],
    "Kevin": ["Miladis"],
    "Juan": ["Carlos"]  
}

latencia={
    "Servidor": {"Kevin": 15, "Juan": 10},
    "Kevin": {"Servidor": 15, "Juan": 7, "Carlos": 27, "Maridis": 70},
    "Juan": {"Servidor": 10, "Miladis": 8, "Berenice": 45, "Kevin": 7},
    "Miladis": {"Juan": 8, "Luna": 27},
    "Maridis": {"Carlos": 20, "Kevin": 70},
    "Carlos": {"Kevin": 27, "Maridis": 20, "Gustavo": 40, "Berenice": 50},
    "Berenice": {"Juan": 45, "Carlos": 50, "Gustavo": 30, "Ana": 35, "Luna": 40}, 
    "Luna": {"Miladis": 25, "Berenice": 45, "Ana": 17},
    "Ana": {"Berenice": 35, "Luna": 17, "Jose": 8}, 
    "Gustavo": {"Jose": 5, "Carlos": 40, "Berenice": 30},
    "Jose": {"Gustavo": 5, "Ana": 8},  
}

def encontrar_amigos_en_comun(grafo_amigos, persona1, persona2):
  if persona1 == persona2:
    return []
  amigos_persona1 = grafo_amigos[persona1]
  amigos_persona2 = grafo_amigos[persona2]
  amigos_en_comun = []
  for amigo in amigos_persona1:
    if amigo in amigos_persona2 and amigo != persona1 and amigo != persona2:
      amigos_en_comun.append(amigo)
  if not amigos_en_comun:
    print(f"***No hay amigos en común entre {persona1} y {persona2}***")
  return amigos_en_comun

def dijkstra_latencia(grafo, origen, destino):
  distancia = {nodo: float('inf') for nodo in grafo}
  distancia[origen] = 0
  visitados = set()
  anterior = {nodo: None for nodo in grafo}
  while visitados != grafo.keys():
    nodo_actual = min((nodo for nodo in grafo if nodo not in visitados), key=lambda nodo: distancia[nodo])
    visitados.add(nodo_actual)
    for vecino, peso in grafo[nodo_actual].items():
      if vecino not in visitados:
        nueva_distancia = distancia[nodo_actual] + peso
        if nueva_distancia < distancia[vecino]:
          distancia[vecino] = nueva_distancia
          anterior[vecino] = nodo_actual
  camino = []
  nodo_actual = destino
  while nodo_actual is not None:
    camino.append(nodo_actual)
    nodo_actual = anterior[nodo_actual]
  camino.reverse()
  return distancia[destino], camino

def buscar_por_contenido(grafo_contenido, contenido):
  if contenido not in grafo_contenido:
    return []
  usuarios = grafo_contenido[contenido]
  return usuarios


while True:
    print("Escoge una opcion")
    print("1. Buscar Amigos En Comun")
    print("2. Buscar latencia entre usuarios")
    print("3. Mostrar Comunidad")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_1 = input("Ingrese el primer nombre: ").capitalize()
        nombre_2 = input("Ingrese el segundo nombre: ").capitalize()
        amigos_en_comun = encontrar_amigos_en_comun(grafo_amigos, nombre_1, nombre_2)
        print(amigos_en_comun)

    if opcion == "2":
      nombre_1 = input("Ingrese el primer nombre: ").capitalize()
      nombre_2 = input("Ingrese el segundo nombre: ").capitalize()
      nombre_1 = nombre_1.replace(" ", "-")
      nombre_2 = nombre_2.replace(" ", "-")
      distancia, camino = dijkstra_latencia(latencia, nombre_1, nombre_2)
      print(f"Latencia más corta desde {nombre_1} a {nombre_2}: {distancia}")
      print(f"Camino: {' -> '.join(camino)}")

    if opcion == "3":
      contenido_buscado = input("Buscar por tipo de contenido: ").capitalize()
      usuarios_que_ven_contenido = buscar_por_contenido(grafo_contenido, contenido_buscado)
      print(f"Los usuarios que ven {contenido_buscado} son: {usuarios_que_ven_contenido}")

    if opcion == "4":
      break
