label lugar:
    scene bg cb_circulo
    show akari olhos_fechados
    akari 'Ah sim, é verdade...'
    show akari feliz
    akari 'A Livre Jam vai ser lá no Instituto de Computação, nas salas do IC 3,5. Sabe onde fica?'
    show akari olhos_fechados
    p 'Mais ou menos...'
    show akari feliz
    akari 'Sabe onde fica o RS?'
    show akari olhos_fechados
    p 'Sei.'
    show akari feliz
    akari 'O IC 3 e o IC 3,5 ficam na mesma rua que o RS, um pouco mais abaixo. Vai começar 19 horas. Tudo certo então?'
    show akari olhos_fechados
    p 'Tudo certo, só mais uma pergunta...'
    show akari feliz
    p 'Se são 48h... Vocês dormem lá no IC e tomam banho?'
    show akari olhos_fechados
    akari 'Não é todo mundo, mas você pode. Tem chuveiro e você pode dormir em algum cantinho, ou na sala do Centro Acadêmico, já que o IC não fecha.'
    show akari feliz
    akari 'Mas não é todo mundo que dorme não, hehe.'
    show akari olhos_fechados
    p 'Entendo...'
    show akari feliz
    p 'Fechado então. Eu só preciso ir ver uma prova com um professor e me arrumar, 19 horas estarei lá.'
    show akari olhos_fechados
    akari 'Ótimo. Não é pra furar, entendido?'
    akari 'Se furar, vai ficar sem Toddynho, já deixo o aviso.'
    show akari feliz
    akari 'Eu te vejo lá então, até mais, [p]!'
    show akari olhos_fechados
    p 'Tchau Akari, até lá!'
    show akari feliz at right
    with move
    hide akari feliz
    with None
label sala:
    '{i}Eu me despeço da Akari e vou até a sala da matéria que mais está me preocupando. Preciso ver o resultado dessa prova...{/i}'
    scene bg sala_prof
    '{i}Eu não devo ter ido mal, eu estudei bastante, acho que meu resultado deve ter sido satisfatório...{/i}'
    '{i}Cheguei à sala. O professor está na mesa e prova está ali virada. Só tem uma... Deve ser a minha. Vai ser agora, eu pego a prova...{/i}'
    '{i}O QUÊ?! NÂO PODE SER!{/i}'
    '{i}EU NÃO POSSO TER TIRADO ZERO!!!!!!!!{/i}'
    '{i}Mas pera, isso está errado...{/i}'
    '{i}Eu fui bem nessa prova, não é possível!{/i}'
    p 'Professor, com licença...'
    'Professor' 'Olá, jovem, no que posso te ajudar?'
    p'Eu acho que tem algum erro na correção da minha prova... Olha aqui, essas respostas estão certas, era pra eu ter tirado, pelo menos, 9,0 nessa prova. Houve algum engano...'
    show prof
    professor 'Eu sei, MWUAHAHAHAHAHAHAHAHAHAH!'
    show prof aura
    professor 'Era pra você ter tirado dez nessa prova, mas eu te dei zero. Não me leve a mal, não é nada pessoal. Sei que você é uma pessoa muito esforçada, mas eu vou me sentir mal se não deixar uma certa quantidade de alunos de exame.'
    show prof
    professor 'E nesse semestre pessoas demais estão bem. Você, por exemplo, é excelente: está indo muito bem. Eu precisava deixar algumas pessoas de exame, isso não podia ficar assim.'
    show prof aura
    professor 'Eu escolhi você porque vocẽ está indo tão bem que um examezinho não vai te fazer mal, espero que você me entenda.'
    show prof at left
    with move
    hide prof
    '{i}Eu saio correndo da sala aos prantos. Não consigo nem mais olhar na cara desse professor maldito...{/i}'
    '{i}O que fazer agora? Eu estou ferrado, esse maldito vai me pôr de exame, vou ter que estudar muito agora...{/i}'
    '{i}Deixa eu pensar...{/i}'
    '{i}Essa foi a segunda prova, eu tirei dez na primeira prova. Se eu tirar dez na terceira, eu passo sem exame. Ainda há esperança!{/i}'
    '{i}É melhor eu avisar sobre esse desgraçado na DAC e estudar muito. Preciso tirar 10, mas...{/i}'
    '{i}Droga, eu prometi à Akari que iria ao evento dela, o que eu vou fazer?!{/i}'
menu:
    'Ir à Jam':
        '{i}Não, eu não posso furar, agora já prometi que iria, não vou faltar. Vai ser bom ir até lá, vou me distrair um pouco.{/i}'
        jump chegada
    'Desistir':
        if estudar:
            '{i}Eu já planejava estudar, agora não vai ter jeito. Depois ligo pra Akari, mas vou ter que deixar pra próxima.{/i}'
            $ desistir = True
            jump sadending
        else:
            '{i}É, parece que está difícil, melhor eu deixar esse evento da Akari pra lá...{/i}'
            '{i}Mas será que essa é a melhor opção mesmo? Ir pode ser uma boa...{/i}'
            jump desistir
menu desistir:
    'Não desistir':
        '{i}Ah cara, vai ser divertido lá, e a Akari vai ficar chateada se eu não for, melhor eu ir... Eu vou!{/i}'
        jump chegada
    'Desistir':
        '{i}Melhor não, preciso estudar, estou quase indo pra exame... Desculpa Akari, mas não vai rolar.{/i}'
        $ desistir = True
        jump sadending
