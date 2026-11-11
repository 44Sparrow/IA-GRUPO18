class Grafo:
    def __init__(self):
        self.locais = {}
        self.ligacoes = {}

    def adicionar_local(self, id_local, tipo, posicao):
        if id_local not in self.locais:
            self.locais[id_local] = {'tipo': tipo, 'posicao': posicao}
            self.ligacoes[id_local] = []

    def adicionar_ligacao(self, origem, destino, custo, bidirecional=True):
        if origem not in self.locais:
            raise ValueError(f"Local de origem '{origem}' não existe.")
        if destino not in self.locais:
            raise ValueError(f"Local de destino '{destino}' não existe.")
        self.ligacoes[origem].append({'destino': destino, 'custo': custo})
        if bidirecional:
            self.ligacoes[destino].append({'destino': origem, 'custo': custo})

    def vizinhos(self, id_local):
        if id_local not in self.locais:
            raise ValueError(f"Local '{id_local}' não existe.")
        return self.ligacoes[id_local]

    def tem_local(self, id_local):
        return id_local in self.locais

    def custo(self, origem, destino):
        if origem not in self.locais or destino not in self.locais:
            raise ValueError("Um ou ambos os locais não existem.")
    
        for ligacao in self.ligacoes[origem]:
            if ligacao["destino"] == destino:
                return ligacao["custo"]
    
        raise ValueError(
            f"Não existe ligação entre {origem} e {destino}."
        )