define ana = Character('Ana',color='#000000')
define gabriel = Character('Gabriel',color='#8B0000')
define akari = Character('Akari')
define peronio = Character('Perônio')
define stehfano = Character('Stehfano')
define alec = Character('Alec',color='#90EE90')
define thiago = Character('Thiago')
define finger = Character('Finger')
define artur = Character('Artuts')
define carlos = Character('Carlos')
define gustavo = Character('Gustavo')
define rapha = Character('Rapha')
define professor = Character('Professor maléfico')
define p = Character('[name]') #Personagens
default role = False #Variáveis
default estudar = False
default desistir = False



label start:
    python:
        name = renpy.input('Digite seu nome:')
        name = name.strip() or 'Protagonista' #Recebendo nome do jogador
    'É, acabei de sair da aula aqui no CB, não está fácil' #Primeira cena, jogador sai da aula e encontra com a Akari, que a/o convida para a Livre Jam
    'Acabei de entregar um trabalho, já tenho mais cinco pra fazer, tenho prova semana que vem, esse semestre está puxado...'
    'Depois de um tempo viajando, percebo que alguém vem em minha direção'
    '???' 'Oi [p] como vai, tem planos pro final de semana?'
    show akari feliz
    'Ah, essa é minha amiga Akari, da ciência da computação.'
    'Eu não tinha pensado em nada, e agora?'
menu:
    'Dormir':
        p 'Oi Akari, vou indo, essa semana foi puxada pra mim, acho que vou passar o final de semana todo dormindo e você?'
        jump conversa
    'Netflix':
        p 'Oi Akari, vou bem, pretendo maratonar minhas séries esse final de semana, e você, tem planos?'
        jump conversa
    'Estudar':
        p 'Oi Akari, estou pensando nesse semestre, está tenso, vou estudar o final de semana todo e você?'
        $ estudar = True
        jump conversa
    'Rolê':
        $ role = True
        p 'Oi Akari, vou bem, eu queria sair esse final de semana, tenho estado no tédio ultimamente, tem algum projeto?'
        jump conversa
    'Nada':
        p 'Oi Akari, estou bem. Hum... Acho que vou só brisar no final de semana, haha, e você?'
        'Mas que porcaria de resposta...'
        jump conversa
label conversa:
    if role:
        akari 'Olha só, quanto ânimo, eu tenho um projeto sim, eu vou participar de um evento do Gamux lá no IC, a entidade que faço parte, chama Livre Jam, quer ir?'
    elif estudar:
        akari 'Ah, entendo, realmente, não está fácil pra ninguém.'
        akari 'Eu vou pra Livre Jam, um evento organizado pelo Gamux junto com a LivreCamp, se mudar de ideia e quiser ir também, vai ser lá no IC, só aparecer lá.'
    else:
        'A Akari não se deixou convencer com meus planos, certeza'
        akari 'Está certo então. Eu vou pra Livre Jam no IC, evento da entidade que eu faço parte, Gamux.'
        akari 'Por que, em vez de ficar embromando o final de semana inteiro, você não vai lá também?'
    'É verdade, eu lembro que ela me contou que fazia parte de uma entidade, só não lembro exatamente o que é'
    p 'Parece interessante, mas do que se trata mesmo esse evento, e sua entidade em si?'
    akari 'A Livre Jam e a Gamux?! Ah, foi mal, o que você achava que a Gamux era?'
    p 'Hum...'
menu:
    'Jogar Lol o dia todo':
        p 'Achava que Gamux era uma entidade que você ia pra ficar jogando Lol o dia todo'
    'Fazer joguinhos':
        p 'Achava que no Gamux você só ia pra fazer joguinhos'
    'Casa de swing':
        p 'Eu achava, sinceramente, que era uma casa de Swing'
    'Clubinho nerd':
        p 'Gamux não é tipo um clubinho onde os nerds vão se reunir?'

label explicacao:
    akari 'Não! Nada a ver'
    akari 'Gamux é uma entidade de estudo e desenvolvimento de jogos que busca fomentar a cultura dos Games na universidade e sua região'
    'Eu não sabia nada disso'
    p 'Que incrível, eu não imaginava que sua entidade fosse assim'
    akari 'Tudo bem'
    p 'E o evento, do que se trata?'
    akari 'Ah sim, a Livre Jam é uma Game Jam, uma maratona em que temos um tempo determinado pra desenvolver e apresentar um jogo, 48 horas na livre Jam.'
    akari 'Além disso, a Livre Jam é especial porque usamos apenas plataformas livres'
    akari 'E aí, você vai?'
    p 'Parece muito incrível, eu não sei...'
menu:
    'Ir':
        p 'Quer saber, eu vou, parece realmente muito bom, onde e que horas começa?'
        jump lugar
    'Furar':
        p 'Ah... Sabe, eu acho que não vai rolar, desculpa [akari]'
        akari 'Você tem certeza? Vai ser bem legal'
        jump escolha_final

menu escolha_final:
    'Ir':
        p 'Tudo bem, você me conquistou, eu vou então, onde eu preciso ir, a que horas?'
        jump lugar
    'Não ir':
        if estudar:
            p 'Não dá, Akari, é sério, desculpa, mas se eu não for estudar, acho que vou bombar o semestre, me desculpa, não fica magoada tá?'
            akari 'Tudo bem, eu entendo, fazer o que, as vezes temos que estudar não? hehe'
        elif role:
            p 'Agradeço o convite, mas esperava algum outro rolê, sei lá, vou procurar alguma outra coisa pra fazer, desculpa'
            akari 'Poxa vida, tudo bem então'
        else:
            p 'Foi mal Akari, mas não vai rolar, acho que não é pra mim, deculpa'
            akari 'Tudo bem, se quiser ir em alguma outra coisa, estaremos sempre abertos pra você'
        jump sadending
label sadending:
    if not desistir:
        hide akari feliz
        'Eu recusei o convite da Akari e não fui à Livre Jam'
    else:
        'Acabei desistindo e não fui à Jam'
        show akari feliz
        akari 'Sem Toddynho pra você'
        hide akari feliz
    'Este foi o final de semana mais entediante da minha vida, eu deveria ter ido à Jam'
    'FIM DE JOGO'
