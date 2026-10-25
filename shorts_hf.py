#!/usr/bin/env python3
"""İSG-PRO Shorts, HyperFrames sürümü. Kullanım: python3 shorts_hf.py sorular.json cikti_klasoru
JSON biçimi mevcut shorts_uret.py ile aynı: no, sinif, konu, soru, secenekler[4-5], dogru (A-E), aciklama, kaynak.
Gerekenler: node, npx hyperframes, ffmpeg, gsap.min.js (bu dosyanın yanında)."""
import json, os, sys, shutil, subprocess, html
W=1080
FIT=r'''const DOG=%d;
(function(){const main=document.getElementById('main');const q=main.querySelector('.q');const ots=[...main.querySelectorAll('.ot')];const exp=main.querySelector('.exp');
let fs=52,os=44;const lim=1180;
function h(){let b=0;main.querySelectorAll('.opt').forEach(o=>{b=Math.max(b,o.offsetTop+o.offsetHeight)});return b}
while(h()>lim&&fs>34){fs-=2;os-=2;q.style.fontSize=fs+'px';ots.forEach(o=>o.style.fontSize=os+'px');}
const opts=[...main.querySelectorAll('.opt')];const c=opts[DOG];const qb=q.offsetTop+q.offsetHeight+30;
window.__dy=qb-c.offsetTop;exp.style.top=(qb+c.offsetHeight+22)+'px';})();
'''
def build(q, d):
    letters="ABCDE"; no=q.get("no",1); sec=q["secenekler"]; dog=letters.index(q["dogru"])
    n_=len(sec); QS=2.0; BS=QS+1.0+n_*.35+.4; AS=BS+15.0; CS=AS+7.0; T=CS+2.5
    e=html.escape
    opts=''.join(f'<div class="opt o{i}"><div class="g"></div><span class="lt">{letters[i]}</span><span class="ot">{e(s)}</span></div>' for i,s in enumerate(sec))
    box=f'''<div id="main" class="clip" data-start="0" data-duration="{T}" style="left:50px;top:190px;width:880px">
<div class="tag">SORU #{no} · {e(q["konu"])}</div>
<div class="q">{e(q["soru"])}</div>
<div class="opts">{opts}</div>
<div class="exp"><b>Açıklama</b><br>{e(q["aciklama"])}<div class="src">Kaynak: {e(q["kaynak"])}</div></div>
</div>'''
    cover=f'''<div id="cov" class="clip" data-start="0" data-duration="{QS+.4}" style="left:0;top:0;width:1080px;height:1920px;background:#0D1B2A">
<div class="cl">İsg <span style="color:#0B1F3A">Pro</span></div><div class="cn">SORU #{no}</div><div class="ck">{e(q["konu"])}</div></div>'''
    close=f'''<div id="cls" class="clip" data-start="{CS}" data-duration="{T-CS}" style="left:0;top:0;width:1080px;height:1920px;background:#0D1B2A">
<div class="cc1">Her gün yeni soru için<br>abone ol!</div><div class="cc2">isg-pro.com</div></div>'''
    bars=f'''<div id="trk" class="clip" data-start="{QS}" data-duration="{AS-QS}" style="left:50px;top:1440px;width:760px;height:22px;background:rgba(255,255,255,.2);border-radius:11px"></div>
<div id="gb" class="clip" data-start="{QS}" data-duration="{AS-QS}" style="left:50px;top:1440px;width:760px;height:22px;background:#43A047;border-radius:11px;transform-origin:0 50%"></div>
<div id="rb" class="clip" data-start="{QS}" data-duration="{AS-QS}" style="left:50px;top:1440px;width:760px;height:22px;background:#E53935;border-radius:11px;transform-origin:0 50%"></div>'''
    digs=''.join(f'<div id="dg{k}" class="clip dg" data-start="{AS-5+k}" data-duration="1.0" style="left:830px;top:1408px;width:100px;text-align:center;font-size:84px;font-weight:700;color:#E53935">{5-k}</div>' for k in range(5))
    head=f'''<div id="band" class="clip" data-start="0" data-duration="{T}" style="left:0;top:0;width:1080px;height:150px;background:#FF8C00"></div>
<div id="bt" class="clip" data-start="0" data-duration="{T}" style="left:0;top:38px;width:1080px;text-align:center;font-size:72px;font-weight:700;color:#0D1B2A">İSG-PRO.COM</div>
'''
    js=[f"gsap.set('#cov',{{opacity:1}});tl.to('#cov',{{opacity:0,duration:.4}},{QS});",
        "gsap.set(['.cl','.cn','.ck'],{opacity:0});tl.fromTo('.cl',{opacity:0,scale:.6},{opacity:1,scale:1,duration:.5},.1);tl.fromTo('.cn',{opacity:0,y:-80},{opacity:1,y:0,duration:.5},.3);tl.fromTo('.ck',{opacity:0,y:40},{opacity:1,y:0,duration:.5},.7);",
        f"gsap.set(['.tag','.q','.exp'],{{opacity:0}});tl.fromTo('.tag',{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.5}},{QS+.2});tl.fromTo('.q',{{opacity:0,y:40}},{{opacity:1,y:0,duration:.6}},{QS+.5});",
        "gsap.set('.g',{opacity:0});gsap.set('.opt',{opacity:0});"]
    for i in range(len(sec)):
        js.append(f"tl.fromTo('.o{i}',{{opacity:0,x:-120}},{{opacity:1,x:0,duration:.5}},{QS+1.0+i*.35:.2f});")
    js.append(f"gsap.set(['#trk','#gb','#rb'],{{opacity:0}});tl.fromTo('#trk',{{opacity:0}},{{opacity:1,duration:.3}},{QS+.3});tl.fromTo('#gb',{{opacity:1,scaleX:1}},{{opacity:1,scaleX:0,duration:{AS-BS},ease:'none'}},{BS});tl.fromTo('#rb',{{opacity:0,scaleX:1}},{{opacity:1,scaleX:0,duration:{AS-BS},ease:'none'}},{BS});")
    js.append(f"tl.to('#rb',{{opacity:0,duration:.1}},{BS});tl.to('#rb',{{opacity:1,duration:5.0}},{BS+10.0});")
    for i in range(len(sec)):
        if i==dog:
            js.append(f"tl.to('.o{i} .g',{{opacity:1,duration:.4}},{AS+.2});tl.fromTo('.o{i}',{{scale:1}},{{scale:1.04,duration:.25}},{AS+.2});tl.to('.o{i}',{{scale:1,duration:.25}},{AS+.5});tl.to('.o{i}',{{y:window.__dy,duration:.6}},{AS+.9});")
        else:
            js.append(f"tl.to('.o{i}',{{opacity:0,duration:.4}},{AS+.2});")
    js.append(f"tl.fromTo('.exp',{{opacity:0,y:50}},{{opacity:1,y:0,duration:.6}},{AS+1.0});")
    js.append(f"gsap.set(['.cc1','.cc2'],{{opacity:0}});gsap.set('#cls',{{opacity:0}});tl.fromTo('#cls',{{opacity:0}},{{opacity:1,duration:.4}},{CS});tl.fromTo('.cc1',{{opacity:0,y:-60}},{{opacity:1,y:0,duration:.5}},{CS+.2});tl.fromTo('.cc2',{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.5}},{CS+.7});")
    for k in range(5):
        js.append(f"gsap.set('#dg{k}',{{opacity:0}});tl.fromTo('#dg{k}',{{opacity:0,scale:1.8}},{{opacity:1,scale:1,duration:.25}},{AS-5+k:.2f});")
    js.append(f"tl.to('#bt',{{opacity:1,duration:.1}},{T-.1});")
    css='''html,body{margin:0;background:#0D1B2A}#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0D1B2A;font-family:"DejaVu Sans",Arial,sans-serif}
.clip{position:absolute;line-height:1.2}.tag{display:inline-block;padding:12px 28px;background:#162C44;color:#FF8C00;font-size:38px;font-weight:700;border-radius:20px;margin-bottom:24px}
.q{font-size:52px;font-weight:700;color:#fff;margin-bottom:36px;line-height:1.22}
.opt{position:relative;display:flex;align-items:center;min-height:112px;margin-bottom:16px;padding:12px 22px;box-sizing:border-box;background:#162C44;border-radius:24px;font-size:44px;color:#fff;overflow:hidden}
.opt .g{position:absolute;left:0;top:0;width:100%;height:100%;background:#2E7D32}
.lt{position:relative;flex:none;width:60px;height:60px;border-radius:30px;background:#FF8C00;color:#0D1B2A;font-weight:700;text-align:center;line-height:60px;margin-right:20px}
.ot{position:relative;display:block;width:730px;line-height:1.2}
.exp{position:absolute;left:0;width:880px;box-sizing:border-box;padding:24px 30px;background:#162C44;border-left:12px solid #43A047;border-radius:20px;font-size:36px;color:#fff}
.exp b{color:#43A047;font-size:34px}.src{margin-top:12px;font-size:30px;color:#C8D6E5}
.cl{position:absolute;left:340px;top:560px;width:400px;padding:18px 0;background:#C81E1E;border-radius:22px;text-align:center;font-size:64px;font-weight:700;color:#fff}
.cn{position:absolute;left:0;top:760px;width:1080px;text-align:center;font-size:130px;font-weight:700;color:#fff}
.ck{position:absolute;left:0;top:960px;width:1080px;text-align:center;font-size:56px;color:#FF8C00;font-weight:700}
.cc1{position:absolute;left:0;top:640px;width:1080px;text-align:center;font-size:76px;font-weight:700;color:#fff}
.cc2{position:absolute;left:0;top:1000px;width:1080px;text-align:center;font-size:96px;font-weight:700;color:#FF8C00}'''
    fit=FIT%dog
    page=f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css}</style><script src="gsap.min.js"></script></head><body>
