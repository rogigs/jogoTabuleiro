# -*- coding: UTF-8 -*-
import random
print("-" * 70)
print("\n THE GAME \n" )
print("-" * 70 )
print("")
print("O THE GAME constitui-se em um jogo multiplayer de tabuleiro \n" +
      "com perguntas do Ensino Médio. Para jogar basta escolher o \n" +
      "nome de dois jogadores para iniciar o jogo. \n")
print("O THE GAME indicará de quem é a vez de jogar e se o jogador \n " +
      "acertar a resposta um dado é lançado, e ele andará o\n" +
      "número do resultado do dado. Cada pergunta contém 5 alternativas \n")
print("Se o jogador da da vez errar ele passára a vez para o outro jogador \n")
print("Pórem, a casas de AVANÇO, RETROCESSO e NEUTRAS. Regras das casas: \n")
print(". AVANÇO: Há casas de avanço de 3 e 5 casas, caso você caia \n"+
      "nela terá de responder uma nova pergunta e caso acerte avançará \n" +
      "o tanto de casas indicado \n")
print(". RETROCESSO: Há casas de retrocesso de 3 e 5 casas, caso você caia \n"+
      "nela terá de responder uma nova pergunta e caso erre retrocederá \n" +
      "o tanto de casas indicado \n")
print(". NEUTRA: Você passa a sua vez de jogar \n")
print("O THE GAME possui um total de 50 casas")
print("-" * 70)
print("")


    
nick1 = input("Digite o nome do primeiro jogador: ")
nick2 = input("Digite o nome do segundo jogador: ")
print("")


