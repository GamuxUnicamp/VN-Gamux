define ana = Character('Ana', color='#000000')
define gabriel = Character('Gabriel', color='#8B0000')
define akari = Character('Akari')
define peronio = Character('Perônio')
define stefano = Character('Stéfano')
define alec = Character('Alec', color='#90EE90')
define thiago = Character('Thiago')
define finger = Character('Finger')
define artuts = Character('Artuts')
define carlos = Character('Carlos')
define gustavo = Character('Gustavo')
define rapha = Character('Rapha')
define chris = Character('Chris')
define professor = Character('Professor maléfico')
define p = Character('[name]') #Personagens
default role = False #Variáveis
default estudar = False
default desistir = False
default equipe = False
default dormiu = False
default happyending = True


label start:
    python:
        name = renpy.input('Digite seu nome:')
        name = name.strip() or 'Protagonista' #Recebendo nome do jogador
    'É... Acabei de sair da aula aqui no CB, não está fácil.' #Primeira cena, jogador sai da aula e encontra com a Akari, que a/o convida para a Livre Jam
    'Acabei de entregar um trabalho, já tenho mais cinco pra fazer, tenho prova semana que vem... Esse semestre está puxado.'
    'Depois de um tempo viajando, percebo que alguém vem em minha direção.'
    '???' 'Oi, [p]! Como vai? Tem planos pro final de semana?'
    show akari feliz
    'Ah, essa é minha amiga Akari, da Ciência da Computação.'
menu:
    'Dormir':
        p 'Oi, Akari. Vou indo, essa semana foi puxada pra mim, acho que vou passar o final de semana todo dormindo. E você?'
        jump conversa
    'Netflix':
        p 'Oi, Akari, vou bem. Pretendo maratonar minhas séries esse final de semana. E você, tem planos?'
        jump conversa
    'Estudar':
        p 'Oi, Akari. Estou pensando nesse semestre, está tenso, vou estudar o final de semana todo, e você?'
        $ estudar = True
        jump conversa
    'Rolê':
        $ role = True
        p 'Oi, Akari. Vou bem. Eu queria sair esse final de semana, tenho estado no tédio ultimamente. Tem alguma ideia?'
        jump conversa
    'Nada':
        p 'Oi, Akari, estou bem. Hum... Acho que vou só brisar no final de semana, haha, e você?'
        'Mas que porcaria de resposta...'
        jump conversa
label conversa:
    if role:
        akari 'Olha só quanto ânimo! Eu vou participar de um evento do Gamux, a entidade da qual faço parte. Chama Livre Jam, quer vir?'
    elif estudar:
        akari 'Ah, entendo. Realmente não está fácil pra ninguém...'
        akari 'Eu vou pra Livre Jam, um evento organizado pelo Gamux junto com a LivreCamp. Se mudar de ideia e quiser vir também, vai ser lá no IC, só aparecer.'
    else:
        'A Akari não se deixou convencer com meus planos, certeza...'
        akari 'Certo então. Eu vou pra Livre Jam no IC, evento da entidade da qual eu faço parte, o Gamux.'
        akari 'Por que, em vez de ficar embromando o final de semana inteiro, você não vem também?'
    'Verdade! Eu lembro que ela me contou que fazia parte de uma entidade, só não lembro exatamente o que é...'
    p 'Parece interessante, mas do que se trata mesmo esse evento e sua entidade em si?'
    akari 'A Livre Jam e o Gamux?! Ah, foi mal, o que você achava que o Gamux era?'
    p 'Hum...'
menu:
    'Jogar LoL o dia todo':
        p 'Achava que Gamux era uma entidade na qual você ia pra ficar jogando LoL o dia todo.'
    'Fazer joguinhos':
        p 'Achava que no Gamux você só ia pra fazer joguinhos.'
    'Casa de swing':
        p 'Eu achava, sinceramente, que era uma Casa de Swing.'
    'Clubinho nerd':
        p 'Gamux não é tipo um clubinho onde os nerds vão se reunir?'

label explicacao:
    akari 'Não! Nada a ver!'
    akari 'Gamux é uma entidade de estudo e desenvolvimento de jogos que busca fomentar a cultura de games na universidade e na região.'
    'Eu não sabia nada disso...'
    p 'Que incrível! Eu não imaginava que sua entidade fosse assim.'
    akari 'Tudo bem.'
    p 'E o evento, do que se trata?'
    akari 'Ah sim, a Livre Jam é uma Game Jam, uma maratona na qual temos um tempo determinado pra desenvolver e apresentar um jogo. No caso da Livre Jam, são 48 horas.'
    akari 'Além disso, a Livre Jam é especial porque usamos apenas ferramentas livres.'
    akari 'E aí, você vai?'
    p 'Parece muito incrível, mas eu não sei...'
menu:
    'Ir':
        p 'Quer saber? Eu vou. Parece realmente muito bom. Onde é e que horas começa?'
        jump lugar
    'Furar':
        p 'Ah... Sabe, eu acho que não vai rolar, desculpa [akari]'
        akari 'Você tem certeza? Vai ser bem legal...'
        jump escolha_final

menu escolha_final:
    'Ir':
        p 'Tudo bem, você me conquistou. Eu vou então. Onde eu preciso ir e que horas?'
        jump lugar
    'Não ir':
        if estudar:
            p 'Não dá, Akari, é sério. Desculpa, mas, se eu não for estudar, acho que vou bombar o semestre. Me desculpa. Não fica magoada, tá?'
            akari 'Tudo bem, eu entendo. Fazer o que... Às vezes temos que estudar, não?'
        elif role:
            p 'Agradeço o convite, mas esperava algum outro rolê. Sei lá, vou procurar alguma outra coisa pra fazer... Desculpa.'
            akari 'Poxa vida, tudo bem então.'
        else:
            p 'Foi mal, Akari, mas não vai rolar. Acho que não é pra mim, desculpa.'
            akari 'Tudo bem. Se quiser vir em alguma outra coisa do Gamux, estaremos sempre abertos pra você.'
        jump sadending
label sadending:
    if not desistir:
        hide akari feliz
        'Eu recusei o convite da Akari e não fui à Livre Jam.'
    else:
        'Acabei desistindo e não fui à Jam.'
        show akari feliz
        akari 'Sem Toddynho pra você.'
        hide akari feliz
    'Este foi o final de semana mais entediante da minha vida, eu deveria ter ido à Jam!'
    'FIM DE JOGO'
