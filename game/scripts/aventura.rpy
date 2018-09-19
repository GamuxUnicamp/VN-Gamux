label aventura:
    scene bg sala ic3_5
    p 'Eu estou numa game jam, mas eu não sei nem como começar a fazer um jogo! O que eu faço?'
    show chris feliz
    chris 'Não se preocupe! Não precisa ter experiência desenvolvendo para participar do evento.'
    chris 'O objetivo é se divertir e, também, aprender.'
    chris 'Ah, e você pode fazer seu jogo sozinho ou em equipe.'
    chris 'É bem divertido desenvolver em equipe, por exemplo, juntar alguns amigos e vir para a jam.'
    chris 'Mas você também pode entrar em alguma equipe na hora e ver no que dá.'
    chris 'Você quer chamar alguns amigos? Ainda dá tempo, mande mensagens pra eles!'

menu:
    'Mandar mensagens pros amigos perguntando se querem vir à jam':
        p 'Espero que eles venham...'
        p 'Finalmente, eles chegaram! Vamos começar!'
        $ equipe = True
    'Quero fazer meu jogo sozinho':
        chris 'Tudo bem então! Se precisar de ajuda com as ferramentas, me chame!'
    'Quero entrar em uma equipe com pessoas que já estão no evento':
        chris 'Vamos procurar uma equipe para você então.'
        $ equipe = True

chris 'Então, o que pensa em fazer no desenvolvimento do jogo?'
p 'Não sei...'
p 'O que posso fazer?'
chris 'Bem, fazer um jogo não é apenas programar, você pode trabalhar com modelagem 3D, arte digital, produção musical, roteiro e programação, dentre outras coisas'
chris 'Quer fazer alguma dessas?'
menu:
    'Modelagem 3D':
        p 'Eu quero modelagem 3D'
        Chris 'Muito bom, então o Blender é uma boa ferramenta pra você experimentar'
    'Arte digital':
        p 'Quero arte digital'
        chris 'Bem interessante, você pode trabalhar com Krita ou GIMP, são boas ferramentas'
        chris 'Há material na wiki do Gamux sobre o Krita para consulta.'
    'produção musical':
        p 'Eu gostaria muito de ficar com a produção musical'
        chris 'Isso é muito legal, há várias coisas que você pode fazer, uma ferramenta legal é o audacity'
    'roteiro':
        p 'Eu quero a parte de roteiro'
        chris 'Boa, você pode trabalhar para fazer isso em qualquer jogo, mas jogos com mais enfoque em roteiro, como os feitos em Renpy e Twine são interessantes pra você'
    'Programação':
        p 'Eu acho que vou codar mesmo'
        chris 'Da hora, uma boa ferramenta, a que temos usado no Gamux, é o Godot engine'
        chris 'Vários membros do Gamux têm experiência com ela, então saberão te ajudar!'
        p 'Que legal!'
        chris 'Há tutoriais de Godot na nossa wiki. Dê uma olhada, pode ser um bom ponto de partida!'
chris 'Indepente do que for fazer, a Wiki do Gamux tem tutoriais sobre algumas ferramentas, se você precisar'
chris 'Boa sorte!'
chris 'Ah, não se esqueça! A ideia da Livre Game Jam é utilizar apenas ferramentas livres no desenvolvimento.'
p 'Ah sim, mas o que é software livre?'
show chris feliz at left
with move
show peronio at right
with None
peronio 'Olá, ouvi a conversa de vocês, eu posso te dizer o que é software livre'
hide chris
with None
show peronio at center
with move
peronio 'Segundo a Free Software Foundation e o site do GNU, softaware livre é todo aquele que possua as quatro liberdades fundamentais:'
peronio 'A liberdade de executar o programa como você desejar, para qualquer propósito;'
peronio 'A liberdade de estudar como o programa funciona, e adaptá-lo às suas necessidades. Para tanto, acesso ao código-fonte é um pré-requisito;'
peronio 'A liberdade de redistribuir cópias de modo que você possa ajudar outros;'
peronio 'E'
peronio 'A liberdade de distribuir cópias de suas versões modificadas a outros. Desta forma, você pode dar a toda comunidade a chance de beneficiar de suas mudanças. Para tanto, acesso ao código-fonte é um pré-requisito.'
peronio 'Ou seja, com o softaware livre, você não está preso à vontade das grandes desenvolvedoras de software, você pode saber o que está acontecendo com seu softaware e alterá-lo segundo suas necessidades e vontades, sem depender de outros.'
p 'Que interessante, eu gostei dessa ideia'
peronio 'Ah sim, é realmente muito incrível'
peronio 'Mais alguma dúvida'
p 'bem...'
menu:
    'FPS procedural':
        p 'Eu consigo criar um FPS como COD ou BF, mas gerado proceduralmente numa Jam?'
    'Skirim melhor':
        p 'Eu consigo criar um RPG como Skyrim, mas melhor, durante a Jam?'