#perguntas
perg1 = "Em que período da pré-história o fogo foi descoberto?\n a) Neolítico \n b) Paleolítico \n c) Idade dos Metais \n d) Período da Pedra Polida \n e) Idade Média"
perg2 = "Qual das alternativas abaixo apenas contêm classes de palavras? \n a) Vogais, semivogais e consoantes \n b) Artigo, verbo transitivo e verbo intransitivo \n c) Fonologia, Morfologia e Sintaxe \n d) Hiatos, ditongos e tritongos \n e) Substantivo, verbo e preposição"
perg3 = "Qual a montanha mais alta do Brasil? \n a) Pico da Neblina \n b) Pico Paraná \n c) Monte Roraima \n d) Pico Maior de Friburgo \n e) Pico da Bandeira"
perg4 = "Qual a velocidade da luz?  \n a) 300 000 000 metros por segundo (m/s) \n b) 150 000 000 metros por segundo (m/s) \n c) 199 792 458 metros por segundo (m/s) \n d) 299 792 458 metros por segundo (m/s) \n e) 30 000 000 metros por segundo (m/s)"
perg5 = "Em qual local da Ásia o português é língua oficial? \n a) Índia \n b) Filipinas \n c) Moçambique \n d) Macau \n e) Portugal"
perg6 = "It is six twenty ou twenty past six. Que horas são em inglês? \n a) 12:06 \n b) 6:20 \n c) 2:20 \n d) 6:02 \n e) 12:20"
perg7 = "Como é a conjugação do verbo caber na 1.ª pessoa do singular do presente do indicativo? \n a) Eu caibo \n b) Ele cabe \n c) Que eu caiba \n d) Eu cabo \n e) Nenhuma das alternativas"
perg8 = "Quais destas doenças são sexualmente transmissíveis? \n a) Aids, tricomoníase e ebola \n b) Chikungunya, aids e herpes genital \n c) Gonorreia, clamídia e sífilis \n d) Botulismo, cistite e gonorreia \n e) Hepatite B, febre tifoide e hanseníase"
perg9 = "Qual destes países é transcontinental? \n a) Rússia \n b) Filipinas \n c) Istambul \n d) Groenlândia \n e) Tanzânia"
perg10 = "Em qual das orações abaixo a palavra foi empregada incorretamente? \n a) Mais uma vez, portou-se mal. \n b) É um homem mal. \n c) Esse é o mal de todos. \n d) Mal falou nele, o fulano apareceu. \n e) É um mau vendedor."
perg11 = "Qual foi o recurso utilizado inicialmente pelo homem para explicar a origem das coisas? \n a) A Filosofia \n b) A Biologia \n c) A Matemática \n d) A Astronomia \n e) A Mitologia"
perg12 = "Qual das alternativas menciona apenas símbolos nacionais? \n a) Bandeira insígnia da presidência, bandeira nacional, brasão, hinos e selo \n b) Bandeira nacional, armas nacionais, hino nacional e selo nacional \n c) Bandeira nacional, brasão, hino nacional e hino da independência \n d) Bandeira nacional, cores nacionais, hino nacional e hino da independência \n e) Bandeira insígnia da presidência, brasão flora e fauna e hinos"
perg13 = "Qual era o nome de Aleijadinho? \n a) Alexandrino Francisco Lisboa \n b) Manuel Francisco Lisboa \n c) Alex Francisco Lisboa \n d) Francisco Antônio Lisboa \n e) Antônio Francisco Lisboa"
perg14 = "Qual o maior animal terrestre? \n a) Baleia Azul \n b) Dinossauro \n c) Elefante africano \n d) Tubarão Branco \n e) Girafa"
perg15 = "O que são Acordo de Paris e Tríplice Aliança respectivamente? \n a) Acordo ortográfico entre países cuja língua oficial é o francês e Acordo de cooperação financeira internacional entre as três maiores potências mundiais \n b) Acordo entre países europeus acerca da imigração e Acordo econômico entre Inglaterra, Rússia a França \n c) Acordo entre vários países acerca das consequências do aquecimento global e Acordo de cooperação financeira internacional entre as três maiores potências mundiais \n d) Acordo de cooperação financeira internacional entre as três maiores potências mundiais e Acordo entre vários países acerca das consequências do aquecimento global \n e) Acordo entre vários países acerca das consequências do aquecimento global e Acordo entre Alemanha, império Austro-Húngaro e Itália acerca de apoio em caso de guerra"
perg16 = "Qual a religião monoteísta que conta com o maior número de adeptos no mundo? \n a) Judaísmo \n b) Zoroastrismo \n c) Islamismo \n d) Cristianismo \n e) Hinduísmo"
perg17 = "Quem foi o primeiro homem a pisar na Lua? Em que ano aconteceu? \n a) Yuri Gagarin, em 1961 \n b) Buzz Aldrin, em 1969 \n c) Charles Conrad, em 1969 \n d) Charles Duke, em 1971 \n e) Neils Armstrong, em 1969."
perg18 = "Qual o nome do cientista que descobriu o processo de pasteurização e a vacina contra a raiva? \n  a) Marie Curie \n b) Blaise Pascal  \n c) Louis Pasteurs \n d) Antoine Lavoisier \n e) Charles Darwin"
perg19 = "As pessoas de qual tipo sanguíneo são consideradas doadores universais? \n a) Tipo A \n b) Tipo B \n c) Tipo O \n d) Tipo AB \n e) Tipo ABO"
perg20 = "De onde é a invenção do chuveiro elétrico? \n a) França \n b) Inglaterra \n c) Brasil \n d) Austrália \n e) Itália"
perg21 = "Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue? \n a) Tem entre 2 a 4 litros. São retirados 450 mililitros \n b) Tem entre 4 a 6 litros. São retirados 450 mililitros \n c) Tem 10 litros. São retirados 2 litros \n d) Tem 7 litros. São retirados 1,5 litros \n e) Tem 0,5 litros. São retirados 0,5 litros"

global posicaoJogador
global vezJogador


def contagemRodadas(rodada, posicaoJogador1, posicaoJogador2):
    print("")
    print("-" * 25)
    print("THE GAME")  
    print("-" * 25)
    print("Rodada: ", rodada)
    print("Posição de", nick1, ": ", posicaoJogador1)
    print("Posição de", nick2, ": ", posicaoJogador2)
    print("")
    return 

def sorteio():
    perguntas = [perg1, perg2, perg3, perg4, perg5, perg6, perg7, perg8, perg9, perg10, perg11, perg12, perg13, perg14, perg15, perg16, perg17, perg18, perg19, perg20, perg21]
    respPerguntas = ["B", "E", "A", "D", "D", "B", "A", "C", "A", "B", "A", "B", "E", "C", "E", "D", "A", "C", "C", "C", "B" ]
    numeroSorteado = int(random.random() * 21)
    numeroSorteadoDado = random.randint(1, 6)
    perguntaSorteada = perguntas[numeroSorteado]
    respostaSorteada = respPerguntas[numeroSorteado]
    return perguntaSorteada, respostaSorteada, numeroSorteadoDado

