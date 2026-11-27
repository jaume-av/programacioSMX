from pathlib import Path
import ast,io,contextlib,json,hashlib,itertools
from unittest.mock import patch
root=Path('/home/jaume/Documentos/programacioSMX/tmp/revisio_exercicis_actualitzacio/RevisioEstructures')
s=root/'solucions_python';p=s/'principals';r=s/'reforc_opcional'
count=0
for f in s.rglob('*.py'):
 tree=ast.parse(f.read_text())
 assert not any(isinstance(n,(ast.FunctionDef,ast.ClassDef,ast.For,ast.While,ast.List,ast.Dict,ast.Set)) for n in ast.walk(tree)),f
 assert '# ' in f.read_text()
def run(file,values):
 global count
 out=io.StringIO()
 with patch('builtins.input',side_effect=[str(v) for v in values]),contextlib.redirect_stdout(out):exec(file.read_text(),{'__name__':'__main__'})
 count+=1
 return out.getvalue()
for x in [-1,0,1]:
 o=run(p/'01_primera_adaptacio.py',[x]);assert o.endswith('Comprovació acabada\n');assert ('El número és positiu' in o)==(x>0)
for age,soc,aut,block in itertools.product([15,16,17,18,25],['si','no'],['si','no'],['si','no']):
 o=run(p/'02_acces_taller.py',[age,soc,aut,block]);allowed=block=='no' and ((age>=18 and soc=='si') or (16<=age<=17 and aut=='si'))
 assert ('Accés al taller autoritzat' in o)==allowed
for x,expect in [(-.01,'Nota no vàlida'),(0,'Suspés'),(4.99,'Suspés'),(5,'Aprovat'),(8.99,'Aprovat'),(9,'Excel·lent'),(10,'Excel·lent'),(10.01,'Nota no vàlida')]:assert run(p/'03_qualificacio_valida.py',[x]).strip()==expect
for values in itertools.product([-8,-1,0,5],repeat=3):
 out=run(p/'04_major_de_tres.py',values);assert float(out.split('és ')[1])==max(values)
for op,result in [(1,10),(2,6),(3,16),(4,4)]:assert f'Resultat: {float(result)}' in run(p/'05_calculadora.py',[8,2,op])
for values,msg in [([8,0,4],'No es pot dividir entre zero'),([8,2,5],'Opció no vàlida')]:assert run(p/'05_calculadora.py',values).strip().endswith(msg) and 'Resultat:' not in run(p/'05_calculadora.py',values)
for filename,expected in [('06_transport_public.py','0.75'),('06b_transport_prioritat_gratuitat.py','0.00')]:
 assert f'Preu final: {expected} €' in run(p/filename,['urbà',10,'no','si'])
 assert run(p/filename,['altre',10,'no','si']).strip()=='Trajecte no vàlid'
 for vals,total in [(['urbà',12,'si','no'],'1.05'),(['interurbà',25,'si','no'],'2.10'),(['interurbà',26,'si','no'],'3.00'),(['urbà',65,'no','no'],'0.90')]:assert f'Preu final: {total} €' in run(p/filename,vals)
for c,power,social,noct,expected in [(0,3,'no','no','12.00'),(100,3,'no','no','27.00'),(100.5,3,'no','no','32.10'),(200,3,'si','si','37.05'),(200.5,3,'si','si','39.08'),(250,3,'no','no','62.00'),(250.5,3,'no','no','74.62')]:assert f'Total final: {expected} €' in run(p/'07_factura_llum.py',[c,power,social,noct])
for c,power in [(-1,3),(100,0),(100,-1)]:assert run(p/'07_factura_llum.py',[c,power,'si','si']).strip()=='Dades no vàlides'
# Room: validation takes precedence; both rejections and compatible complements.
valid=[4,20,'si','si','si','si','si']
assert 'Total final: 55.00 €' in run(p/'08_reserva_sala.py',valid)
for pos in range(2,7):
 vals=valid.copy();vals[pos]='potser';assert run(p/'08_reserva_sala.py',vals).strip()=='Dades no vàlides'
