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

label tarefa:
    chris 'Então, o que pensa em fazer no desenvolvimento do jogo?'
    p 'Não sei...'
    p 'O que posso fazer?'
    chris 'Bem, fazer um jogo não é apenas programar, você pode trabalhar com modelagem 3D, arte digital, produção musical, roteiro, programação, entre outras coisas.'
    chris 'Quer fazer alguma dessas?'
menu:
    'Modelagem 3D':
        p 'Eu quero modelagem 3D.'
        chris 'Muito bom, então o Blender é uma boa ferramenta pra você experimentar!'
    'Arte digital':
        p 'Quero arte digital.'
        chris 'Bem interessante, você pode trabalhar com Krita ou GIMP, são boas ferramentas.'
        chris 'Há material na wiki do Gamux sobre o Krita para consulta.'
    'Produção musical':
        p 'Eu gostaria muito de ficar com a produção musical.'
        chris 'Isso é muito legal, há várias coisas que você pode fazer. Uma ferramenta legal é o Audacity.'
    'Roteiro':
        p 'Eu quero a parte de roteiro.'
        chris 'Boa! Você pode trabalhar com roteiro em qualquer jogo, afinal, a história é muito importante.'
        chris 'Mas, como são apenas 48 horas nessa jam, pode ser interessante tentar uma ferramenta que simplifica a programação e permite focar na história, se é o que você quer.'
        chris "Ren'Py e Twine são boas opções para isso."
    'Programação':
        p 'Eu acho que vou codar mesmo.'
        chris 'Da hora. Uma boa ferramenta, a que temos usado no Gamux, é o Godot Engine.'
        chris 'Vários membros do Gamux têm experiência com ela, então saberão te ajudar!'
        p 'Que legal!'
        chris 'Há tutoriais de Godot na nossa wiki. Dê uma olhada, pode ser um bom ponto de partida!'
label software_livre:
    chris 'Indepente do que for fazer, a Wiki do Gamux tem tutoriais sobre algumas ferramentas, se você precisar.'
    chris 'Boa sorte!'
    chris 'Ah, não se esqueça! A ideia da Livre Game Jam é utilizar apenas ferramentas livres no desenvolvimento.'
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
    peronio '\"A liberdade de executar o programa como você desejar, para qualquer propósito;'
    peronio 'A liberdade de estudar como o programa funciona, e adaptá-lo às suas necessidades. Para tanto, acesso ao código-fonte é um pré-requisito;'
    peronio 'A liberdade de redistribuir cópias de modo que você possa ajudar outros;'
    peronio 'E'
    peronio 'A liberdade de distribuir cópias de suas versões modificadas a outros. Desta forma, você pode dar a toda comunidade a chance de beneficiar de suas mudanças. Para tanto, acesso ao código-fonte é um pré-requisito.\"'
    peronio 'Ou seja, com o softaware livre, você não está preso à vontade das grandes desenvolvedoras de software, você pode saber o que está acontecendo com seu softaware e alterá-lo segundo suas necessidades e vontades, sem depender de outros.'
    p 'Que interessante, eu gostei dessa ideia.'
    peronio 'Ah, sim, é realmente muito incrível.'
    peronio 'Mais alguma dúvida?'
    p 'Bem...'
menu:
    'FPS procedural':
        p 'Eu consigo criar um FPS como Call Of Duty ou Battle Field, mas gerado proceduralmente, numa game jam?'
    'Skirim só que melhor':
        p 'Eu consigo criar um RPG como Skyrim, mas melhor, durante a jam?'
label larijam:
    peronio 'Vai nessa!'
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
    rapha 'Tem várias coisas, por exemplo Toddynho, Cup Noodles, chocolates... Dê uma olhada!'
    show rapha feliz at left
    with move
    hide rapha feliz
    with None

    '{i}Eu vou ao balcão da LariJam...{/i}'

    show thiago feliz
    thiago 'Olá, tudo bem? Você quer comprar alguma coisa?'
menu:
    'Toddynho':
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

'{i}Algum tempo depois...{/i}'

p 'Nossa... Estou caindo de sono.'

menu:
    'Dormir':
        $ dormiu = True
        jump happyending
    'Não! Mais café, quero continuar fazendo meu jogo!':
        show rapha feliz
        rapha 'Ei! Descansar também é importante!'
        rapha 'O objetivo do evento é se divertir, não tem problema se você não acabar seu jogo.'
        rapha '48 horas é um tempo curto para fazer um jogo...'
        rapha 'A ideia é fazer algo mais simples e se divertir mesmo!'
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

#if equipe:
    # treta