def perguntas():
    perguntaSorteada, respostaSorteada, numeroSorteadoDado = sorteio()
    print(perguntaSorteada)
    resp = input("Digite a alternativa correta: ")

    while (resp.upper() != "A") and (resp.upper() != "B") and (resp.upper() != "C") and (resp.upper() != "D") and (resp.upper() != "E"):
        print("*-*  VALOR INVÁLIDO  *-*")
        resp = input("Digite a alternativa correta: ")

    if resp.upper() == respostaSorteada:
        print("** Acertou **")
        print("")
        soma = numeroSorteadoDado
        vezJogador = True
        resposta = "correta"
    else:
        print("** Errou **")
        print("")
        soma = 0
        vezJogador = False
        resposta = "errada"
    return soma, vezJogador, resposta, numeroSorteadoDado

           
posicoesTabuleiro = True
rodada = 0
posicaoJogador1 = 0
posicaoJogador2 = 0
somaPosicaoJogador1 = 0
somaPosicaoJogador2 = 0
while posicoesTabuleiro == True:
    vezJogador1 = True
    vezJogador2 = True

    #Joga o jogador1
    while vezJogador1 == True:
        print("-" * 25)
        print("Agora é a vez de", nick1)
        print(nick1, "está na posição", somaPosicaoJogador1)
        print("")
        posicaoJogador1, vezJogador1, resposta, numeroSorteadoDadoAnt = perguntas()
        if resposta == "correta":
            print("O dado foi lançado...")
            print("Resultado do dado: ", numeroSorteadoDadoAnt)
            print("")
        somaPosicaoJogador1 += posicaoJogador1
        
        # PERGUNTA FINAL
        if somaPosicaoJogador1 >= 50:
            print("--- PERGUNTA FINAL ---")
            posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
            if resposta == "correta":
                print("-" * 25)
                print("VOCÊ VENCEU")
                print("-" * 25)
                vezJogador1 = False
                vezJogador2 = False
                posicoesTabuleiro = False
            else:
                print("VOCÊ ERROU RETORNARÁ A CASA QUE ESTAVA")
                print("")
                somaPosicaoJogador1 -= numeroSorteadoDadoAnt
                
        # CASA DE AVANÇO
        elif somaPosicaoJogador1 == 5 or somaPosicaoJogador1 == 20 or somaPosicaoJogador1 == 35:
            print("--- CASA DE AVANÇO ---")
            if somaPosicaoJogador1 == 5:
                print("--- 5 CASAS ---")
                posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
                if resposta == "correta":
                    print("** Acertou **")
                    print("")
                    somaPosicaoJogador1 += 5
                else:
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            else:
                if somaPosicaoJogador1 == 20 or somaPosicaoJogador1 == 35:
                    print("--- 3 CASAS ---")
                    posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
                    if resposta == "correta":
                        print("** Acertou **")
                        print("")
                        somaPosicaoJogador1 += 3
                    else:
                        print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                        print("")
            vezJogador1 = False
            
        #CASA DE RETROCESSO
        elif somaPosicaoJogador1 == 15 or somaPosicaoJogador1 == 25 or somaPosicaoJogador1 == 45:
            print("--- CASA DE RETROCESSO ---")
            if somaPosicaoJogador1 == 15:
                print("--- 5 CASAS ---")
                posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
                contadorRetrocesso = 0
                while resposta == "correta":
                    vezJogador1 = False
                    if contadorRetrocesso > 0:
                        vezJogador1 = True
                        somaPosicaoJogador1 -= 5
                    resposta = "errada"
                    contadorRetrocesso += 1
                if resposta == "errada":
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            if somaPosicaoJogador1 == 25 or somaPosicaoJogador1 == 45:
                print("--- 3 CASAS ---")
                posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
                contadorRetrocesso = 0
                while resposta == "correta":
                    vezJogador1 = False
                    if contadorRetrocesso > 0:
                        vezJogador1 = True
                        somaPosicaoJogador1 -= 3
                    resposta = "errada"
                    contadorRetrocesso += 1
                if resposta == "errada":
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            vezJogador1 = False
            
        #Neutra
        elif somaPosicaoJogador1 == 7 or somaPosicaoJogador1 == 21 or somaPosicaoJogador1 == 32:
            contadorNeutra = 0
            respostaWhile = "correta"
            while (contadorNeutra == 0) and (respostaWhile == "correta"):
                print("--- CASA NEUTRA ---")
                vezJogador1 = False
                if contadorNeutra > 0:
                    vezJogador1 = True
                    posicaoJogador1, vezJogador1, resposta, numeroSorteadoDado = perguntas()
                    if resposta == "correta":
                        print("** Acertou **")
                        print("")
                        somaPosicaoJogador1 += numeroSorteadoDadoAnt
                    else:
                        print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                        print(" ")
                contadorNeutra += 1
            vezJogador1 = False   
        print("-" * 25)




    # JOGADOR2
    while vezJogador2 == True:
        print("-" * 25)
        print("Agora é a vez de", nick2)
        print(nick1, "está na posição", somaPosicaoJogador2)
        print("")
        posicaoJogador2, vezJogador2, resposta, numeroSorteadoDadoAnt = perguntas()
        if resposta == "correta":
            print("O dado foi lançado...")
            print("Resultado do dado: ", numeroSorteadoDadoAnt)
            print("")
        somaPosicaoJogador2 += posicaoJogador2
        
        # PERGUNTA FINAL
        if somaPosicaoJogador2 >= 50:
            print("--- PERGUNTA FINAL ---")
            posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
            if resposta == "correta":
                print("-" * 25)
                print("VOCÊ VENCEU")
                print("-" * 25)
                vezJogador2 = False
                posicoesTabuleiro = False
            else:
                print("VOCÊ ERROU RETORNARÁ A CASA QUE ESTAVA")
                print("")
                somaPosicaoJogador2 -= numeroSorteadoDadoAnt
                
        # CASA DE AVANÇO
        elif somaPosicaoJogador2 == 5 or somaPosicaoJogador2 == 20 or somaPosicaoJogador2 == 35:
            print("--- CASA DE AVANÇO ---")
            if somaPosicaoJogador2 == 5:
                print("--- 5 CASAS ---")
                posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
                if resposta == "correta":
                    print("** Acertou **")
                    print("")
                    somaPosicaoJogador2 += 5
                else:
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            else:
                if somaPosicaoJogador2 == 20 or somaPosicaoJogador2 == 35:
                    print("--- 3 CASAS ---")
                    posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
                    if resposta == "correta":
                        print("** Acertou **")
                        print("")
                        somaPosicaoJogador2 += 3
                    else:
                        print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                        print("")
            vezJogador2 = False
            
        #CASA DE RETROCESSO
        elif somaPosicaoJogador2 == 15 or somaPosicaoJogador2 == 25 or somaPosicaoJogador2 == 45:
            print("--- CASA DE RETROCESSO ---")
            if somaPosicaoJogador2 == 15:
                print("--- 5 CASAS ---")
                posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
                contadorRetrocesso = 0
                while resposta == "correta":
                    vezJogador2 = False
                    if contadorRetrocesso > 0:
                        vezJogador2 = True
                        somaPosicaoJogador2 -= 5
                    resposta = "errada"
                    contadorRetrocesso += 1
                if resposta == "errada":
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            if somaPosicaoJogador2 == 25 or somaPosicaoJogador2 == 45:
                print("--- 3 CASAS ---")
                posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
                contadorRetrocesso = 0
                while resposta == "correta":
                    vezJogador2 = False
                    if contadorRetrocesso > 0:
                        vezJogador2 = True
                        somaPosicaoJogador2 -= 3
                    resposta = "errada"
                    contadorRetrocesso += 1
                if resposta == "errada":
                    print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                    print("")
            vezJogador2 = False
            
        #Neutra
        elif somaPosicaoJogador2 == 7 or somaPosicaoJogador2 == 21 or somaPosicaoJogador2 == 32:
            contadorNeutra = 0
            respostaWhile = "correta"
            while (contadorNeutra == 0) and (respostaWhile == "correta"):
                print("--- CASA NEUTRA ---")
                vezJogador2 = False
                if contadorNeutra > 0:
                    vezJogador2 = True
                    posicaoJogador2, vezJogador2, resposta, numeroSorteadoDado = perguntas()
                    if resposta == "correta":
                        print("** Acertou **")
                        print("")
                        somaPosicaoJogador2 += numeroSorteadoDadoAnt
                    else:
                        print("VOCÊ ERROU MAS CONTINUARÁ NA CASA QUE ESTÁ")
                        print("")
                contadorNeutra += 1
            vezJogador2 = False   
        print("-" * 25)
      
    rodada += 1
    contagemRodadas(rodada, somaPosicaoJogador1, somaPosicaoJogador2)



