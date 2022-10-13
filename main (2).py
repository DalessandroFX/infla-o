class inflacao():
    def __init__(self,prod):
        self.prod= prod
    def preco(self,preco):
        self.preco=preco
    def set_preco(self,infla):
        if infla > 100:
            infla = 100
        self.preco = (self.preco * (infla/100)) + self.preco
    def get_prod(self):
        return self.prod
    def get_preco(self):
        return self.preco
prod1 = inflacao(str(input("qual o nome do produto:")))
prod1.preco(float(input("quanto custa esse produto ano passado?")))
prod1.set_preco(float(input("quanto foi a inflacao do ano passado para esse em %?")))
print("o valor de", prod1.get_prod(), " hoje em dia é ", prod1.get_preco())
prod2 = inflacao(str(input("qual o nome do produto:")))
prod2.preco(float(input("quanto custa esse produto ano passado?")))
prod2.set_preco(float(input("quanto foi a inflacao do ano passado para esse em %?")))
print("o valor de", prod2.get_prod(), " hoje em dia é ", prod2.get_preco())