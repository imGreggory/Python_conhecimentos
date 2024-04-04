# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada 
# com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | profissão: {self.profissao}"
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Olá! meu nome é {self.nome}, tenho {self.idade} e trabalho como {self.profissao}."
    
profissao1 = Pessoa("anthony", 20, "Programador")

print(profissao1)
print(profissao1.saudacao)

#após o aniversário
profissao1.aniversario()
print(profissao1.saudacao)