def sugestao(jornada_esperada:list, pontos_realizados:list):
    from copy import deepcopy
    import datetime
    
    jornada_esperada_dir = {'Entradas':{}, 'Intervalos':{}, 'Saidas':{}}
    pontos_batidos_dir = {'Entradas' : {}, 'Intervalos':{}, 'Saidas':{}}
    output_popup = []
    jornada_atualizada = []
    quantidade_esperada = {
        'Entradas' : 0,
        'Intervalos' : 0,
        'Saidas' : 0,
    }

    quantidade_realizada = {
        'Entradas' : 0,
        'Intervalos' : 0,
        'Saidas' : 0,
    }

    definicao = {
        1 : 'Entrada',
        2 : 'Intervalo',
        3 : 'Saída',
    }




    for i in enumerate(jornada_esperada):
        
        i[1][1] = datetime.timedelta(hours = int(i[1][1].split(':')[0]), minutes = int(i[1][1].split(':')[1]), seconds = int(i[1][1].split(':')[2])) #formatando a hora de forma a conseguir operar com ela

        if definicao[i[1][0]] == 'Entrada':
            quantidade_esperada['Entradas'] += 1 #contando a quantidade de Entradas
            jornada_esperada_dir['Entradas'][quantidade_esperada['Entradas']] = [i[0], i[1][1]] #ordenando as entradas/intervalos/saidas numa estrutura de dado mais útil p esse caso

        elif definicao[i[1][0]] == 'Intervalo':
            quantidade_esperada['Intervalos'] += 1
            jornada_esperada_dir['Intervalos'][quantidade_esperada['Intervalos']] = [i[0], i[1][1]]
        elif definicao[i[1][0]] == 'Saída':
            quantidade_esperada['Saidas'] += 1
            jornada_esperada_dir['Saidas'][quantidade_esperada['Saidas']] = [i[0], i[1][1]]



   
    for i in enumerate(pontos_realizados):


        i[1][1] = datetime.timedelta(hours = int(i[1][1].split(':')[0]), minutes = int(i[1][1].split(':')[1]), seconds = int(i[1][1].split(':')[2]))

        if definicao[i[1][0]] == 'Entrada':

            quantidade_realizada['Entradas'] += 1

            pontos_batidos_dir['Entradas'][quantidade_realizada['Entradas']] = [i[0], i[1][1]] #ordenando as entradas/intervalos/saidas numa estrutura de dado mais útil p esse caso

        elif definicao[i[1][0]] == 'Intervalo':
            quantidade_realizada['Intervalos'] += 1
            pontos_batidos_dir['Intervalos'][quantidade_realizada['Intervalos']] = [i[0], i[1][1]]
        elif definicao[i[1][0]] == 'Saída':
            quantidade_realizada['Saidas'] += 1
            pontos_batidos_dir['Saidas'][quantidade_realizada['Saidas']] = [i[0], i[1][1]]
    
    jornada_atualizada = deepcopy(pontos_realizados)


    if quantidade_realizada['Entradas'] == 0 or definicao[pontos_realizados[0][0]] != 'Entrada' :

        
        if pontos_realizados[0][1] - jornada_esperada[0][1] <= datetime.timedelta(minutes = 45) or len(pontos_realizados) == len(jornada_esperada):

            output_popup += [definicao[pontos_realizados[0][0]] + ' às ' + str(pontos_realizados[0][1]) + ' alterar para ' + 'entrada às ' + str(pontos_realizados[0][1])]
            
            
            jornada_atualizada[0][0] = 1

        else:
            output_popup += ['Nem uma entrada foi adicionada! Adicionar entrada']
            jornada_atualizada[0] = jornada_esperada[0]

    
    if quantidade_realizada['Saidas'] == 0 or definicao[pontos_realizados[-1][0]] != 'Saída':

        if pontos_realizados[-1][1] - jornada_esperada[-1][1] <= datetime.timedelta(minutes = 45):
         
            output_popup += [definicao[pontos_realizados[-1][0]] + ' às ' + str(pontos_realizados[-1][1]) + ' alterar para ' + 'saída às ' + str(jornada_esperada[-1][1])]
            jornada_atualizada [-1][0] = 3
        else:

            output_popup += ['Nem uma saída foi adicionada! Adicionar saída']
            
            jornada_atualizada[-1] = jornada_esperada[-1]



    
    pseudo_intervalos_realizados = [[False, False, []] for i in range(0, quantidade_esperada['Intervalos'])] #define o [tipo, horário, ponto_todo]
    
    intervalo_counter = 0

    for ponto in pontos_realizados:

        if definicao[ponto[0]] == 'Intervalo':
                
            for i in range(0, len(jornada_esperada)):

                param = jornada_esperada[i][1] - ponto[1]
                
                if param <= datetime.timedelta(seconds = -1):
                    param = ponto[1] - jornada_esperada[i][1]
    
                if param <= datetime.timedelta(minutes=40) and definicao[jornada_esperada[i][0]] == 'Intervalo':
                    pseudo_intervalos_realizados[intervalo_counter] = [True, True, ponto]


        else: 
            for i in range(0, len(jornada_esperada)): 
                if ponto[1] - jornada_esperada[i][1] <= datetime.timedelta(minutes = 40) and definicao[jornada_esperada[i][0]] == 'Intervalo':
                    pseudo_intervalos_realizados[intervalo_counter] = [False, True, ponto]
                    
        intervalo_counter += 1

    for intervalo in range(0, len(pseudo_intervalos_realizados)):
    

        if pseudo_intervalos_realizados[intervalo][0] == False and pseudo_intervalos_realizados[intervalo][1] == False:
            output_popup += ['Adicionar intervalo às ' + str(jornada_esperada_dir['Intervalos'][intervalo+1][1])+ '?']
            
            jornada_atualizada.insert(jornada_esperada_dir['Intervalos'][intervalo+1][0], [2, jornada_esperada_dir['Intervalos'][intervalo+1][1]])
        elif pseudo_intervalos_realizados[intervalo][0] == False and pseudo_intervalos_realizados[intervalo][1] == True:
            
            output_popup += ['Substituir ' + definicao[pseudo_intervalos_realizados[intervalo][2][0]] + ' às ' + str(pseudo_intervalos_realizados[intervalo][2][1]) + ' por um intervalo?']


    for i in jornada_atualizada:

        i[1] = str(i[1])
            

    output = {'Mensagem' : output_popup, 'Jornada ajustada' : jornada_atualizada}
    return output


sugestao.__doc__ = """

A função recebe jornada_esperada:list e pontos_realizados:list na forma:

[[tipo do ponto:int, horario:str(HH:MM:SS)], ...]

e retorna o dicionario:

{'Mensagem' : output:list('TEXTO SUGESTÃO'), 'Jornada ajustada' : jornada_atualizada:list}

onde a jornada_atualizada vem na mesma forma da jornada_esperada/pontos_realizados, com a 
exceção de estar com os pontos substituidos de acordo com as sugestões.

"""



#análisar horaŕios batidos
#comparar a distancia deles com os horários esperados 
#e sugerir baseado nisso
