label aventura:
    scene bg sala ic3_5 with dissolve
    p 'Eu estou numa game jam, mas eu não sei nem como começar a fazer um jogo! O que eu faço?'
    show chris feliz at left
    with None
    show chris feliz at center
    with move
    chris 'Não se preocupe! Não precisa ter experiência desenvolvendo para participar do evento.'
    show chris olhos_fechados
    chris 'O objetivo é se divertir e, também, aprender.'
    show chris feliz
    chris 'Ah, e você pode fazer seu jogo sozinho ou em equipe.'
    show chris olhos_fechados
    chris 'É bem divertido desenvolver em equipe, por exemplo, juntar alguns amigos e vir para a jam.'
    show chris feliz
    chris 'Mas você também pode entrar em alguma equipe na hora e ver no que dá.'
    show chris olhos_fechados
    chris 'Você quer chamar alguns amigos? Ainda dá tempo, mande mensagens pra eles!'
    show chris feliz
menu:
    'Mandar mensagens pros amigos perguntando se querem vir à jam':
        show chris olhos_fechados
        '{i}Espero que eles venham...{/i}'
        show chris feliz
        '{i}Finalmente, eles chegaram! Vamos começar!{/i}'
        show chris olhos_fechados
        $ equipe = True
    'Quero fazer meu jogo sozinho':
        show chris olhos_fechados
        chris 'Tudo bem então! Se precisar de ajuda com as ferramentas, me chame!'
    'Quero entrar em uma equipe com pessoas que já estão no evento':
        show chris olhos_fechados
        chris 'Vamos procurar uma equipe para você então.'
        $ equipe = True

label tarefa:
    show chris feliz
    chris 'Então, o que pensa em fazer no desenvolvimento do jogo?'
    show chris olhos_fechados
    p 'Não sei...'
    show chris feliz
    p 'O que posso fazer?'
    show chris olhos_fechados
    chris 'Bem, fazer um jogo não é apenas programar, você pode trabalhar com modelagem 3D, arte digital, produção musical, roteiro, programação, entre outras coisas.'
    show chris feliz
    chris 'Quer fazer alguma dessas?'
menu:
    'Modelagem 3D':
        show chris olhos_fechados
        p 'Eu quero modelagem 3D.'
        show chris feliz
        chris 'Muito bom, então o Blender é uma boa ferramenta pra você experimentar!'
        show chris olhos_fechados
    'Arte digital':
        show chris olhos_fechados
        p 'Quero arte digital.'
        show chris feliz
        chris 'Bem interessante, você pode trabalhar com Krita ou GIMP, são boas ferramentas.'
        show chris olhos_fechados
        chris 'Há material na wiki do Gamux sobre o Krita para consulta.'
    'Produção musical':
        show chris olhos_fechados
        p 'Eu gostaria muito de ficar com a produção musical.'
        show chris feliz
        chris 'Isso é muito legal, há várias coisas que você pode fazer. Uma ferramenta legal é o Audacity.'
        show chris olhos_fechados
    'Roteiro':
        show chris olhos_fechados
        p 'Eu quero a parte de roteiro.'
        show chris feliz
        chris 'Boa! Você pode trabalhar com roteiro em qualquer jogo, afinal, a história é muito importante.'
        show chris olhos_fechados
        chris 'Mas, como são apenas 48 horas nessa jam, pode ser interessante tentar uma ferramenta que simplifica a programação e permite focar na história, se é o que você quer.'
        show chris feliz
        chris "Ren'Py e Twine são boas opções para isso."
        show chris olhos_fechados
    'Programação':
        show chris olhos_fechados
        p 'Eu acho que vou codar mesmo.'
        show chris feliz
        chris 'Da hora. Uma boa ferramenta, a que temos usado no Gamux, é o Godot Engine.'
        show chris olhos_fechados
        chris 'Vários membros do Gamux têm experiência com ela, então saberão te ajudar!'
        show chris feliz
        p 'Que legal!'
        show chris olhos_fechados
        chris 'Há tutoriais de Godot na nossa wiki. Dê uma olhada, pode ser um bom ponto de partida!'

label software_livre:
    show chris feliz
    chris 'Indepente do que for fazer, a Wiki do Gamux tem tutoriais sobre algumas ferramentas, se você precisar.'
    show chris olhos_fechados
    chris 'Boa sorte!'
    show chris feliz
    chris 'Ah, não se esqueça! A ideia da Livre Game Jam é utilizar apenas ferramentas livres no desenvolvimento.'
    show chris olhos_fechados
    p 'Ah sim, mas o que é software livre?'
    show chris feliz at left
    with move
    show peronio at right
    with None
    peronio 'Olá, ouvi a conversa de vocês. Eu posso te dizer o que é software livre.'
    hide chris
    with None
    show peronio at center
    with move
    peronio 'Segundo a Free Software Foundation e o site do GNU, softaware livre é todo aquele que possua as quatro liberdades fundamentais:'
    show peronio olhos_fechados
    peronio '\"A liberdade de executar o programa como você desejar, para qualquer propósito;'
    show peronio
    peronio 'A liberdade de estudar como o programa funciona, e adaptá-lo às suas necessidades. Para tanto, acesso ao código-fonte é um pré-requisito;'
    show peronio olhos_fechados
    peronio 'A liberdade de redistribuir cópias de modo que você possa ajudar outros;'
    show peronio
    peronio 'E'
    show peronio olhos_fechados
    peronio 'A liberdade de distribuir cópias de suas versões modificadas a outros. Desta forma, você pode dar a toda comunidade a chance de beneficiar de suas mudanças. Para tanto, acesso ao código-fonte é um pré-requisito.\"'
    show peronio
    peronio 'Ou seja, com o softaware livre, você não está preso à vontade das grandes desenvolvedoras de software, você pode saber o que está acontecendo com seu softaware e alterá-lo segundo suas necessidades e vontades, sem depender de outros.'
    show peronio olhos_fechados
    p 'Que interessante, eu gostei dessa ideia.'
    show peronio
    peronio 'Ah, sim, é realmente muito incrível.'
    show peronio olhos_fechados
    peronio 'Mais alguma dúvida?'
    show peronio
    p 'Bem...'
