from Lista import Lista

class Grafo:
    def __init__(self,quantVertices = 0,grafoDirecionado=False,pesoAresta=None):
        self.quantVertices = quantVertices
        self.listaVertices = Lista()
        self.grafoDirecionado = grafoDirecionado
        self.pesoAresta = pesoAresta
        for elemento in range(quantVertices):
            self.listaVertices.inserir([])

    def vazia(self):
        return self.quantVertices == 0

    def inseAres(self,verticeA,verticeB,grafoDirecionado=None,peso=1):
        if grafoDirecionado == False:
            self.listaVertices.inserirAresNaoDire(verticeA,verticeB,peso)
        elif grafoDirecionado == True:
            self.listaVertices.inserirAresDire(verticeA,verticeB,peso)

    def verifica(self,verticeA,verticeB):
        aux = self.listaVertices.verificaAresta(verticeA,verticeB)
        return aux

    def removeAresta(self,verticeA,verticeB):
        self.listaVertices.removeAresta(verticeA,verticeB)

    def grauEntrada(self,vertice):
        grau = self.listaVertices.grauEntrada(vertice)
        return grau

    def grauSaida(self,vertice):
        aux = self.listaVertices.grauSaida(vertice)
        print(aux)
        return aux

    def listaAdjacentes(self,vertice):
        lista = self.listaVertices.listaAd(vertice)
        return lista

    def __str__(self):
        #return self.listaVertices.__str__()
        aux = 0
        tamanhoLista = self.listaVertices.__len__()
        objeto = self.listaVertices.primeiro.proximo
        s = ""
        while aux < tamanhoLista:
            s += str(aux) + " = " + str(objeto.item)
            s += "\n"
            aux += 1
            objeto = objeto.proximo
        return s
    def __len__(self):
        return self.quantVertices

def extract(Q, w):
        m=0
        minimum=w[0]
        for i in range(len(w)):
                if w[i]<minimum:
                        minimum=w[i]
                        m=i
        return m, Q[m]

def grafoVetor(G):
    vetor = []
    node = G.listaVertices.primeiro.proximo
    i = 0
    while not node is None:
        vetor.append(node.item)
        i += 1
        node = node.proximo
    return vetor
def dijkstra(vetor,src,dest,visited=[],distances={},predecessors={}):
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            print(distances)
            print(predecessors)
            x  = predecessors.values()
            soma = 0
            for caminho in x:
                soma += caminho
        print('O menor caminho para: '+str(path)+" é com o custo="+str(soma))
    else :
        if not visited:
            distances[src]=0
        # visit the neighbors
        contador = 0
        for neighbor in vetor[src]:
            if neighbor[0] not in visited:
               # print(distances[src] + vetor[src][contador][1])
                new_distance = distances[src] + vetor[src][contador][1]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor[0]] = new_distance
                    predecessors[neighbor] = neighbor[1]
                contador += 1
        visited.append(src)
        unvisited={}
        for k in range(len(vetor)):
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        dijkstra(vetor,x,dest,visited,distances,predecessors)

