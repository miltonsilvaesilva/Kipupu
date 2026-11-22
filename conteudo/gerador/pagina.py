"""Gera conteudo/agenda-publicacoes.html (página Artifact) e files.json (mapa de imagens)."""
import csv, os, json, html, glob, datetime as dt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = list(csv.DictReader(open(os.path.join(ROOT, "conteudo", "calendario-nov-dez-2026.csv"))))
MES = {"11": "Nov", "12": "Dez"}; DIA = {"seg":"Segunda","ter":"Terça","qua":"Quarta","qui":"Quinta","sex":"Sexta","sab":"Sábado","dom":"Domingo"}
files = {}; cards = []
for r in rows:
    folder = os.path.join(ROOT, r["pasta"]); base = os.path.basename(r["pasta"])
    imgs = sorted(glob.glob(os.path.join(folder, "*.png")))
    thumbs = []
    for k, f in enumerate(imgs, 1):
        pub = f"img/{r['n'].zfill(2)}/{k:02d}.png"; files[pub] = os.path.relpath(f, ROOT)
        thumbs.append(f'<figure><img src="{pub}" alt="Imagem {k} do post {r["n"]}" loading="lazy"><figcaption>{k}</figcaption></figure>')
    d = r["data"]; n = r["n"]
    cards.append(f'''
<article class="post" id="post-{n}" data-n="{n}">
  <div class="when"><span class="num">#{n}</span><span class="day">{DIA[r["dia"]]}</span><span class="date">{d[8:]} {MES[d[5:7]]}</span><span class="hour">{r["hora"]}</span><span class="fase">{html.escape(r["fase"])}</span></div>
  <div class="body">
    <div class="meta"><span class="chip">{html.escape(r["formato"])}</span><span class="chip ghost">{len(imgs)} imagem{"ns" if len(imgs)>1 else ""} · pasta <code>{base}</code></span>
      <label class="done"><input type="checkbox" id="done-{n}"> Agendado</label></div>
    <div class="strip">{"".join(thumbs)}</div>
    <div class="txt"><div class="lbl">Legenda <button type="button" class="copy" data-t="cap-{n}">Copiar legenda</button></div>
      <pre id="cap-{n}" class="caption">{html.escape(r["legenda"])}</pre>
      <div class="lbl">Texto alternativo <button type="button" class="copy" data-t="alt-{n}">Copiar</button></div>
      <p id="alt-{n}" class="alt">{html.escape(r["alt"])}</p>
      <p class="sched">Agendar para: <strong>{d[8:]}/{d[5:7]}/{d[:4]} às {r["hora"]}</strong> (hora de Luanda) · Facebook + Instagram</p></div>
  </div>
</article>''')
PROMPT = ("Abre a página Agenda KiPUPU (este link) e, no Meta Business Suite da página KiPUPU, agenda os posts que ainda não estão agendados. "
          "Para cada post: Criar publicação → marcar Facebook e Instagram → eu carrego as imagens da pasta indicada, por ordem → tu colas a legenda exacta → "
          "em Definições avançadas colas o texto alternativo → Agendar na data e hora indicadas (hora de Luanda). Não publiques nada de imediato; só agenda. "
          "Pára e pergunta-me se algo não corresponder.")
