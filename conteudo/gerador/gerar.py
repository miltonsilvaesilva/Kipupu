"""Gera HTML dos posts (posts.py) e renderiza PNG 1080x1350 com Playwright.
Uso: python3 gerar.py [slug ...]"""
import sys, os, json, subprocess, shutil, html
sys.path.insert(0, os.path.dirname(__file__))
from posts import P
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "conteudo", "design")
LOGOS = os.path.join(ROOT, "marca", "logotipos")

CSS = """
:root{--navy:#003A5D;--night:#062B45;--cyan:#28FFF8;--orange:#F26B1D;--peach:#FFE6D5;--bg:#F4F7F9;--ink:#0E2233;--muted:#4F6475;--teal:#0A7C86}
*{margin:0;box-sizing:border-box}body{background:#777;font-family:Inter,sans-serif}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;padding:110px 96px;display:flex;flex-direction:column}
.dark{background:var(--night);color:#EAF3F8}.light{background:var(--bg);color:var(--ink)}.cyan{background:var(--cyan);color:var(--night)}
.k{font:600 30px Inter;letter-spacing:6px;text-transform:uppercase}
.dark .k{color:var(--cyan)}.light .k{color:#C2551A}.cyan .k{color:var(--teal)}
h1{font:700 96px/1.07 Lexend;margin-top:56px}
.dark h1 span{color:var(--cyan)}.light h1 span{color:var(--navy);background:linear-gradient(transparent 62%,var(--cyan) 62%)}.cyan h1 span{color:var(--teal)}
h1 .o{color:#C2551A}
.t2{font:600 64px/1.15 Lexend;margin-top:44px;color:var(--teal)}
.sub{font:500 40px/1.4 Inter;margin-top:44px}.dark .sub{color:#A9C2D3}.light .sub{color:var(--muted)}.cyan .sub{color:#064A57}
.cta{align-self:flex-start;margin-top:56px;font:600 44px Lexend;padding:30px 50px;border-radius:999px}
.dark .cta{background:var(--cyan);color:var(--night)}.cyan .cta{background:var(--night);color:#fff}.cyan .cta b{color:var(--cyan)}.light .cta{background:var(--navy);color:#fff}.light .cta b{color:var(--cyan)}
.dark .cta b{color:var(--night)}
.swipe{position:absolute;right:96px;bottom:96px;font:600 34px Inter}.dark .swipe{color:var(--cyan)}
.logo{position:absolute;left:72px;bottom:84px;height:72px}
.band{position:absolute;left:0;right:0;bottom:0;height:190px;background:var(--night);display:flex;align-items:center;padding:0 72px}.band img{height:80px}
.ico{position:absolute;right:96px;bottom:80px;height:76px}
.bigk{position:absolute;right:-200px;top:130px;height:900px;opacity:.07}
.n{position:absolute;right:96px;top:110px;font:600 30px Inter;color:var(--muted);letter-spacing:2px}
.card{background:#fff;border-radius:48px;padding:80px 72px;margin-top:60px;box-shadow:0 10px 40px rgba(0,58,93,.06);flex:1;margin-bottom:120px;display:flex;flex-direction:column;justify-content:center}
.emo{width:200px;height:200px;border-radius:40px;background:var(--peach);display:flex;align-items:center;justify-content:center;font-size:110px}
.card h2{font:700 76px/1.1 Lexend;margin-top:60px;color:var(--ink)}
.card p{font:400 44px/1.45 Inter;margin-top:30px;color:var(--muted)}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:120px}
.chat{margin-top:70px;display:flex;flex-direction:column;gap:34px}
.b1,.b2{font:700 64px Lexend;padding:34px 52px;border-radius:44px;max-width:max-content}
.b1{background:#fff;color:var(--navy);border-bottom-left-radius:8px}.b2{align-self:flex-end;background:var(--orange);color:#fff;border-bottom-right-radius:8px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:50px}
.cell{height:250px;background:#fff;border:3px solid #D5E0E8;border-radius:28px;display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;font:600 32px/1.25 Lexend;color:var(--navy)}
.cell:nth-child(5){background:var(--navy);color:#fff;border-color:var(--navy)}
.pre{font:500 42px Inter;color:#A9C2D3;margin-top:80px}
.big{font:700 210px/1 Lexend;color:var(--cyan);margin-top:30px;letter-spacing:-4px}
.foot{position:absolute;left:96px;right:96px;bottom:180px;font:400 26px Inter;color:#6F8899}
table{width:100%;border-collapse:separate;border-spacing:0;margin-top:56px;font-size:32px}
td{padding:22px 20px;vertical-align:middle;border-bottom:2px solid #DCE5EC;line-height:1.3}
td.l{font:600 32px Lexend;color:var(--navy);width:230px}
td.a{color:var(--muted)}td.a:before{content:"✕  ";color:var(--orange);font-weight:700}
td.b{background:var(--navy);color:#fff;font-weight:600}td.b:before{content:"✓  ";color:var(--cyan);font-weight:700}
th{font:600 30px Lexend;text-align:left;padding:20px 22px;color:var(--muted)}th.b{background:var(--navy);color:var(--cyan);border-radius:30px 30px 0 0}
tr:last-child td.b{border-radius:0 0 30px 30px}
.steps{margin-top:20px;display:flex;flex-direction:column;gap:26px}
.st{display:flex;gap:36px;align-items:center;background:#0B3A5A;border-radius:32px;padding:30px 40px}
.st b{width:96px;height:96px;border-radius:50%;background:var(--cyan);color:var(--night);font:700 48px Lexend;display:flex;align-items:center;justify-content:center;flex:none}
.st h3{font:600 44px Lexend;color:#fff}.st p{font:400 32px/1.35 Inter;color:#A9C2D3;margin-top:6px}
.row{display:flex;gap:50px;align-items:center;margin-top:30px}
.phone{width:420px;flex:none;border:16px solid var(--ink);border-radius:64px;background:var(--bg);padding:40px 28px 36px}
.phone .hi{font:500 22px Inter;color:var(--muted)}.phone .pt{font:700 32px Lexend;color:var(--navy);margin-top:4px}
.plan{background:var(--navy);border-radius:24px;padding:22px 24px;margin-top:20px;color:#fff}.plan small{font:400 18px Inter;color:#A9C2D3}.plan div{font:700 48px Lexend;color:var(--cyan)}
.qr{background:#fff;border-radius:22px;margin:22px auto 0;width:250px;height:250px;padding:22px}
.pbtn{margin-top:22px;background:var(--cyan);color:var(--night);font:600 24px Lexend;text-align:center;padding:18px;border-radius:999px}
"""