for pos,wrong in [(0,0),(0,9),(1,0),(1,31)]:
 vals=valid.copy();vals[pos]=wrong;assert run(p/'08_reserva_sala.py',vals).strip()=='Dades no vàlides'
for adult,available,msg in [('no','no','Sala no disponible'),('si','no','Sala no disponible'),('no','si','Cal una persona responsable major d’edat')]:
 vals=valid.copy();vals[2]=adult;vals[4]=available
 assert run(p/'08_reserva_sala.py',vals).strip().replace("d'edat",'d’edat')==msg
for vals,total in [([1,1,'si','no','si','no','no'],'12.00'),([3,30,'si','si','si','si','no'],'36.80'),([8,30,'si','no','si','no','si'],'95.00')]:assert f'Total final: {total} €' in run(p/'08_reserva_sala.py',vals)
# At least one passing and one contrasting case for every optional program.
cases={
'if_02_igual_a_deu.py':[(10,'El número és 10'),(9,'')],
'if_03_adolescent.py':[(12,'Ets adolescent'),(18,'')],
'if_04_vip_o_soci.py':[(['no','si'],'Accés especial concedit'),(['no','no'],'')],
'if_05_no_repetidor.py':[('no','Pot passar de curs'),('si','')],
'if_06_condicio_combinada.py':[([17,'si','no'],'Pot entrar'),([17,'no','si'],'')],
'guiat_01_major_edat.py':[(18,"Ets major d'edat"),(17,"Ets menor d'edat")],
'guiat_02_zero.py':[(0,'El número és zero'),(-1,'El número no és zero')],
'guiat_03_notes.py':[(9,'Excel·lent'),(5,'Aprovat'),(4.99,'Suspés')],
'guiat_04_classificacio_edat.py':[(17,"Menor d'edat"),(18,'Adult'),(65,'Jubilat')],
'guiat_05_condicional_anidat.py':[([17,'si'],'Accés denegat'),([18,'si'],'Entrada amb descompte'),([18,'no'],'Entrada normal')],
'guiat_06_alternatives_edat.py':[(64,'Adult'),(65,'Jubilat')],
'autonom_01_parell_imparell.py':[(-2,'Parell'),(0,'Parell'),(3,'Imparell')],
'autonom_03_descompte.py':[(99,'Preu final: 99.00 €'),(100,'Preu final: 90.00 €'),(200,'Preu final: 180.00 €'),(201,'Preu final: 160.80 €')],
'autonom_04_nota_valida.py':[(0,'Nota correcta'),(10,'Nota correcta'),(10.1,'Nota incorrecta')],
'autonom_06_acces_sistema.py':[([17,'si'],'Accés denegat'),([18,'no'],'Accés normal'),([18,'si'],'Accés premium')],
'autonom_07_temperatura.py':[(-.1,'Gel'),(0,'Fred'),(15,'Fred'),(15.5,'Temperatura suau'),(25,'Temperatura suau'),(25.1,'Calor')]
}
for filename,tests in cases.items():
 for vals,msg in tests:assert run(r/filename,vals if isinstance(vals,list) else [vals]).strip()==msg
# Preserve all original source files and all theory pages of the revision.
src=Path('/home/jaume/Escritorio/RevisioEstructures/2.2.-Estructures')
changed=['2.2.2.1-Exercicis IF.md','2.2.3.1 -Exercicis IF-ELSE.md']
for f in src.glob('*.md'):
 if f.name not in changed:assert f.read_bytes()==(root/'2.2.-Estructures'/f.name).read_bytes()
manifest=json.loads((root/'originals_sha256.json').read_text())
original=Path('/home/jaume/Documentos/programacioSMX/apunts/2.-Python/2.2.-Estructures')
for name,sha in manifest.items():assert hashlib.sha256((original/name).read_bytes()).hexdigest()==sha
p=root/'comprovacio.json';data=json.loads(p.read_text());data['actualitzacio_exercicis']={'activitats_principals':8,'fitxers_principals_amb_variant':9,'reforc_opcional':16,'fitxers_python':25,'execucions_correctes':count,'teoria_sense_canvis':True,'originals_intactes':True};p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Correcte:',count,'execucions, 25 programes independents, teoria i originals intactes.')
