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



<!-- Laad WebLLM als ES module vanaf jsDelivr en zet 'm op window.webllm -->
<script type="module">
  import * as webllm from "https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.79/lib/index.js";
  window.webllm = webllm;
  console.log("WebLLM loaded (module):", !!window.webllm);
</script>


<script>
(async () => {
  const log = document.getElementById('log');
  const status = document.getElementById('status');
  const add = (r,t)=>{const d=document.createElement('div');d.textContent=`${r}: ${t}`;log.appendChild(d);log.scrollTop=log.scrollHeight;};

  if (!window.webllm) { add('Error','WebLLM script not loaded.'); return; }
  if (!('gpu' in navigator)) { add('Error','WebGPU not available. Use Chrome/Edge via HTTPS.'); return; }

  // Baseurl-veilig pad voor GitHub Pages
  const BASE = '{{ site.baseurl }}' || '';
  let KB = {bio:'', highlights:[], projects:[]};
  try {
    const resp = await fetch(`${BASE}/assets/about.json`, {cache:'no-store'});
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    KB = await resp.json();
  } catch (e) { add('Error','/assets/about.json niet gevonden.'); console.error(e); return; }

  const context = `BIO: ${KB.bio}
HIGHLIGHTS: ${KB.highlights.join('; ')}
PROJECTS: ${KB.projects.map(p=>p.title+': '+p.desc).join(' | ')}`;

  // Probeer lichte, bekende model-ID's die in WebLLM beschikbaar zijn
  // (Qwen2.5 0.5B bestaat in MLC-formaat; zie lijst/discussies) 
  const candidates = [
    "Qwen2.5-0.5B-Instruct-q4f16_1-MLC",
    "Qwen2-0.5B-Instruct-q4f16_1-MLC",
    "Phi-1.1-q4f16_1-MLC"
  ];

  let engine = null, lastErr = null;
  for (const m of candidates) {
    try {
      status.textContent = `Loading model: ${m} …`;
      engine = await webllm.CreateMLCEngine({ model: m }, { gpuMemoryUtility: 0.9, wasmNumThreads: 1 });
      status.textContent = `Model ready: ${m}`;
      break;
    } catch (e) {
      console.warn('Model failed', m, e);
      lastErr = e;
    }
  }
  if (!engine) { add('Error','Model load failed for all candidates. Check console.'); console.error(lastErr); return; }

  async function ask(q){
    const sys = `You ONLY answer about Lars using this profile context. If unrelated, say you only answer about Lars.
### PROFILE CONTEXT
${context}`;
    try {
      const out = await engine.chat.completions.create({
        messages:[{role:'system',content:sys},{role:'user',content:q}],
        temperature:0.2, max_tokens:256
      });
      return out.choices[0].message.content;
    } catch (e) { console.error(e); return 'Generation error.'; }
  }

  document.getElementById('send').onclick = async () => {
    const box = document.getElementById('q');
    const q = box.value.trim(); if(!q) return;
    add('You', q); box.value = '';
    status.textContent = 'Thinking…';
    const a = await ask(q);
    status.textContent = '';
    add('Bot', a);
  };
})();
</script>