page = f'''<title>Agenda KiPUPU</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&family=Inter:wght@400;500;600&display=swap">
<style>
/* Layout: lista vertical de posts por ordem de data; cada post = bloco de data à esquerda + imagens e legenda */
:root{{--bg:#F4F7F9;--surface:#FFFFFF;--fg:#0E2233;--muted:#4F6475;--line:#DCE5EC;--navy:#003A5D;--accent:#0A7C86;--cyan:#28FFF8;--done:#E6F7EE;
--display:"Lexend",system-ui,sans-serif;--text:"Inter",system-ui,sans-serif}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#061C2C;--surface:#0B2A40;--fg:#E7F0F6;--muted:#9FB6C6;--line:#1C4560;--navy:#0F4A72;--accent:#28FFF8;--done:#0F3B2E;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#061C2C;--surface:#0B2A40;--fg:#E7F0F6;--muted:#9FB6C6;--line:#1C4560;--navy:#0F4A72;--accent:#28FFF8;--done:#0F3B2E;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--text);font-size:15px;line-height:1.5;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:24px 64px}}
.wrap{{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:20px}}
header h1{{font:700 clamp(26px,4vw,36px)/1.1 var(--display);text-wrap:balance}}
header p{{color:var(--muted);margin-top:6px;max-width:68ch}}
.how{{background:var(--navy);color:#EAF3F8;border-radius:16px;padding:18px 20px;display:grid;gap:10px}}
.how h2{{font:600 17px var(--display);color:var(--cyan)}}
.how ol{{padding-left:20px;display:grid;gap:4px}}
.how pre{{white-space:pre-wrap;background:rgba(255,255,255,.08);border-radius:10px;padding:12px;font:13px/1.5 var(--text)}}
.how .copy{{background:var(--cyan);color:#062B45;border-color:transparent}}
.bar{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;color:var(--muted);font-size:14px}}
.post{{background:var(--surface);border:1px solid var(--line);border-radius:16px;display:grid;grid-template-columns:150px minmax(0,1fr);overflow:hidden}}
.post.is-done{{background:var(--done)}}
.when{{background:var(--navy);color:#fff;padding:16px;display:flex;flex-direction:column;gap:2px;font-variant-numeric:tabular-nums}}
.when .num{{font:600 13px var(--text);opacity:.7}}.when .day{{font:500 14px var(--text)}}
.when .date{{font:700 26px/1.1 var(--display)}}.when .hour{{font:600 20px var(--display);color:var(--cyan)}}
.when .fase{{margin-top:auto;font-size:12px;opacity:.75}}
.body{{padding:16px;display:grid;gap:12px;min-width:0}}
.meta{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.chip{{font:600 12px var(--text);padding:4px 10px;border-radius:999px;background:var(--navy);color:#fff}}
.chip.ghost{{background:transparent;color:var(--muted);border:1px solid var(--line)}}
.chip code{{font-size:11px}}
.done{{margin-left:auto;font-weight:600;display:flex;gap:6px;align-items:center;cursor:pointer}}
.strip{{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px}}
figure{{flex:none;width:112px;position:relative}}figure img{{width:112px;height:140px;object-fit:cover;border-radius:8px;border:1px solid var(--line);display:block}}
figcaption{{position:absolute;top:4px;left:4px;background:rgba(6,43,69,.85);color:#fff;font:600 11px var(--text);border-radius:6px;padding:1px 6px}}
.lbl{{font:600 13px var(--display);color:var(--accent);display:flex;gap:10px;align-items:center;margin-top:4px}}
.caption{{white-space:pre-wrap;font:14px/1.5 var(--text);background:var(--bg);border-radius:10px;padding:12px;border:1px solid var(--line)}}
.alt{{color:var(--muted);font-size:14px}}
.sched{{font-size:14px}}
.copy{{font:600 12px var(--text);padding:5px 12px;border-radius:999px;border:1px solid var(--line);background:var(--surface);color:var(--fg);cursor:pointer}}
.copy:focus-visible,.done input:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.copy.ok{{background:var(--accent);color:var(--bg);border-color:transparent}}
@media (max-width:640px){{.post{{grid-template-columns:1fr}}.when{{flex-direction:row;flex-wrap:wrap;gap:8px;align-items:baseline}}.when .fase{{margin-top:0}}}}
</style>
<div class="wrap">
<header><h1>Agenda KiPUPU · 22 Nov – 26 Dez</h1>
<p>20 publicações para o Facebook e o Instagram. Cada bloco tem a data e hora, as imagens por ordem, a legenda e o texto alternativo prontos a copiar.</p></header>
<section class="how"><h2>Como agendar com a extensão Claude no Chrome</h2>
<ol><li>Descarrega e descomprime o <strong>KiPUPU-agendar-22nov-26dez.zip</strong> no computador. A extensão não consegue escolher ficheiros por ti: quando pedir, carregas tu as imagens da pasta indicada.</li>
<li>Abre o Meta Business Suite da página KiPUPU num separador e esta página noutro.</li>
<li>Na extensão Claude, cola a instrução abaixo.</li>
<li>Marca <strong>Agendado</strong> em cada post concluído. Fica guardado só neste browser.</li></ol>
<div class="lbl" style="color:var(--cyan)">Instrução para a extensão <button type="button" class="copy" data-t="prompt">Copiar instrução</button></div>
<pre id="prompt">{html.escape(PROMPT)}</pre></section>
<div class="bar"><span id="count"></span></div>
{"".join(cards)}
</div>
<script>
(function(){{
  function store(k,v){{try{{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}}catch(e){{return null}}}}
  function update(){{var n=document.querySelectorAll('.done input:checked').length;document.getElementById('count').textContent=n+' de {len(rows)} agendados'}}
  document.querySelectorAll('.done input').forEach(function(cb){{
    var post=cb.closest('.post');cb.checked=store(cb.id)==='1';post.classList.toggle('is-done',cb.checked);
    cb.addEventListener('change',function(){{store(cb.id,cb.checked?'1':'0');post.classList.toggle('is-done',cb.checked);update()}});
  }});update();
  document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{
    var el=document.getElementById(b.dataset.t),t=el.innerText,label=b.textContent;
    function ok(){{b.textContent='Copiado';b.classList.add('ok');setTimeout(function(){{b.textContent=label;b.classList.remove('ok')}},1500)}}
    function sel(){{var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Seleccionado: Ctrl+C'}}
    if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(t).then(ok,sel)}}else sel();
  }})}});
}})();
</script>'''
open(os.path.join(ROOT, "conteudo", "agenda-publicacoes.html"), "w").write(page)
json.dump(files, open(os.path.join(ROOT, "conteudo", "gerador", "files.json"), "w"), indent=0)
print(len(files), "imagens")
