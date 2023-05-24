from random import randint

class Calcular:
    def __init__(self: object, dificuldade: int, /) -> None:
        # Inicializa a classe Calcular com os parâmetros de dificuldade
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 somar / 2 subtrair / 3 multiplicar
        self.__resultado: int = self._gerar_resultado
        
    @property
    def dificuldade(self: object) -> int:
        # Retorna a dificuldade da operação
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        # Retorna o valor1 gerado aleatoriamente
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        # Retorna o valor2 gerado aleatoriamente
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        # Retorna o tipo de operação: 1 para soma, 2 para subtração, 3 para multiplicação
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        # Retorna o resultado da operação
        return self.__resultado
    
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operacao Desconhecida'
            
        # Retorna uma representação em string da operação com os valores, dificuldade e tipo de operação
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperacao: {op}'
    
    @property
    def _gerar_valor(self: object) -> int:
        # Gera um valor aleatório com base na dificuldade
        if self.dificuldade == 1:
            return randint(0,10)
        elif self.dificuldade == 2:
            return randint(0,100)
        elif self.dificuldade == 3:
            return randint(0,1000)
        elif self.dificuldade == 4:
            return randint(0,10000)
        else:
            return randint(0,100000)
    
    @property
    def _gerar_resultado(self: object) -> int:
        # Gera o resultado da operação com base nos valores e no tipo de operação
        if self.operacao == 1: #somar
            return self.valor1 + self.valor2
        elif self.operacao == 2: #subtrair
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
        
    @property
    def _op_simbolo(self:object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'
    
        
    def checar_resultado(self: object, resposta: int) -> bool:
        # Verifica se a resposta fornecida pelo usuário está correta
        certo : bool = False
        
        if self.resultado == resposta:
            print('Resposta Correta')
            certo = True
        else:
            print('Resposta Errada')
            print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
            return certo
        
        
    def mostrar_operacao(self: object) -> None:
        # Mostra a operação ao usuário
        print(f'{self.valor1} {self._op_simbolo} {self.valor2}')