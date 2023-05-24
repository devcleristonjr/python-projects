
from calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)
    
    
def jogar(pontos:int) -> None:
    dificuldade: int = int(input('informe o nivel de dificudade desejado [1,2,3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)
    
    print('informe o resultado para a seguinte operacao:  ')
    calc.mostrar_operacao()
    
    resultado: int = int(input())
    
    if calc.checar_resultado(resultado):
        pontos +=  1
        print(f'voce tem {pontos} ponto(s).')
              
    continuar : int = int(input('Deseja Continuar no jogo? [1- sim, 0- nao]'))
    
    if continuar:
        jogar(pontos)
    else:
        print(f'voce finalizou com {pontos} ponto(s). ') 
        print('ate a proxima')   
    
if __name__ == '__main__':
    main()
    
