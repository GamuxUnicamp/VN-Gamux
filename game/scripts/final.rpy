label sadending:
    if not desistir:
        hide akari feliz
        '{i}Eu recusei o convite da Akari e não fui à Livre Jam.{/i}'
    else:
        '{i}Acabei desistindo e não fui à Jam.{/i}'
        show akari olhos_fechados
        akari 'Sem Toddynho pra você.'
        hide akari
    '{i}Este foi o final de semana mais entediante da minha vida, eu deveria ter ido à Jam!{/i}'
    'FIM DE JOGO'
    return

label sleepending:
    if dormiu == False:
        $ happyending = False
        '{i}Um tempo depois...{/i}'
        '{i}O que está acontecendo?{/i}'
        '{i}Está tudo escurecendo...{/i}'
        '{i}Você sucumbe ao sono, seu corpo cai sobre a mesa.{/i}'
        '{i}Sua cabeça inevitavelmente bate no teclado...{/i}'
        '{i}E pressiona a tecla Backspace, que começa a apagar o código e tudo que você tinha feito...{/i}'
        '{i}E todo o seu jogo se perde. Todo o seu trabalho.{/i}'
        'FIM DE JOGO'
        return

label happyending:
    if happyending == True:
        '{i}Que bom que descansei um pouco, isso certamente vai melhorar meu rendimento!{/i}'

        '{i}O tempo passa... Você desenvolve um jogo e se diverte muito na jam.{/i}'

        '{i}E, finalmente, o tempo acaba. Você tem um jogo simples, mas que fez com muito carinho.{/i}'

        show akari feliz at left
        with None
        show akari feliz at center
        with move
        akari 'Está na hora do encerramento e da apresentação dos jogos!'
        show akari olhos_fechados
        p 'Apresentação dos jogos?'
        akari 'Sim! Todos que quiserem podem apresentar o que fizeram! Você quer apresentar seu jogo?'
        show akari feliz

        menu:
            'Claro!':
                show akari olhos_fechados
                akari 'Então vamos pro auditório!'
            'Hm... Não sei.':
                show akari olhos_fechados
                akari 'Não se preocupe, é só uma apresentação rápida sobre a sua ideia e as ferramentas que você usou.'
                show akari feliz
                akari 'E ninguém está aqui para julgar.'
                show akari olhos_fechados
                akari 'É que é sempre incrível ver como o mesmo tema pode dar origem a vários jogos diferentes!'
            'Não.':
                show akari olhos_fechados
                akari 'Ok! Assista as apresentações então!'

        show akari at left
        with move
        hide akari

        '{i}Nós do Gamux te agradecemos por ter jogado nossa Visual Novel de divulgação da Livre Game Jam!{/i}'
        '{i}Esperamos que tenha conhecido melhor a entidade e se divertido.{/i}'
        '{i}Venha para a Livre Game Jam! Está chegando! *-*{/i}'
        return
