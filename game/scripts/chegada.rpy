label chegada:
    'Cheguei ao IC, acho que vai ser divertido, mas estou completamente perdido, não sei muito bem o que fazer'
    show akari feliz at left
    with None
    show akari feliz at center
    with move
    akari 'Finalmente você chegou! Os outros membros do Gamux querem muito te conhecer!'
    show akari feliz at left
    with move
    hide akari feliz
    with None
    show anaclara feliz at right
    with None
    show anaclara feliz at center
    with move
    ana 'Oi, tudo bem? É um prazer te conhecer, eu sou a Ana. Sou da Ciência da Computação.'
    show anaclara olhos_fechados
    ana 'Comecei a participar do Gamux no meio de 2017. Sempre gostei muito de arte, de desenhar...'
    show anaclara feliz
    ana 'Então eu faço alguns materiais de divulgação do Gamux. Sou a Coordenadora de Comunicação.'
    p 'É um prazer te conhecer, Ana! Que legal!'
    show anaclara feliz at left
    with move
    hide anaclara feliz
    with None
    show peronio at right
    with None
    show peronio at center
    with move
    peronio 'Olá, prazer. Eu sou o Perônio, sou o Coordenador de Projetos do Gamux.'
    peronio 'Atualmente temos um projeto chamado Godotware. É um jogo que é uma coleção de minijogos.'
    peronio 'Nós trabalhamos nele no nosso horário de desenvolvimento, que atualmente é às segundas-feiras das 17h30 às 20h.'
    p 'Que legal! Onde?'
    peronio 'No IC 3, que fica aqui do lado. Apareça lá!'
    show peronio at left
    with move
    hide peronio
    with None
    show stefano at left
    with None
    show stefano at center
    with move
    stefano 'Olá, meu nome é Stéfano. Sou o Coordenador Financeiro do Gamux, eu decido quanto vamos gastar em toddyinho na jam.'
    stefano 'Também decido quanto as guloseimas vão custar para maximizar o lucro.'
    show stefano at right
    with move
    hide stefano
    with None
    show gabriel at right
    with None
    show gabriel at center
    with move
    gabriel 'Oi, eu sou o Gabriel! Entrei para o Gamux esse ano. Participo no desenvolvimento do Godotware.'
    gabriel 'Ah, e participei também do desenvolvimento dessa Visual Novel que você está jogando agora!'
    show gabriel at left
    with move
    hide gabriel
    with None
    show alec at left
    with None
    show alec at center
    with move
    alec 'Olá, tudo bem? Meu nome é Alec. Participo do desenvolvimento do Godotware também. Além disso, sou o hokage do Gamux. Quer ver minha capa do Naruto?'

menu:
    'Claro!':
        # hide alec
        # show alec hokage
        alec 'Jutsu Clones das Sombras!'
    'Hum.......... Não, valeu.':
        # hide alec
        # show alec decepcionado
        alec 'Nossa.'

show alec at right
with move
hide alec
with None
show finger at right
with None
show finger at center
with move
finger 'Prazer, meu nome é Henrique, mas todos me chamam de Finger. Na última jam eu quase morri, mas foi muito louco.'

menu:
    'Meu Deus! O que houve?':
        finger '(contar o que aconteceu)' #lembrar o Finger de contar o que houve
    '...':
        finger 'Haha, calma, estou exagerando. Não precisa se assustar.'

show finger at left
with move
hide finger
with None
show artuts at left
with None
show artuts at center
with move
artuts 'Oi, eu sou o Arthur, mas todos me chamam de Artuts ou de Tuts. É um prazer te conhecer!'
show artuts at right
with move
hide artuts
with None
show carlos at right
with None
show carlos at center
with move
carlos 'Eu sou o Carlos. Eu fiz o site do Gamux junto com o Alec. É um prazer te conhecer!'
show carlos at left
with move
hide carlos
with None
show gustavo at left
with None
show gustavo at center
with move
gustavo 'Olá, eu sou o Gustavo. Aproveite a Jam!'
show gustavo at right
with move
hide gustavo
with None

jump aventura
