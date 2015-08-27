##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: capitulo 08\08.34 - Modulo entrada (entrada.py).py
##############################################################################





def valida_inteiro(mensagem, mínimo, máximo):
     while True:
         try:
               v = int(input(mensagem))
               if v >= mínimo and v <= máximo:
                   return v
               else:
                   print("Digite um valor entre %d e %d" % (mínimo, máximo))
         except:
               print("Você deve digitar um número inteiro")