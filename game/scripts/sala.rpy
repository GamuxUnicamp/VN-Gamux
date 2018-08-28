label lugar:
    akari 'Ah sim, é verdade...'
    akari 'A Livre Jam vai ser lá no Instituto de Computação, nas salas do IC 3,5. Sabe onde fica?'
    p 'Mais ou menos...'
    akari 'Sabe onde fica o RS?'
    p 'Sei.'
    akari 'O IC 3 e o IC 3,5 ficam na mesma rua que o RS, um pouco mais abaixo. Vai começar 19 horas. Tudo certo então?'
    p 'Tudo certo, só mais uma pergunta...'
    p 'Se são 48h... Vocês dormem lá no IC e tomam banho?'
    akari 'Não é todo mundo, mas você pode. Tem chuveiro e você pode dormir em algum cantinho, ou na sala do Centro Acadêmico, já que o IC não fecha.'
    akari 'Mas não é todo mundo que dorme não, hehe.'
    p 'Entendo...'
    p 'Fechado então. Eu só preciso ir ver uma prova com um professor e me arrumar, 19 horas estarei lá.'
    akari 'Ótimo. Não é pra furar, entendido?'
    show akari olhos_fechados
    akari 'Se furar, vai ficar sem Toddynho, já deixo o aviso.'
    show akari feliz
    akari 'Eu te vejo lá então, até mais! [p]'
    p 'Tchau Akari, até lá!'
    show akari feliz at right
    with move
    hide akari feliz
    with None
label sala:
    'Eu me despeço da Akari e vou até a sala da matéria que mais está me preocupando. Preciso ver o resultado dessa prova...'
    'Eu não devo ter ido mal, eu estudei bastante, acho que meu resultado deve ter sido satisfatório...'
    'Cheguei à sala. O professor está na mesa e prova está ali virada. Só tem uma... Deve ser a minha. Vai ser agora, eu pego a prova...'
    'O QUÊ?! NÂO PODE SER!'
    'EU NÃO POSSO TER TIRADO ZERO!!!!!!!!'
    'Mas pera, isso está errado...'
    'Eu fui bem nesse prova, não é possível!'
    p 'Professor, com licença...'
    'Professor' 'Olá, jovem, no que posso te ajudar?'
    'Eu acho que tem algum erro na correção da minha prova... Olha aqui, essas respostas estão certas, era pra eu ter tirado, pelo menos, 9,0 nessa prova. Houve algum engano...'
    professor 'Eu sei, MWUAHAHAHAHAHAHAHAHAHAH!'
    professor 'Era pra você ter tirado dez nessa prova, mas eu te dei zero. Não me leve a mal, não é nada pessoal. Sei que você é uma pessoa muito esforçada, mas eu vou me sentir mal se não deixar uma certa quantidade de alunos de exame.'
    professor 'E nesse semestre pessoas demais estão bem. Você, por exemplo, é excelente: está indo muito bem. Eu precisava deixar algumas pessoas de exame, isso não podia ficar assim.'
    professor 'Eu escolhi você porque vocẽ está indo tão bem que um examezinho não vai te fazer mal, espero que você me entenda.'
    'Eu saio correndo da sala aos prantos. Não consigo nem mais olhar na cara desse professor maldito...'
    'O que fazer agora? Eu estou ferrado, esse maldito vai me pôr de exame, vou ter que estudar muito agora...'
    'Deixa eu pensar...'
    'Essa foi a segunda prova, eu tirei dez na primeira prova. Se eu tirar dez na terceira, eu passo sem exame. Ainda há esperança!'
    'É melhor eu avisar sobre esse desgraçado na DAC e estudar muito. Preciso tirar 10, mas...'
    'Droga, eu prometi à Akari que iria ao evento dela, o que eu vou fazer?!'
menu:
    'Ir à Jam':
        'Não, eu não posso furar, agora já prometi que iria, não vou faltar. Vai ser bom ir até lá, vou me distrair um pouco.'
        jump chegada
    'Desistir':
        if estudar:
            'Eu já planejava estudar, agora não vai ter jeito. Depois ligo pra Akari, mas vou ter que deixar pra próxima.'
            $ desistir = True
            jump sadending
        else:
            'É, parece que está difícil, melhor eu deixar esse evento da Akari pra lá...'
            'Mas será que essa é a melhor opção mesmo? Ir pode ser uma boa...'
            jump desistir
menu desistir:
    'Não desistir':
        'Ah cara, vai ser divertido lá, e a Akari vai ficar chateada se eu não for, melhor eu ir... Eu vou!'
        jump chegada
    'Desistir':
        'Melhor não, preciso estudar, estou quase indo pra exame... Desculpa Akari, mas não vai rolar.'
        $ desistir = True
        jump sadending
