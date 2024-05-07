candidatos = {
    'Vaga1':[],
    'Vaga2':[]
}

print(f'''===============================
 Bem-vindo a porta de entrada
  para o mercado de trabalho!
===============================\n'''
        )

while True:
    aptos1 = []
    aptos2 = []
    vaga = int(input(f'''Para qual vaga deseja se candidatar?
        1 = Vaga 1
        2 = Vaga 2
        0 = Sair
: '''))
   
    if vaga == 1:
        nome = input('Nome completo: ')
        minibio = input('Resuma suas qualificações a seguir: ')
        candidatos['Vaga1'].append({nome:minibio})

    elif vaga == 2:
        nome = input('Nome completo: ')
        minibio = input('Resuma suas qualificações a seguir: ')
        candidatos['Vaga2'].append({nome:minibio})

    elif vaga == 0:
        for chave, lista in candidatos.items():
            for candidato in lista:
                for nome, bio in candidato.items():
                    if 'python' in bio or 'programação'in bio or 'desenvolvimento' in bio:
                        aptos1.append(nome)
                    elif 'análise de dados' in bio or 'dados' in bio or 'SQL' in bio:
                        aptos2.append(nome)  
        print(f'Para vaga 1 recemos {len(candidatos['Vaga1'])} inscrições de candidatos, onde {len(aptos1)} são aptos')
        print(f'Tiveram {len(candidatos['Vaga2'])} candidatos para Vaga 2 onde {len(aptos2)} são aptos')             
        break
    else:
        print('Erro!')

