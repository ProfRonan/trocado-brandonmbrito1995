"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    
    valor = float(input('Digite um valor entre 0.00 e 10.00: '))

    total = valor
    moeda = 1.00
    totmoe = 0

    while True:
      if total >= moeda:
        total -= moeda
        totmoe +=  1
    else:
      if totmoe > 0:
        print('São necessárias: ')
        print(f'Total de {totmoe} moedas de R${moeda}')
      if moeda == 1.00:
           moeda = 0.50
      elif moeda == 0.50:
           moeda = 0.25
      elif moeda == 0.25:
           moeda = 0.10
      elif moeda == 0.10:
           moeda = 0.05
      elif moeda == 0.05:
           moeda = 0.01
           totmoe = 0
      if total == 0:
        break

if __name__ == '__main__':
    main()
