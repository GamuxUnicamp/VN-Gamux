label sadending:
    if not desistir:
        hide akari feliz
        'Eu recusei o convite da Akari e não fui à Livre Jam.'
    else:
        'Acabei desistindo e não fui à Jam.'
        show akari olhos_fechados
        akari 'Sem Toddynho pra você.'
        hide akari
    'Este foi o final de semana mais entediante da minha vida, eu deveria ter ido à Jam!'
    'FIM DE JOGO'
    return

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
        return

label happyending:
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
        return