menu:
    'FPS procedural':
        p 'Eu consigo criar um FPS como Call Of Duty ou Battle Field, mas gerado proceduralmente, numa game jam?'
    'Skirim só que melhor':
        p 'Eu consigo criar um RPG como Skyrim, mas melhor, durante a jam?'
label larijam:
    show peronio olhos_fechados
    peronio 'Vai nessa!'
    show peronio
    peronio 'Nada te impede de tentar, mas assim, fazer isso numa equipe de quatro a cinco pessoas, em 48 horas, é praticamente impossível.'
    show peronio olhos_fechados
    peronio 'Mas se quiser, vou achar incrível, vou querer muito jogar seu jogo depois.'
    hide peronio
    '{i}Algum tempo depois...{/i}'

    show rapha feliz
    rapha 'Olá, como está indo seu jogo?!'
    show rapha olhos_fechados
    rapha 'Ah, acho que ainda não nos conhecemos! Eu sou a Rapha, estudo no IA.'
    show rapha feliz
    p 'É um prazer te conhecer!'
    show rapha olhos_fechados
    rapha 'Você já deu uma olhada na LariJam?'
    show rapha feliz
    p 'O que é a LariJam?'
    show rapha olhos_fechados
    rapha 'É uma venda de guloseimas especialmente para a jam.'
    show rapha feliz
    rapha 'Tem várias coisas, por exemplo Toddynho, Cup Noodles, chocolates... Dê uma olhada!'
    show rapha feliz at left
    with move
    hide rapha feliz
    with None

    '{i}Eu vou ao balcão da LariJam...{/i}'

    show thiago feliz at left
    with None
    show thiago feliz at center
    with move
    show thiago feliz
    thiago 'Olá, tudo bem? Você quer comprar alguma coisa?'
    show thiago olhos_fechados
menu:
    'Toddynho':
        show thiago feliz
        thiago 'Aqui está! Aproveite o evento!'
        show thiago olhos_fechados
    'Cup Noodles':
        show thiago feliz
        thiago 'Aqui está! Mas tome cuidado, o cheiro pode incomodar algumas pessoas!'
        show thiago olhos_fechados
    'Eu preciso mesmo é de café pra codar!':
        show thiago feliz
        thiago 'Aqui está, boa sorte! Não se esqueça de parar um pouco para descansar, hein?'
        show thiago olhos_fechados
    'Chocolate! *_*':
        show thiago feliz
        thiago 'Aqui está!'
        show thiago olhos_fechados
    'Eu queria comida, tipo, uma refeição... Ou pizza.':
        show thiago feliz
        thiago 'A LariJam tem apenas guloseimas, mas você pode pedir pelo iFood ou pedir marmitas.'
        show thiago olhos_fechados
        thiago 'É comum o pessoal se juntar para pedir marmitas, tente combinar com alguém.'
        show thiago feliz

show thiago at left
with move
hide thiago

'{i}Algum tempo depois...{/i}'

p 'Nossa... Estou caindo de sono.'

menu:
    'Dormir':
        $ dormiu = True
        jump happyending
    'Não! Mais café, quero continuar fazendo meu jogo!':
        show rapha feliz at left
        with None
        show rapha feliz at center
        with move
        rapha 'Ei! Descansar também é importante!'
        show rapha olhos_fechados
        rapha 'O objetivo do evento é se divertir, não tem problema se você não acabar seu jogo.'
        show rapha feliz
        rapha '48 horas é um tempo curto para fazer um jogo...'
        show rapha olhos_fechados
        rapha 'A ideia é fazer algo mais simples e se divertir mesmo!'
        show rapha at left
        with move
        hide rapha

if dormiu == False:
    '{i}Algum tempo depois...{/i}'

    p 'ZZZ...ZZZ...'
    p 'AH! Meu jogo!'
    p 'Mas eu estou com bastante sono... Talvez seja melhor dormir um pouco.'
    menu:
        'Dormir':
            $ dormiu = True
            jump happyending
        'Não! Quero continuar!':
            '{i}Você continua, mas sente suas pálpebras pesando...{/i}'

if dormiu == False:
    '{i}Algum tempo depois...{/i}'

    p 'Não aguento mais... Preciso dormir!'
    menu:
        'Dormir':
            $ dormiu = True
            jump happyending
        'Acho que aguento mais um pouco...':
            '{i}Você continua... Que determinação{/i}!'
            jump sleepending
