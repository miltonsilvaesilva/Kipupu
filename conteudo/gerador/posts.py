# Dados dos posts desenhados pelo gerador. Cada post = lista de slides.
# Tipos: statement, card, bingo, compare, phone, steps
P = {}

P["p02-depende"] = [dict(t="chat", theme="light", kicker="Luanda, todos os dias",
    q="Quanto é?", a="Depende…",
    title="O <span>“depende”</span> mais famoso de Luanda.", sub="Conta aqui a melhor resposta que já ouviste. 😂")]

P["p03-chuva"] = [
 dict(t="statement", theme="dark", kicker="Época das chuvas 🌧️", title="Lavaste ontem.<br>Hoje parece que <span>não.</span>", sub="Porque é que o carro suja tão depressa nesta altura?", swipe=True),
 dict(t="card", theme="light", n="1/4", emoji="💧", title="Gotas com terra", body="A chuva traz pó e areia. Quando a água seca, a sujidade fica na pintura e nos vidros."),
 dict(t="card", theme="light", n="2/4", emoji="🛞", title="Lama nas jantes", body="Poças e ruas de terra atiram lama para as jantes, as cavas das rodas e por baixo do carro."),
 dict(t="card", theme="light", n="3/4", emoji="👟", title="O interior também sofre", body="Sapatos molhados deixam terra nos tapetes. Com o calor, ficam humidade e cheiro."),
 dict(t="card", theme="light", n="4/4", emoji="🪟", title="Vidros e escovas", body="Vidro sujo com chuva é perigoso à noite. Mantém o pára-brisas e as escovas limpos."),
 dict(t="statement", theme="cyan", kicker="E agora?", title="Lavar mais vezes não devia custar mais sábados.", sub="Estamos a preparar uma solução. 👀", cta="Comenta <b>QUERO</b> 👇", band=True),
]

P["p05-problema"] = [dict(t="statement", theme="cyan", kicker="O que pensamos", title="O verdadeiro problema não é o carro sujo.", title2="É todo o trabalho necessário para o manter cuidado.", cta="Concordas? Comenta <b>QUERO</b> 👇", band=True)]

P["p06-bingo"] = [dict(t="bingo", theme="light", kicker="Sábado de lavagem", title="Bingo da lavagem 🎯",
   cells=["Fila de mais de 1 hora","“Quanto é?” “Depende…”","Não há troco","Esqueceram os tapetes","Choveu no dia seguinte","Pagaste e não tens recibo","Ficaram marcas no vidro","Fechado quando chegaste","Preço diferente da última vez"],
   sub="Quantas já te aconteceram? Comenta o número! 👇")]

P["p07-estacoes"] = [dict(t="statement", theme="dark", kicker="Bastidores", title="Nem todas as estações <span>entram.</span>", sub="Estamos a escolher, uma a uma, as estações certificadas da rede KiPUPU. Padrão de qualidade. Avaliação contínua.", cta="Tens uma lavagem? Manda mensagem 💬")]

P["p08-130horas"] = [dict(t="stat", theme="dark", kicker="Faz as contas", pre="2h30 por sábado × 52 sábados =", big="130 horas", title="por ano a tratar de lavar o carro.", sub="Mais de 5 dias inteiros. O que farias com esse tempo?", foot="Cenário ilustrativo: 2h30 por lavagem, uma vez por semana.")]

P["p10-amanha"] = [dict(t="statement", theme="dark", kicker="Sábado, 12 de Dezembro", title="Amanhã contamos <span>tudo.</span>", sub="Activa as notificações. 🔔", cta="Comenta <b>QUERO</b> 👇", logo=True)]

P["p11-conhece"] = [
 dict(t="statement", theme="dark", kicker="Chegou o dia", title="Conhece a <span>KiPUPU.</span>", sub="A plataforma que lava o teu carro.", swipe=True, logo=True),
 dict(t="card", theme="light", n="1/3", emoji="📱", title="Uma app", body="Plano, carros, passe, estações e histórico de lavagens num só lugar."),
 dict(t="card", theme="light", n="2/3", emoji="🗓️", title="Um valor mensal fixo", body="Subscrição paga em Kwanza, de forma digital. Sem dinheiro vivo, sem negociar."),
 dict(t="card", theme="light", n="3/3", emoji="✅", title="Uma rede certificada", body="Estações seleccionadas, com o mesmo padrão de qualidade e avaliação contínua."),
 dict(t="statement", theme="cyan", kicker="Os primeiros 100", title="Queres ser membro fundador?", sub="Estamos a abrir a lista dos primeiros 100 membros em Luanda.", cta="Comenta <b>FUNDADOR</b> 👇", band=True),
]

P["p12-5passos"] = [
 dict(t="statement", theme="dark", kicker="Como funciona", title="Do sofá à estação em <span>5 passos.</span>", swipe=True),
 dict(t="steps", theme="dark", steps=[("Subscreve","Escolhe o plano na app e paga em Kwanza."),("Regista o carro","Pela matrícula. O plano fica ligado ao carro."),("Mostra o QR Code","Um passe seguro, lido na estação."),("Lava","Serviço padronizado e registado."),("Avalia","Dá nota. Se algo correr mal, abre uma reclamação.")]),
 dict(t="statement", theme="cyan", kicker="Simples assim", title="Sem dinheiro vivo.<br>Sem negociar.", sub="Cada lavagem fica no histórico do teu carro.", cta="Comenta <b>FUNDADOR</b> 👇", band=True),
]

