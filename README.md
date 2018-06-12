# lista3-algoritmos

Q1 - Dado o grafo abaixo, escreva uma função que calcule a menor distância de S a T, ou
seja, o custo de um caminho mínimo que começa em S e termina em T.

A1 - ​Dê a seqüência de valores dos dados de controle ao final de cada iteração durante a
execução do algoritmo para encontrar a Árvore Geradora de Peso Mínimo, quando a
entrada é dada pela lista de incidências abaixo.
1 - (3,9), (5,5), (4,1)
2 - (3,2), (4,2), (5,2)
3 - (1,9), (2,2), (5,3)
4 - (1,1), (2,2), (5,2)
5 - (1,5), (3,3), (4,2), (2,2)

C1 - ​O código a seguir está errado​. Descubra o que o código deveria fazer, quais são os
erros e conserte-o. Altamente recomendado que nessa questão você use o debugger do
Eclipse ou alguma outra IDE com um bom debugger.

    def Funcao(self):
        resultado =[]
        i = 0
        e = 0
        self.grafo = sorted(self.grafo,key=lambda item: item[2])
        pai = [] ; posicao = []
        for no in range(self.V):
            pai.append(no)
            posicao.append(0)
            
        while e < self.V -1 :
            u,v,w = self.grafo[i]
            i = i + 1
            x = self.find(pai, u)
            y = self.find(pai ,v)
            if x != y:
                e = e + 1
                resultado.append([u,v,w])
                self.union(pai, posicao, x, y)

        print "Arestas construídas:"
        for u,v,peso in resultado:
            print ("%d -- %d == %d" % (u,v,peso))
