class Pilha():
    def __init__(self):
        self.items=[]
    def vazia(self):
        return self.items==[]
    def topo(self):
        return self.items[len(self.items)-1]
    def tamanho(self):
        return len(self.items)
    def empilha(self,e):
        self.items.append(e)
    def desempilha():
        return self.items.pop()
def verifica(exp):
    p=Pilha()
    for i in exp:
        if i =='(':
            p.empilha(i)
        else:
            if p.vazia():
                return False
    else:
            p.desempilha()
    if p.vazia():
        return True
    else:
        return False

            
            
            
        