def qr_svg():
    import random
    r = random.Random(7); n = 21; cells = []
    def finder(x, y):
        return f'<rect x="{x}" y="{y}" width="7" height="7" fill="#003A5D"/><rect x="{x+1}" y="{y+1}" width="5" height="5" fill="#fff"/><rect x="{x+2}" y="{y+2}" width="3" height="3" fill="#003A5D"/>'
    for i in range(n):
        for j in range(n):
            if (i < 8 and j < 8) or (i < 8 and j > 12) or (i > 12 and j < 8): continue
            if r.random() < .5: cells.append(f'<rect x="{i}" y="{j}" width="1" height="1" fill="#003A5D"/>')
    return f'<svg viewBox="0 0 21 21" width="100%" height="100%" shape-rendering="crispEdges">{finder(0,0)}{finder(14,0)}{finder(0,14)}{"".join(cells)}</svg>'

def foot(d, theme):
    if d.get("band"): return '<div class="band"><img src="logo-branco.webp"></div>'
    if d["t"] in ("bingo", "compare", "phone"): return '<img class="ico" src="icone-cor.png" style="top:96px;bottom:auto;height:64px">'
    if d.get("logo") or d["t"] in ("statement", "stat", "chat", "steps"):
        if theme == "dark": return '<img class="logo" src="logo-branco.webp">'
        if theme == "light": return '<img class="logo" src="logo-cor.webp">'
    return ""

