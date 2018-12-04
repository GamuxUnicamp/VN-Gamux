define ana = Character('Ana', color='#FFFFFF')
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

label splashscreen:
    $ renpy.movie_cutscene('gamux_intro.ogg')
    return #nao funciona com mp4

label start:
    scene bg cb_circulo
    play music 'começo.mp3'
    #python: Esse bloco nao e obrigatorio, o sifrao resolve
    $ name = renpy.input('Digite seu nome:')
    $ name = name.strip() or 'Protagonista' #Recebendo nome do jogador
    '{i}É... Acabei de sair da aula aqui no CB, não está fácil.{/i}' #Primeira cena, jogador sai da aula e encontra com a Akari, que a/o convida para a Livre Jam
    '{i}Acabei de entregar um trabalho, já tenho mais cinco pra fazer, tenho prova semana que vem... Esse semestre está puxado.{/i}'
    '{i}Depois de um tempo viajando, percebo que alguém vem em minha direção.{/i}'
    '???' 'Oi, [p]! Como vai? Tem planos pro final de semana?'
    show akari feliz
    '{i}Ah, essa é minha amiga Akari, da Ciência da Computação.{/i}'
    show akari olhos_fechados
menu:
    'Dormir':
        show akari feliz
        p 'Oi, Akari. Vou indo, essa semana foi puxada pra mim, acho que vou passar o final de semana todo dormindo. E você?'
        jump conversa
    'Netflix':
        show akari feliz
        p 'Oi, Akari, vou bem. Pretendo maratonar minhas séries esse final de semana. E você, tem planos?'
        jump conversa
    'Estudar':
        show akari feliz
        p 'Oi, Akari. Estou pensando nesse semestre, está tenso, vou estudar o final de semana todo, e você?'
        $ estudar = True
        jump conversa
    'Rolê':
        show akari feliz
        $ role = True
        p 'Oi, Akari. Vou bem. Eu queria sair esse final de semana, tenho estado no tédio ultimamente. Tem alguma ideia?'
        jump conversa
    'Nada':
        show akari feliz
        p 'Oi, Akari, estou bem. Hum... Acho que vou só brisar no final de semana, haha, e você?'
        show akari olhos_fechados
        '{i}Mas que porcaria de resposta...{/i}'
        show akari feliz
        jump conversa #Conversa sobre o final de semana
label conversa:
    if role:
        show akari olhos_fechados
        akari 'Olha só quanto ânimo! Eu vou participar de um evento do Gamux, a entidade da qual faço parte. Chama Livre Jam, quer vir?'
        show akari feliz #Akari pisca
    elif estudar:
        show akari olhos_fechados
        akari 'Ah, entendo. Realmente não está fácil pra ninguém...'
        show akari feliz
        akari 'Eu vou pra Livre Jam, um evento organizado pelo Gamux junto com a LivreCamp. Se mudar de ideia e quiser vir também, vai ser lá no IC, só aparecer.'
        show akari olhos_fechados
    else:
        '{i}A Akari não se deixou convencer com meus planos, certeza...{/i}'
        show akari olhos_fechados
        akari 'Certo então. Eu vou pra Livre Jam no IC, evento da entidade da qual eu faço parte, o Gamux.'
        show akari feliz
        akari 'Por que, em vez de ficar embromando o final de semana inteiro, você não vem também?'
        show akari olhos_fechados
    '{i}Verdade! Eu lembro que ela me contou que fazia parte de uma entidade, só não lembro exatamente o que é...{/i}'
    show akari feliz
    p 'Parece interessante, mas do que se trata mesmo esse evento e sua entidade em si?'
    show akari olhos_fechados
    akari 'A Livre Jam e o Gamux?! Ah, foi mal, o que você achava que o Gamux era?'
    show akari feliz
    p 'Hum...'
    show akari olhos_fechados
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
    show akari feliz
    akari 'Não! Nada a ver!'
    show akari olhos_fechados
    akari 'Gamux é uma entidade de estudo e desenvolvimento de jogos que busca fomentar a cultura de games na universidade e na região.'
    show akari feliz
    '{i}Eu não sabia nada disso...{/i}'
    show akari olhos_fechados
    p 'Que incrível! Eu não imaginava que sua entidade fosse assim.'
    show akari feliz
    akari 'Tudo bem.'
    p 'E o evento, do que se trata?'
    show akari olhos_fechados
    akari 'Ah sim, a Livre Jam é uma Game Jam, uma maratona na qual temos um tempo determinado pra desenvolver e apresentar um jogo. No caso da Livre Jam, são 48 horas.'
    show akari feliz
    akari 'Além disso, a Livre Jam é especial porque usamos apenas ferramentas livres.'
    show akari olhos_fechados
    akari 'E aí, você vai?'
    show akari feliz
    p 'Parece muito incrível, mas eu não sei...'
menu:
    'Ir':
        p 'Quer saber? Eu vou. Parece realmente muito bom. Onde é e que horas começa?'
        jump lugar
    'Furar':
        p 'Ah... Sabe, eu acho que não vai rolar, desculpa [akari].'
        show akari feliz
        akari 'Você tem certeza? Vai ser bem legal...'
        show akari olhos_fechados
        jump escolha_final

menu escolha_final:
    'Ir':
        show akari feliz
        p 'Tudo bem, você me conquistou. Eu vou então. Onde eu preciso ir e que horas?'
        jump lugar
    'Não ir':
        show akari feliz
        if estudar:
            p 'Não dá, Akari, é sério. Desculpa, mas, se eu não for estudar, acho que vou bombar o semestre. Me desculpa. Não fica magoada, tá?'
            show akari olhos_fechados
            akari 'Tudo bem, eu entendo. Fazer o que... Às vezes temos que estudar, não?'
            show akari feliz
        elif role:
            show akari feliz
            p 'Agradeço o convite, mas esperava algum outro rolê. Sei lá, vou procurar alguma outra coisa pra fazer... Desculpa.'
            show akari olhos_fechados
            akari 'Poxa vida, tudo bem então.'
            show akari feliz
        else:
            show akari feliz
            p 'Foi mal, Akari, mas não vai rolar. Acho que não é pra mim, desculpa.'
            show akari olhos_fechados
            akari 'Tudo bem. Se quiser vir em alguma outra coisa do Gamux, estaremos sempre abertos pra você.'
            show akari feliz
        jump sadending
