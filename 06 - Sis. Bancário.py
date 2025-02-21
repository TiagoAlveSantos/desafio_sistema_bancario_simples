#!/usr/bin/env python
# coding: utf-8

# In[30]:


menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
LIMITE_DIARIO = 500
LIMITE_SAQUES = 3

saldo = float(0)
quantidade_saques = 0
extrato = ""

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        valor_deposito = float(input('Digite o valor que deseja depositar:'))
        if (valor_deposito <= 0):
            print("Valor Inválido, tente novamente.")
        else:
            saldo += float(valor_deposito)
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
    elif opcao == 's':
        valor_saque = float(input('Digite o valor que deseja sacar:'))
        if (valor_saque <= 0):
            print("Valor Inválido, tente novamente.")
        elif (quantidade_saques < LIMITE_SAQUES and valor_saque <= LIMITE_DIARIO and saldo >= valor_saque) :
            quantidade_saques += 1
            saldo -= float(valor_saque)
            print(f'Saque de {valor_saque} realizado com sucesso.')
            extrato += f'Saque de {valor_saque} realizado \n'
        elif valor_saque > saldo:
            print('Saldo insuficiente.')
        else:
            print("Operação Inválida, confira seu extrato.")
    elif opcao == 'e':
        print("\n=============== EXTRATO =================")
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print(f'Seu limite diário é de: R${LIMITE_DIARIO:.2f}')
        print(f'Você já realizou {quantidade_saques} saques hoje.')
        #if len(extrato) > 0:
            #print('\n' + extrato)
        print("==========================================")
    elif opcao == 'q':
        break
    else:
        print("Operação inválida. Selecione um menu.")

