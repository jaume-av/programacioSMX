const fs=require('fs'),path=require('path');
const {chromium}=require('/home/jaume/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const root='/home/jaume/Documentos/programacioSMX/tmp/revisio_exercicis_actualitzacio/RevisioEstructures/_site';
 const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});const missing=[];
 await page.route('http://revisio.local/**',async route=>{
 let rel=decodeURIComponent(new URL(route.request().url()).pathname);if(rel.endsWith('/'))rel+='index.html';const file=path.join(root,rel);
 if(!fs.existsSync(file)){missing.push(rel);return route.fulfill({status:404,body:'Not found'});}
 const type={'.html':'text/html;charset=utf-8','.css':'text/css','.js':'text/javascript','.json':'application/json'}[path.extname(file)]||'application/octet-stream';
 await route.fulfill({status:200,contentType:type,body:fs.readFileSync(file)});
 });
 for(const [name,count,banks]of [['2.2.2.1-Exercicis IF.html',2,5],['2.2.3.1 -Exercicis IF-ELSE.html',6,11]]){
 await page.goto('http://revisio.local/2.2.-Estructures/'+encodeURIComponent(name));
 const titles=await page.locator('main h2').allTextContents();if(titles.filter(t=>t.trim().startsWith('Activitat ')).length!==count)throw Error('Activities');
 if(await page.locator('details h3').count()!==banks)throw Error('Optional banks not rendered');
 await page.locator('details summary').first().click();if(!await page.locator('details[open]').count())throw Error('Disclosure');
 console.log(name+': activitats i reforços correctes');
 }
 const downloads=fs.readdirSync(path.join(root,'solucions_python/principals')).filter(f=>f.endsWith('.py'));
 if(downloads.length!==9)throw Error('Missing Python files');
 if(missing.length)throw Error(missing.join(','));
 await browser.close();console.log('Correcte: vista Just the Docs i fitxers Python disponibles.');
})().catch(e=>{console.error(e);process.exit(1)});
