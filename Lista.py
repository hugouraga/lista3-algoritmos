class No:
    def __init__(self,item = None,proximo = None):
        self.item = item
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanhoLista = 0

    def vazia(self):
        return self.primeiro == self.ultimo

    def inserir(self,item):
        self.ultimo.proximo = No(item)
        self.ultimo = self.ultimo.proximo
        self.tamanhoLista += 1

    def inserirAresNaoDire(self,verticeA,verticeB,peso=1):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeA and not aux is None:
            aux = aux.proximo
            verificador += 1
        aux.item.append((verticeB,peso))
        verificador = 0
        aux = self.primeiro.proximo
        while verificador < verticeB and not aux is None:
            aux = aux.proximo
            verificador += 1
        aux.item.append((verticeA,peso))

    def inserirAresDire(self,verticeA,verticeB,peso=1):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeA and not aux is None:
            aux = aux.proximo
            verificador += 1
        aux.item.append((verticeB,peso))

    def removeAresta(self,verticeA,verticeB):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeA and not aux is None:
            aux = aux.proximo
            verificador += 1
        listaVerticeA = aux.item

        for elementos in listaVerticeA:
            if elementos[0] == verticeB:
                item = elementos
                listaVerticeA.remove(item)

        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeB and not aux is None:
            aux = aux.proximo
            verificador += 1
        listaVerticeB = aux.item
        print(listaVerticeB)
        for elementos in listaVerticeB:
            if elementos[0] == verticeA:
                item = elementos
                listaVerticeB.remove(item)
    def verificaAresta(self,verticeA,verticeB):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < verticeA and not aux is None:
            aux = aux.proximo
            verificador += 1
        listaVerticeA = aux.item
        verificador = 0
        aux = self.primeiro.proximo
        while verificador < verticeB and not aux is None:
            aux = aux.proximo
            verificador += 1
        listaVerticeB = aux.item
        existe = 0
        for primeiro in listaVerticeA:
            if primeiro[0] == verticeB:
                existe += 1
        for segundo in listaVerticeB:
            if segundo[0] == verticeA:
                existe += 1
        if existe != 0:
            return True
        else:
            return False

    def grauSaida(self,vertice):
        aux = self.primeiro.proximo
        verificador = 0
        while verificador < vertice and not aux is None:
            aux = aux.proximo
            verificador += 1
        listaTam = len(aux.item)
        return listaTam

    def grauEntrada(self,vertice):
        aux = self.primeiro.proximo
        grau = 0
        while not aux is None:
            vetor = aux.item
            for elemento in vetor:
                if elemento[0] == vertice:
                    grau += 1
            aux = aux.proximo
        print(grau)
        return grau
    def listaAd(self,vertice):
        aux = self.primeiro.proximo
        verificador  = 0
        while verificador < vertice and not aux is None:
            aux = aux.proximo
            verificador += 1
        lista = aux.item
        return lista

    def pesquisa(self, item):
        aux = self.primeiro.proximo
        while not aux is None and aux.item != item:
            aux = aux.proximo
        return aux is None and None or aux.item

    def removerInicio(self):
        if self.vazia():
            return None
        aux = self.primeiro.proximo
        self.primeiro.proximo = aux.proximo
        item = aux.item
        if aux == self.ultimo:
            self.ultimo = self.primeiro
        aux.proximo = None
        del aux
        return item

    def removerFim(self):
        if self.vazia():
            return None
        aux = self.primeiro
        while aux.proximo != self.ultimo:
            aux = aux.proximo
        item = self.ultimo.item
        ultimo = aux
        aux = ultimo.proximo
        ultimo.proximo = None
        del aux
        return item

    def __str__(self):
        s = "["
        aux = self.primeiro.proximo
        while not aux is None:
            s += str(aux.item) + ','
            aux = aux.proximo
        s = s.strip(",")
        s += "]"
        return s

    def __getitem__(self, index):
        if self.vazia():
            return IndexError("A lista se encontra vazia")
        if index > tamanhoLista or index < 0:
            return IndexError("index inválido")
        aux = self.primeiro.proximo
        ponteiro = 0
        while index > ponteiro:
            aux = aux.proximo
            ponteiro += 1
        if ponteiro == index:
            return aux.valor

    def __len__(self):
        return self.tamanhoLista