peronio 'Vai nessa'
peronio 'Nada te impede de tentar, mas assim, fazer isso numa equipe de quatro a cinco pessoas, em 48 horas, é praticamente impossível.'
peronio 'Mas se quiser, vou achar incrível, vou querer muito jogar seu jogo depois.'
hide peronio
'Algum tempo depois...'
show rapha feliz



rapha 'Olá, como está indo seu jogo?!'
rapha 'Ah, acho que ainda não nos conhecemos! Eu sou a Rapha, estudo no IA.'
p 'É um prazer te conhecer!'
rapha 'Você já deu uma olhada na LariJam?'
p 'O que é a LariJam?'
rapha 'É uma venda de guloseimas especialmente para a jam.'
rapha 'Tem várias coisas, por exemplo toddyinho, cup noodles, chocolates... Dê uma olhada!'
show rapha feliz at left
with move
hide rapha feliz
with None

'Eu vou ao balcão da LariJam...'

show thiago feliz
thiago 'Olá, tudo bem? Você quer comprar alguma coisa?'
menu:
    'Toddyinho':
        thiago 'Aqui está! Aproveite o evento!'
    'Cup Noodles':
        thiago 'Aqui está! Mas tome cuidado, o cheiro pode incomodar algumas pessoas!'
    'Eu preciso mesmo é de café pra codar!':
        thiago 'Aqui está, boa sorte! Não se esqueça de parar um pouco para descansar, hein?'
    'Chocolate! *_*':
        thiago 'Aqui está!'
    'Eu queria comida, tipo, uma refeição... Ou pizza.':
        thiago 'A LariJam tem apenas guloseimas, mas você pode pedir pelo iFood ou pedir marmitas.'
        thiago 'É comum o pessoal se juntar para pedir marmitas, tente combinar com alguém.'

hide thiago

'Algum tempo depois...'

p 'Nossa... Estou caindo de sono.'

menu:
    'Dormir':
        $ dormiu = True
    'Não! Mais café, quero continuar fazendo meu jogo!':
        show rapha feliz
        rapha 'Ei! Descansar também é importante!'
        rapha 'O objetivo do evento é se divertir, não tem problema se você não acabar seu jogo.'
        rapha '48 horas é um tempo curto para fazer um jogo...'
        rapha 'A ideia é fazer algo mais simples e se divertir mesmo!'
        hide rapha

if dormiu == False:
    'Algum tempo depois...'

    p 'ZZZ...ZZZ...'
    p 'AH! Meu jogo!'
    p 'Mas eu estou com bastante sono... Talvez seja melhor dormir um pouco.'
    menu:
        'Dormir':
            $ dormiu = True
        'Não! Quero continuar!':
            'Você continua, mas sente suas pálpebras pesando...'

if dormiu == False:
    'Algum tempo depois...'

    p 'Não aguento mais... Preciso dormir!'
    menu:
        'Dormir':
            $ dormiu = True
        'Acho que aguento mais um pouco...':
            'Você continua... Que determinação!'
            jump sleepending

#if equipe:
    # treta

label sleepending:
    if dormiu == False:
        $ happyending = False
        'Um tempo depois...'
        'O que está acontecendo?'
        'Está tudo escurecendo...'
        'Você sucumbe ao sono, seu corpo cai sobre a mesa.'
        'Sua cabeça inevitavelmente bate no teclado...'
        'E pressiona a tecla Backspace, que começa a apagar o código e tudo que você tinha feito...'
        'E todo o seu jogo se perde. Todo o seu trabalho.'
        'FIM DE JOGO'

if happyending == True:
    'Que bom que descansei um pouco, isso certamente vai melhorar meu rendimento!'

    'O tempo passa... Você desenvolve um jogo e se diverte muito na jam.'

    'E, finalmente, o tempo acaba. Você tem um jogo simples, mas que fez com muito carinho.'

    show akari feliz
    akari 'Está na hora do encerramento e da apresentação dos jogos!'
    p 'Apresentação dos jogos?'
    akari 'Sim! Todos que quiserem podem apresentar o que fizeram! Você quer apresentar seu jogo?'

    menu:
        'Claro!':
            akari 'Então vamos pro auditório!'
        'Hm... Não sei.':
            akari 'Não se preocupe, é só uma apresentação rápida sobre a sua ideia e as ferramentas que você usou.'
            akari 'E ninguém está aqui para julgar.'
            akari 'É que é sempre incrível ver como o mesmo tema pode dar origem a vários jogos diferentes!'
        'Não.':
            akari 'Ok! Assista as apresentações então!'

    hide akari

    'Nós do Gamux te agradecemos por ter jogado nossa Visual Novel de divulgação da Livre Game Jam!'
    'Esperamos que tenha conhecido melhor a entidade e se divertido.'
    'Venha para a Livre Game Jam! Está chegando! *-*'