P["p13-compara"] = [dict(t="compare", theme="light", title="Não é só o preço.<br>É a <span>experiência.</span>",
  rows=[("Encontrar","Procurar e esperar","Estação próxima, entrada com QR"),("Preço","Negociado a cada visita","Fixo e mensal"),("Qualidade","Depende de quem lava","O mesmo padrão em toda a rede"),("Confiança","Sem registo nem a quem reclamar","Cada lavagem registada e avaliada"),("Pagamento","Dinheiro vivo","Digital, em Kwanza")])]

P["p14-fundadores"] = [
 dict(t="statement", theme="dark", kicker="Membros fundadores", title="Os primeiros <span>100.</span>", sub="Vão ser os primeiros a experimentar a KiPUPU em Luanda e a ajudar-nos a torná-la melhor.", swipe=True, logo=True),
 dict(t="card", theme="light", n="1/3", emoji="🚗", title="Primeiro acesso", body="Os fundadores entram na beta antes de toda a gente."),
 dict(t="card", theme="light", n="2/3", emoji="🗣️", title="A tua voz conta", body="Cada avaliação e sugestão ajuda a melhorar a app e a rede de estações."),
 dict(t="card", theme="light", n="3/3", emoji="💬", title="Como entrar", body="Comenta FUNDADOR. A nossa equipa manda-te mensagem com os próximos passos."),
 dict(t="statement", theme="cyan", kicker="A lista está aberta", title="Queres ser um dos 100?", cta="Comenta <b>FUNDADOR</b> 👇", band=True),
]

P["p15-faq"] = [
 dict(t="statement", theme="dark", kicker="Perguntas e respostas", title="O que vais querer <span>saber.</span>", swipe=True),
 dict(t="card", theme="light", n="1/5", emoji="💵", title="Preciso de dinheiro vivo?", body="Não. Pagas a subscrição na app, em Kwanza, de forma digital."),
 dict(t="card", theme="light", n="2/5", emoji="🏷️", title="O preço muda?", body="Não. É um valor mensal fixo. Sabes sempre quanto pagas."),
 dict(t="card", theme="light", n="3/5", emoji="⭐", title="E se lavarem mal?", body="Avalias cada lavagem na app e, se algo correr mal, abres uma reclamação."),
 dict(t="card", theme="light", n="4/5", emoji="📍", title="Onde posso lavar?", body="Na rede de estações certificadas KiPUPU em Luanda e Icolo e Bengo."),
 dict(t="card", theme="light", n="5/5", emoji="🤫", title="Quanto custa?", body="Anunciamos em breve. Os membros fundadores são os primeiros a saber."),
 dict(t="statement", theme="cyan", kicker="Mais perguntas?", title="Pergunta aqui nos comentários.", sub="Respondemos a todas.", cta="Ou comenta <b>FUNDADOR</b> 👇", band=True),
]

P["p16-natal"] = [dict(t="statement", theme="dark", kicker="Dezembro 🎄", title="Carro limpo para as festas.<br><span>Sábado livre</span> para a família.", sub="É para isso que estamos a construir a KiPUPU.", cta="Comenta <b>FUNDADOR</b> 👇", logo=True)]

P["p17-parceiros"] = [
 dict(t="statement", theme="dark", kicker="Para estações de lavagem", title="Tens uma lavagem?<br>Junta&#8209;te à <span>rede.</span>", swipe=True, logo=True),
 dict(t="card", theme="light", n="1/4", emoji="🔁", title="Clientes recorrentes", body="Condutores com subscrição voltam todas as semanas. Procura mais previsível."),
 dict(t="card", theme="light", n="2/4", emoji="✅", title="Pagamento garantido", body="Recebes por cada serviço válido. Sem negociar com cada cliente."),
 dict(t="card", theme="light", n="3/4", emoji="🔒", title="Menos dinheiro em caixa", body="Pagamentos digitais, mais controlo e mais segurança."),
 dict(t="card", theme="light", n="4/4", emoji="📲", title="Ferramenta simples", body="Uma app fácil para ler o QR Code do cliente e registar a lavagem."),
 dict(t="statement", theme="cyan", kicker="Estação certificada KiPUPU", title="Queres saber como entrar?", sub="Manda mensagem com o nome e a localização da tua estação.", cta="Comenta <b>ESTAÇÃO</b> 👇", band=True),
]

P["p18-passe"] = [dict(t="phone", theme="light", kicker="O teu passe", title="Mostra o QR.<br>Lava.<br><span class='o'>Avalia.</span>", sub="O passe é válido por poucos minutos e lido na estação. Seguro e sem complicações.", cta="Comenta <b>FUNDADOR</b> 👇")]

P["p19-feliz-natal"] = [dict(t="statement", theme="cyan", kicker="25 de Dezembro", title="Feliz Natal! 🎄", sub="Da equipa KiPUPU para ti e para a tua família. Que o próximo ano traga mais tempo para o que importa.", band=True)]

P["p20-ultimo-sabado"] = [dict(t="statement", theme="dark", kicker="26 de Dezembro", title="Último sábado do ano <span>na fila?</span>", sub="Em breve há uma forma melhor.", cta="Comenta <b>FUNDADOR</b> 👇", logo=True)]
