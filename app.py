candidatos = {
    'Vaga1':[],
    'Vaga2':[]
}

def welcome():
    print(f'''===============================
 Bem-vindo a porta de entrada
  para o mercado de trabalho!
===============================\n'''
        )

def dadosCandidato(vaga):
    nome = input('Nome completo: \n')
    minibio = input('Resuma suas qualificações a seguir: \n')
    candidatos[vaga].append({nome:minibio})

def escolhendoAptos():
    aptos1 = []
    aptos2 = []
    for chave, lista in candidatos.items():
            for candidato in lista:
                for nome, bio in candidato.items():
                    if 'python' in bio or 'programação'in bio or 'desenvolvimento' in bio:
                        aptos1.append(nome)
                    elif 'análise de dados' in bio or 'dados' in bio or 'SQL' in bio:
                        aptos2.append(nome)  
    print(f'Para vaga 1 recebemos {len(candidatos['Vaga1'])} inscrições de candidatos, onde {len(aptos1)} são aptos\n')
    print(f'Para vaga 2 recebemos {len(candidatos['Vaga2'])} inscrições de candidatos, onde {len(aptos2)} são aptos') 

def main():
    welcome()
    while True:
        vaga = int(input(f'''\nPara qual vaga deseja se candidatar?
        1 = Vaga 1
        2 = Vaga 2
        0 = Sair
: \n'''))
        if vaga == 1:
            dadosCandidato('Vaga1')
        elif vaga == 2:
            dadosCandidato('Vaga2')
        elif vaga == 0:
            escolhendoAptos()
            break
        else:
            print('Erro!')

main()
