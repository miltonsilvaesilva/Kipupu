const {chromium}=require('playwright');const path=require('path');
(async()=>{const jobs=JSON.parse(process.argv[2]);const b=await chromium.launch();
for(const [dir,n] of jobs){const p=await b.newPage({viewport:{width:1200,height:1500},deviceScaleFactor:1});
await p.goto('file://'+path.join(dir,'post.html'));await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
for(let i=1;i<=n;i++)await p.locator('#s'+i).screenshot({path:path.join(dir,String(i).padStart(2,'0')+'.png')});await p.close();}
await b.close();})();