<div id="root" data-composition-id="root" data-width="1080" data-height="1920">
{box}{bars}{digs}{cover}{close}{head}</div><script>
const tl=gsap.timeline({{paused:true}});
{fit}
{chr(10).join(js)}
window.__timelines=window.__timelines||{{}};window.__timelines["root"]=tl;
</script></body></html>'''
    os.makedirs(d,exist_ok=True); open(os.path.join(d,"index.html"),"w").write(page)
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)),"gsap.min.js"),d)
    return T,BS,AS
def audio(path,QS,AS,T):
    # tik sesleri (her saniye) + doğru cevap "ding"
    ins=[]; fl=[]
    n=0
    for k in range(5):
        ins+=["-f","lavfi","-t","0.06","-i","sine=frequency=1200:sample_rate=44100"]
        fl.append(f"[{n}:a]volume=2.0,adelay={int((AS-5+k)*1000)}|{int((AS-5+k)*1000)}[a{n}]"); n+=1
    ins+=["-f","lavfi","-t","0.7","-i","sine=frequency=880:sample_rate=44100"]
    fl.append(f"[{n}:a]afade=t=out:st=0.2:d=0.5,volume=2.5,adelay={int((AS+.2)*1000)}|{int((AS+.2)*1000)}[a{n}]"); n+=1
    mix="".join(f"[a{i}]" for i in range(n))
    fl.append(f"{mix}amix=inputs={n}:normalize=0,apad,atrim=0:{T}[out]")
    subprocess.run(["ffmpeg","-v","error","-y",*ins,"-filter_complex",";".join(fl),"-map","[out]","-c:a","aac",path],check=True)
if __name__=="__main__":
    here=os.path.dirname(os.path.abspath(__file__))
    jpath=os.path.abspath(sys.argv[1]); out=os.path.abspath(sys.argv[2])
    os.chdir(here)  # yerel node_modules (hyperframes) burada aranır
    qs=json.load(open(jpath)); os.makedirs(out,exist_ok=True)
    for q in qs:
        no=q.get("no",1); d=os.path.join(out,f"_p{no}")
        T,QS,AS=build(q,d)
        v=os.path.join(out,f"_v{no}.mp4")
        subprocess.run(["npx","hyperframes","render",d,"--fps","30","--quality","standard","-o",v,"--quiet"],check=True)
        a=os.path.join(out,f"_a{no}.m4a"); audio(a,QS,AS,T)
        subprocess.run(["ffmpeg","-v","error","-y","-i",v,"-i",a,"-map","0:v","-map","1:a","-c:v","copy","-c:a","copy","-shortest",os.path.join(out,f"soru_{no}.mp4")],check=True)
        shutil.rmtree(d); os.remove(v); os.remove(a)
        print("bitti", no)
