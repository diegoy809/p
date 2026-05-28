import requests,json,time,os,re
import sys
API=sys.argv[1] if len(sys.argv)>1 else ""
SAVE=os.path.expanduser("~/zh.json")
print("下载题库...")
r=requests.get("https://diegoy809.github.io/p/index.html",timeout=30)
txt=r.text;start=txt.find('const Q=')+8;depth=0;end=start
for i,c in enumerate(txt[start:],start):
 if c=='[':depth+=1
 elif c==']':
  depth-=1
  if depth==0:end=i+1;break
Q=json.loads(txt[start:end])
print(f"题库:{len(Q)}题")
def gk(q):return str(q.get("block",""))+"_"+str(len(q["question"]))
try:
 with open(SAVE) as f:zh=json.load(f)
except:zh={}
def save():
 with open(SAVE,"w") as f:json.dump(zh,f,ensure_ascii=False)
def tr(texts):
 p="将以下"+str(len(texts))+"道意大利驾照题翻译成简洁中文,每行一个用序号如'1. 译文',不要解释:\n\n"+"\n".join(f"{i+1}. {t}" for i,t in enumerate(texts))
 r=requests.post("https://api.anthropic.com/v1/messages",headers={"Content-Type":"application/json","x-api-key":API,"anthropic-version":"2023-06-01"},json={"model":"claude-haiku-4-5-20251001","max_tokens":4000,"messages":[{"role":"user","content":p}]},timeout=60)
 r.raise_for_status()
 t=r.json()["content"][0]["text"].strip();out=[]
 for line in t.split("\n"):
  line=line.strip()
  if not line:continue
  m=re.match(r"^\d+[.)、]\s*",line)
  if m:out.append(line[m.end():].strip())
 return out
todo=[q for q in Q if gk(q) not in zh]
print(f"已翻译:{len(zh)} 剩余:{len(todo)}")
B=40
for i in range(0,len(todo),B):
 batch=todo[i:i+B];bn=i//B+1;bt=(len(todo)+B-1)//B
 try:
  res=tr([q["question"] for q in batch])
  for j,q in enumerate(batch):zh[gk(q)]=res[j] if j<len(res) else q["question"]
  save();print(f"批{bn}/{bt} {(i+len(batch))/len(todo)*100:.0f}% {len(zh)}/{len(Q)}")
 except Exception as e:
  print(f"批{bn}失败:{e}")
  for q in batch:
   if gk(q) not in zh:zh[gk(q)]=q["question"]
  time.sleep(10 if "429" in str(e) else 2)
print(f"\n翻译完成{len(zh)}题,生成HTML...")
base=requests.get("https://diegoy809.github.io/p/index.html").text
enriched=[{**q,"zh":zh.get(gk(q),q["question"])} for q in Q]
ds=json.dumps(enriched,ensure_ascii=False,separators=(",",":"))
s=base.find('const Q=')+8;d=0;e=s
for i,c in enumerate(base[s:],s):
 if c=='[':d+=1
 elif c==']':
  d-=1
  if d==0:e=i+1;break
out=os.path.expanduser("~/index.html")
with open(out,"w",encoding="utf-8") as f:f.write(base[:s]+ds+base[e:])
print(f"✅完成! 文件在:{out}")
