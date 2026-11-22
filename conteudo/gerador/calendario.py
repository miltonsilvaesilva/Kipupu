"""Gera conteudo/calendario-nov-dez-2026.md, .csv e a pasta agendar/ (imagens por data)."""
import os, csv, shutil, glob, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = os.path.join(ROOT, "conteudo", "design")
H = " #KiPUPU #Luanda"
C = [
# data, hora, fase, pilar, formato, pasta(design), padrão de ficheiros, legenda, alt
("2026-11-22","19:00","A Teaser","Sábado perdido","Carrossel 7","post-01-sabado","slide-0*.png",
 "Duas horas e meia para lavar um carro. Quem nunca? 😅\n\nDiz aqui em baixo: qual destes passos te irrita mais? 1, 2, 3, 4 ou 5?\n\nEstamos a preparar uma coisa para devolver o teu sábado. Comenta QUERO e és dos primeiros a saber. 👇"+H,
 "Carrossel ilustrado com a manhã de um condutor em Luanda, das 08:00 às 10:30: procurar, esperar, negociar, pagar e torcer pelo resultado."),
("2026-11-23","19:00","A Teaser","Sábado perdido","Imagem","p02-depende","0*.png",
 "O “depende” mais famoso de Luanda. 😂\n\nQual foi a resposta mais criativa que já ouviste quando perguntaste o preço de uma lavagem? Conta aqui.\n\nE se o preço fosse sempre o mesmo? 👀"+H,
 "Dois balões de conversa: “Quanto é?” e “Depende…”, com o texto “O depende mais famoso de Luanda”."),
("2026-11-24","19:00","A Teaser","Cuidar do carro","Carrossel 6","p03-chuva","0*.png",
 "Lavaste ontem e hoje já parece que não? 🌧️ Na época das chuvas é normal. Desliza para perceber porquê.\n\nGuarda este post e partilha com quem vive a lavar o carro. 📌\n\nComenta QUERO para saberes primeiro o que estamos a preparar. 👇"+H,
 "Carrossel sobre a sujidade do carro na época das chuvas: gotas com terra, lama nas jantes, interior com terra e vidros sujos."),
("2026-11-26","19:00","A Teaser","Sábado perdido","Imagem + sondagem nos stories","post-04-sondagem","feed-*.png",
 "Sê sincero. ⏱️ Responde aqui em baixo: A, B, C ou D.\n\nTambém há sondagem nos stories. No domingo partilhamos os resultados nos stories. 👀"+H,
 "Pergunta “Quanto tempo perdeste na tua última lavagem?” com quatro opções: menos de 1 hora, entre 1 e 2 horas, mais de 2 horas, já perdi a conta."),
("2026-11-27","19:00","A Teaser","Sábado perdido","Imagem","p05-problema","0*.png",
 "Ninguém se importa de ter o carro limpo. O que cansa é tudo o que vem antes: procurar, esperar, negociar…\n\nConcordas? Comenta QUERO e acompanha o que estamos a preparar. 👇"+H,
 "Texto: O verdadeiro problema não é o carro sujo. É todo o trabalho necessário para o manter cuidado."),
("2026-11-28","08:00","A Teaser","Sábado perdido","Imagem","p06-bingo","0*.png",
 "Bingo da lavagem de sábado! 🎯\n\nQuantas destas já te aconteceram? Comenta o número (e marca aquele amigo que faz bingo todas as semanas 😂)."+H,
 "Cartão de bingo com 9 situações comuns numa lavagem: fila de mais de 1 hora, “depende”, não há troco, esqueceram os tapetes, choveu no dia seguinte, sem recibo, marcas no vidro, fechado, preço diferente."),
("2026-11-30","19:00","A Teaser","Bastidores","Imagem (trocar por Reel quando houver filmagem)","p07-estacoes","0*.png",
 "Nem todas as estações entram na rede KiPUPU. 💧 Estamos a escolher, uma a uma, as que cumprem o nosso padrão de qualidade.\n\nTens uma lavagem e queres fazer parte? Manda-nos mensagem."+H,
 "Texto: Nem todas as estações entram. Estamos a escolher as estações certificadas da rede KiPUPU."),
("2026-12-01","19:00","A Teaser","Sábado perdido","Imagem","p08-130horas","0*.png",
 "Fizemos as contas. 🧮 Se gastas 2h30 por sábado a tratar de lavar o carro, são 130 horas por ano. Mais de 5 dias inteiros!\n\nO que farias com esse tempo? Conta aqui. 👇"+H,
 "2h30 por sábado vezes 52 sábados é igual a 130 horas por ano, mais de 5 dias inteiros. Cenário ilustrativo."),
("2026-12-03","19:00","A Teaser","Convite","Imagem","post-06-nome","feed-*.png",
 "KiPUPU quer dizer “o que popou”. 🙌\n\nPopar tempo. Popar dinheiro. Popar a paciência que fica na fila todos os sábados.\n\nNo sábado contamos tudo. Comenta QUERO e és dos primeiros a saber. 👇"+H,
 "Ícone KiPUPU com o texto: KiPUPU, o que popou. Popar tempo, popar dinheiro, popar a paciência da fila de sábado."),
("2026-12-04","19:00","A Teaser","Convite","Imagem","p10-amanha","0*.png",
 "Amanhã. 🔔 Activa as notificações da página para não perderes.\n\nJá comentaste QUERO? Ainda vais a tempo. 👇"+H,
 "Texto: Amanhã contamos tudo. Activa as notificações."),
("2026-12-05","08:00","B Revelação","Como funciona","Carrossel 5","p11-conhece","0*.png",
 "Chegou o dia: conhece a KiPUPU, a plataforma que lava o teu carro. 💧\n\nUma app, um valor mensal fixo e uma rede de estações certificadas em Luanda. Sem dinheiro vivo, sem negociar, sem sorte.\n\nEstamos a abrir a lista dos primeiros 100 membros fundadores. Comenta FUNDADOR e a nossa equipa fala contigo. 👇"+H,
 "Carrossel de apresentação da KiPUPU: uma app, um valor mensal fixo pago em Kwanza e uma rede de estações certificadas. Convite para membro fundador."),
("2026-12-07","19:00","B Revelação","Como funciona","Carrossel 3","p12-5passos","0*.png",
 "Do sofá à estação em 5 passos. 📱➡️🚗\n\n1. Subscreve\n2. Regista o carro\n3. Mostra o QR Code\n4. Lava\n5. Avalia\n\nGuarda para mostrares a quem ainda negoceia o preço todos os sábados. 📌 Comenta FUNDADOR para entrares na lista. 👇"+H,
 "Os 5 passos da KiPUPU: subscrever, registar o carro, mostrar o QR Code, lavar e avaliar."),
("2026-12-08","19:00","B Revelação","Como funciona","Imagem","p13-compara","0*.png",
 "Não é só o preço. É a experiência. ✅\n\nQual destas diferenças te faz mais falta? Comenta aqui.\n\nQueres ser membro fundador? Comenta FUNDADOR. 👇"+H,
 "Tabela a comparar a lavagem tradicional com a KiPUPU: encontrar, preço, qualidade, confiança e pagamento."),
("2026-12-10","19:00","B Revelação","Convite","Carrossel 5","p14-fundadores","0*.png",
 "Os primeiros 100. 🚗 Os membros fundadores vão ser os primeiros a experimentar a KiPUPU em Luanda e a ajudar-nos a torná-la melhor.\n\nComo entrar? Comenta FUNDADOR e a nossa equipa manda-te mensagem com os próximos passos. 👇"+H,
 "Carrossel sobre os 100 membros fundadores: primeiro acesso à beta, a tua voz conta, como entrar."),
("2026-12-11","19:00","B Revelação","Como funciona","Carrossel 7","p15-faq","0*.png",
 "As perguntas que vais querer fazer, já respondidas. 👇\n\nFicou alguma de fora? Pergunta aqui nos comentários, respondemos a todas.\n\nPara entrares na lista de fundadores, comenta FUNDADOR."+H,
 "Perguntas e respostas: dinheiro vivo, preço fixo, o que fazer se lavarem mal, onde lavar e quando é anunciado o preço."),
("2026-12-12","08:00","B Revelação","Sábado perdido","Imagem","p16-natal","0*.png",
 "Dezembro é para a família, não para a fila da lavagem. 🎄\n\nÉ para isso que estamos a construir a KiPUPU. Comenta FUNDADOR e sê dos primeiros 100. 👇"+H,
 "Texto: Carro limpo para as festas. Sábado livre para a família."),
("2026-12-14","19:00","B Revelação","Bastidores","Carrossel 6 (estações)","p17-parceiros","0*.png",
 "Donos de lavagens: isto é para vocês. 💧\n\nClientes recorrentes, pagamento garantido por cada serviço válido e menos dinheiro em caixa.\n\nQueres que a tua estação faça parte da rede KiPUPU? Comenta ESTAÇÃO ou manda mensagem com o nome e a localização. 👇"+H,
 "Carrossel para estações de lavagem: clientes recorrentes, pagamento garantido, menos dinheiro em caixa, ferramenta simples para ler o QR Code."),
("2026-12-15","19:00","B Revelação","Como funciona","Imagem","p18-passe","0*.png",
 "Mostra o QR. Lava. Avalia. 📲\n\nO teu passe KiPUPU é válido por poucos minutos e é lido na estação. Seguro e sem complicações.\n\nComenta FUNDADOR para entrares na lista. 👇"+H,
 "Ecrã da app KiPUPU com o passe: plano mensal, 3 de 4 lavagens disponíveis e um QR Code. Texto: Mostra o QR. Lava. Avalia."),
("2026-12-25","10:00","B Revelação","Comunidade","Imagem","p19-feliz-natal","0*.png",
 "Feliz Natal! 🎄 Da equipa KiPUPU para ti e para a tua família.\n\nQue o próximo ano traga mais tempo para o que importa. 💙"+H,
 "Mensagem de Feliz Natal da equipa KiPUPU."),
("2026-12-26","08:00","B Revelação","Sábado perdido","Imagem","p20-ultimo-sabado","0*.png",
 "Último sábado do ano na fila da lavagem? 😅\n\nEm breve há uma forma melhor. Comenta FUNDADOR para seres dos primeiros. 👇"+H,
 "Texto: Último sábado do ano na fila? Em breve há uma forma melhor."),
]
DIAS = ["seg","ter","qua","qui","sex","sab","dom"]
import datetime as dt
out = os.path.join(ROOT, "conteudo", "agendar")
os.makedirs(out, exist_ok=True)
for x in glob.glob(os.path.join(out, '2026-*')): shutil.rmtree(x)
rows = []
for i, (data, hora, fase, pilar, fmt, pasta, pat, leg, alt) in enumerate(C, 1):
    d = dt.date.fromisoformat(data); dia = DIAS[d.weekday()]
    files = sorted(glob.glob(os.path.join(D, pasta, pat)))
    assert files, pasta
    nome = f"{data}_{dia}_{hora.replace(':','h')}_{i:02d}-{re.sub(r'^(post|p)-?[0-9]+-','',pasta)}"
    dst = os.path.join(out, nome); os.makedirs(dst)
    for k, f in enumerate(files, 1): shutil.copy(f, os.path.join(dst, f"{k:02d}.png"))
    open(os.path.join(dst, "legenda.txt"), "w").write(leg + "\n\n---\nTexto alternativo: " + alt + "\n")
    rows.append(dict(n=i, data=data, dia=dia, hora=hora, fase=fase, pilar=pilar, formato=fmt, imagens=len(files), pasta=f"conteudo/agendar/{nome}", legenda=leg, alt=alt))
with open(os.path.join(ROOT, "conteudo", "calendario-nov-dez-2026.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
md = ["# Calendário · 22 Nov – 26 Dez 2026", "", "Facebook + Instagram, ao mesmo tempo (no Meta Business Suite, marcar as duas contas). Horas de Luanda (WAT).", "Cada pasta em `conteudo/agendar/` tem as imagens por ordem e um `legenda.txt` pronto a copiar.", "",
      "| # | Data | Hora | Fase | Pilar | Formato | Pasta |", "|---|---|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['n']} | {r['dia'].capitalize()} {r['data'][8:]}/{r['data'][5:7]} | {r['hora']} | {r['fase']} | {r['pilar']} | {r['formato']} | `{os.path.basename(r['pasta'])}` |")
md += ["", "## Legendas", ""]
for r in rows:
    md += [f"### {r['n']}. {r['dia'].capitalize()} {r['data'][8:]}/{r['data'][5:7]} · {r['hora']} · {r['formato']}", "", r["legenda"], "", f"*Texto alternativo:* {r['alt']}", ""]
open(os.path.join(ROOT, "conteudo", "calendario-nov-dez-2026.md"), "w").write("\n".join(md))
print(len(rows), "posts")