def slide(d):
    th = d["theme"]; t = d["t"]; h = []
    k = f'<div class="k">{d["kicker"]}</div>' if d.get("kicker") else ""
    if t == "statement":
        bg = '<img class="bigk" src="icone-branco.png">' if th == "dark" else ""
        h.append(bg + k + '<div class="mid">' + f'<h1 style="margin-top:0">{d["title"]}</h1>')
        if d.get("title2"): h.append(f'<div class="t2">{d["title2"]}</div>')
        if d.get("sub"): h.append(f'<div class="sub">{d["sub"]}</div>')
        if d.get("cta"): h.append(f'<div class="cta">{d["cta"]}</div>')
        h.append("</div>")
        if d.get("swipe"): h.append('<div class="swipe">Desliza →</div>')
    elif t == "card":
        h.append(f'<div class="n">{d["n"]}</div>{k}<div class="card"><div class="emo">{d["emoji"]}</div><h2>{d["title"]}</h2><p>{d["body"]}</p></div><img class="ico" src="icone-cor.png">')
    elif t == "chat":
        h.append(f'{k}<div class="chat"><div class="b1">{d["q"]}</div><div class="b2">{d["a"]}</div></div><div class="mid"><h1 style="margin-top:0">{d["title"]}</h1><div class="sub">{d["sub"]}</div></div>')
    elif t == "bingo":
        cells = "".join(f'<div class="cell">{c}</div>' for c in d["cells"])
        h.append(f'{k}<h1 style="font-size:80px;margin-top:24px">{d["title"]}</h1><div class="grid">{cells}</div><div class="sub" style="margin-top:36px;font-weight:600;color:var(--ink)">{d["sub"]}</div>')
    elif t == "stat":
        h.append(f'{k}<div class="pre">{d["pre"]}</div><div class="big">{d["big"]}</div><h1 style="font-size:72px;margin-top:20px">{d["title"]}</h1><div class="sub">{d["sub"]}</div><div class="foot">{d["foot"]}</div>')
    elif t == "compare":
        rows = "".join(f'<tr><td class="l">{a}</td><td class="a">{b}</td><td class="b">{c}</td></tr>' for a, b, c in d["rows"])
        h.append(f'<h1 style="font-size:80px;margin-top:0">{d["title"]}</h1><table><tr><th></th><th>Lavagem tradicional</th><th class="b">KiPUPU</th></tr>{rows}</table>')
    elif t == "steps":
        st = "".join(f'<div class="st"><b>{i+1}</b><div><h3>{a}</h3><p>{b}</p></div></div>' for i, (a, b) in enumerate(d["steps"]))
        h.append(f'<div class="steps">{st}</div>')
    elif t == "phone":
        ph = f'<div class="phone"><div class="hi">Olá!</div><div class="pt">O teu passe</div><div class="plan"><small>Plano mensal</small><div>3 de 4</div><small>lavagens disponíveis este mês</small></div><div class="qr">{qr_svg()}</div><div class="pbtn">Estação mais próxima</div></div>'
        h.append(f'{k}<div class="row"><div><h1 style="font-size:90px;margin-top:0">{d["title"]}</h1></div>{ph}</div><div class="sub">{d["sub"]}</div><div class="cta">{d["cta"]}</div>')
    h.append(foot(d, th))
    return th, "".join(h)

def build(slug):
    d = os.path.join(OUT, slug); os.makedirs(d, exist_ok=True)
    for src, dst in [("kipupu-logo-branco-fundo-escuro.webp", "logo-branco.webp"), ("kipupu-logo-cor.webp", "logo-cor.webp"), ("kipupu-icone-branco-hd.png", "icone-branco.png"), ("kipupu-icone-cor-hd.png", "icone-cor.png")]:
        shutil.copy(os.path.join(LOGOS, src), os.path.join(d, dst))
    secs = []
    for i, s in enumerate(P[slug], 1):
        th, inner = slide(s)
        secs.append(f'<section class="s {th}" id="s{i}">{inner}</section>')
    page = f'<!doctype html><html lang="pt"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>{"".join(secs)}</body></html>'
    open(os.path.join(d, "post.html"), "w").write(page)
    return d, len(P[slug])

if __name__ == "__main__":
    slugs = sys.argv[1:] or list(P)
    jobs = [build(s) for s in slugs]
    js = os.path.join(os.path.dirname(__file__), "render.js")
    subprocess.run(["node", js, json.dumps(jobs)], check=True)
    print("ok", len(jobs))
