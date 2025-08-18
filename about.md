---
layout: default
title: About
---

# About Me

![Profile picture](assets/images/profile.jpg){:style="width:200px;border-radius:50%;"}

On this page my education and experiences are further elaborated. My CV is attached at the bottom of this page.


I enjoy working at the intersection of **theory**, **simulation**, and **real-world applications**.  
Some things about me:

- 🎓 MSc Applied Physics – TU Eindhoven
- 🌊 Research on **ocean wave prediction** (Kalman filtering, HOS methods)
- 🧑‍💻 Strong in **Python**, **MATLAB**, **C**, and **LaTeX**
- 🌏 Research visits: **UC Berkeley** and planned **Tsinghua University**

In my free time, I enjoy hiking, sailing, and Japanese language learning.

  
[📄 Download PDF](assets/Lars_ten_Hacken_CV.pdf)

<div id="chat" style="max-width:900px;margin:auto">
  <h3>Ask me anything</h3>
  <div id="log" style="border:1px solid #ddd;height:320px;overflow:auto;padding:10px;font-family:monospace;white-space:pre-wrap"></div>
  <div style="margin-top:8px;display:flex;gap:8px">
    <input id="q" placeholder="Ask about my research, projects, skills…" style="flex:1">
    <button id="send">Send</button>
  </div>
  <div id="status" style="margin-top:6px;color:#666"></div>
</div>

<!-- WebLLM runtime (global 'webllm') -->
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.74/dist/webllm.min.js"></script>

<script>
(async () => {
  const log = document.getElementById('log');
  const status = document.getElementById('status');
  const add = (r,t)=>{const d=document.createElement('div');d.textContent=`${r}: ${t}`;log.appendChild(d);log.scrollTop=log.scrollHeight;};

  if(!('gpu' in navigator)){ add('Error','WebGPU not available—probeer Chrome/Edge desktop via HTTPS.'); return; }

  // 1) Knowledge laden (laat zoals je had)
  const BASE='{{ site.baseurl }}'||'';
  let KB={bio:'',highlights:[],projects:[]};
  try{
    const resp=await fetch(`${BASE}/assets/about.json`,{cache:'no-store'});
    if(!resp.ok) throw new Error(`HTTP ${resp.status}`);
    KB=await resp.json();
  }catch(e){ add('Error','/assets/about.json niet gevonden.'); console.error(e); return; }

  const context=`BIO: ${KB.bio}
HIGHLIGHTS: ${KB.highlights.join('; ')}
PROJECTS: ${KB.projects.map(p=>p.title+': '+p.desc).join(' | ')}`;

  // 2) Probeer meerdere bekende, lichte modellen
  const candidates = [
    "Llama-3.2-1B-Instruct-q4f16_1-MLC",
    "Qwen2.5-0.5B-Instruct-q4f16_1-MLC",
    "Phi-1.1-q4f16_1-MLC"
  ];

  let engine=null, lastErr=null;
  for (const m of candidates){
    try{
      status.textContent = `Loading model: ${m} …`;
      engine = await webllm.CreateMLCEngine(
        { model: m },
        { gpuMemoryUtility: 0.9, wasmNumThreads: 1 } // 1 thread is veiliger op GitHub Pages
      );
      status.textContent = `Model ready: ${m}`;
      break;
    }catch(e){
      console.warn('Model failed', m, e);
      lastErr = e;
    }
  }
  if(!engine){ add('Error','Model load failed for all candidates. Zie console (F12) voor details.'); console.error(lastErr); return; }

  async function ask(q){
    const sys=`You ONLY answer about Lars using this profile context. If unrelated, say you only answer about Lars.\n### PROFILE CONTEXT\n${context}`;
    try{
      const out = await engine.chat.completions.create({
        messages:[{role:'system',content:sys},{role:'user',content:q}],
        temperature:0.2, max_tokens:256
      });
      return out.choices[0].message.content;
    }catch(e){ console.error(e); return 'Generation error.'; }
  }

  document.getElementById('send').onclick = async ()=>{
    const box=document.getElementById('q'); const q=box.value.trim(); if(!q) return;
    add('You', q); box.value=''; status.textContent='Thinking…';
    const a = await ask(q); status.textContent=''; add('Bot', a);
  };
})();
</script>
