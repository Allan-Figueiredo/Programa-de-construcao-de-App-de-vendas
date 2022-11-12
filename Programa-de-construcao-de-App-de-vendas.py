print('Programa de construção de App de vendas de Allan Figueiredo')

valorProduto = float(input(' Qual o valor do produto ? '))
quantidadeProduto = int(input(' Qual a quantidade deste produto ? '))
if quantidadeProduto < 10:
    valorPagar = valorProduto * quantidadeProduto
    print ('O valor será de {:.2f} Reais'.format (valorPagar))
elif 10 <= quantidadeProduto < 100:
    valorPagar = valorProduto * quantidadeProduto
    valorDesconto = valorPagar - (valorPagar * 0.05)
    print ( 'O valor sem o desconto será de {:.2f} Reais'.format(valorPagar))
    print ( 'O valor com o desconto será de {:.2f} Reais - 5%'.format(valorDesconto))
elif 100 <= quantidadeProduto < 1000:
    valorPagar = valorProduto * quantidadeProduto
    valorDesconto = valorPagar - (valorPagar * 0.10)
    print('O valor sem o desconto será de {:.2f} Reais'.format(valorPagar))
    print ( 'O valor com o desconto será de {:.2f} Reais - 10%'.format(valorDesconto))
else:
    valorPagar = valorProduto * quantidadeProduto
    valorDesconto = valorPagar - (valorPagar * 0.15)
    print('O valor sem o desconto será de {:.2f} Reais'.format(valorPagar))
    print('O valor com o desconto será de {:.2f} Reais - 15%'.format(valorDesconto))