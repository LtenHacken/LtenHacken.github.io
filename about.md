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



<div id="chat" style="max-width:900px;margin:auto">
  <h3>Ask about me</h3>
  <div id="log" style="border:1px solid #ddd;height:320px;overflow:auto;padding:10px;font-family:monospace;white-space:pre-wrap"></div>
  <div style="margin-top:8px;display:flex;gap:8px">
    <input id="q" placeholder="Ask about my research, projects, skills…" style="flex:1">
    <button id="send">Send</button>
  </div>
  <div id="status" style="margin-top:6px;color:#666"></div>
</div>

<!-- Import WebLLM via CDN (volgens docs: Using CDN) -->
<script type="module">
  import { CreateMLCEngine } from "https://esm.run/@mlc-ai/web-llm";

  const log = document.getElementById('log');
  const status = document.getElementById('status');
  const add = (r,t)=>{const d=document.createElement('div');d.textContent=`${r}: ${t}`;log.appendChild(d);log.scrollTop=log.scrollHeight;};

  // 0) Checks
  if (!('gpu' in navigator)) {
    add('Error','WebGPU not available. Use latest Chrome/Edge via HTTPS.');
    throw new Error('No WebGPU');
  }

  // 1) Laad jouw profieldata (let op baseurl in GitHub Pages)
  const BASE = "{{ site.baseurl }}" || "";
  let KB = {bio:'', highlights:[], projects:[]};
  try {
    const resp = await fetch(`${BASE}/assets/about.json`, { cache: 'no-store' });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    KB = await resp.json();
  } catch (e) {
    add('Error','/assets/about.json niet gevonden'); console.error(e);
    throw e;
  }

  const context = `BIO: ${KB.bio}
HIGHLIGHTS: ${KB.highlights.join('; ')}
PROJECTS: ${KB.projects.map(p=>p.title+': '+p.desc).join(' | ')}`;

  // 2) Start een klein model (MLC model-id) — kies 1 van deze
  const modelId = "Llama-3.2-1B-Instruct-q4f16_1-MLC";
  status.textContent = `Loading model: ${modelId} … (first time can take a minute)`;

  let engine;
  try {
    engine = await CreateMLCEngine({ model: modelId }, { gpuMemoryUtility: 0.9, wasmNumThreads: 1 });
    status.textContent = `Model ready: ${modelId}`;
  } catch (e) {
    console.error(e);
    status.textContent = "Model load failed.";
    add('Error','Model load failed.');
    throw e;
  }

  async function ask(q) {
    const sys = `You ONLY answer about Lars using this profile context. If unrelated, say you only answer about Lars.
### PROFILE CONTEXT
${context}`;
    const out = await engine.chat.completions.create({
      messages: [{ role:'system', content: sys }, { role:'user', content: q }],
      temperature: 0.2, max_tokens: 256
    });
    return out.choices[0].message.content;
  }

  document.getElementById('send').onclick = async () => {
    const box = document.getElementById('q');
    const q = box.value.trim(); if (!q) return;
    add('You', q); box.value = '';
    status.textContent = 'Thinking…';
    try {
      const a = await ask(q);
      add('Bot', a);
    } catch (e) {
      add('Error', 'Generation error.');
      console.error(e);
    } finally {
      status.textContent = '';
    }
  };
</script>
