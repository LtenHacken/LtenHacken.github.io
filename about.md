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
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm/dist/webllm.min.js"></script>

<script>
(async () => {
  const log = document.getElementById('log');
  const status = document.getElementById('status');
  const add = (role, text) => {
    const div = document.createElement('div');
    div.textContent = `${role}: ${text}`;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
  };

  // 0) Basic checks
  if (!('gpu' in navigator)) {
    add('System', 'WebGPU not available in this browser. Use latest Chrome/Edge on desktop.');
    return;
  }

  // 1) Pad naar JSON corrigeren voor GitHub Pages met baseurl
  const BASE = '{{ site.baseurl }}' || '';
  let KB = {bio:'', highlights:[], projects:[]};
  try {
    const resp = await fetch(`${BASE}/assets/data/about.json`, {cache:'no-store'});
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    KB = await resp.json();
  } catch (e) {
    add('Error', 'Could not load /assets/data/about.json → check pad/bestand.');
    console.error(e);
    return;
  }

  const context = `BIO: ${KB.bio}
HIGHLIGHTS: ${KB.highlights.join('; ')}
PROJECTS: ${KB.projects.map(p=>p.title+': '+p.desc).join(' | ')}`;

  // 2) Start een klein, zeker-bestaand model in WebLLM
  // Tip: deze model-id werkt in de officiële WebLLM builds.
  status.textContent = 'Loading model (Qwen2.5-0.5B-Instruct)… first time can take a minute.';
  let engine;
  try {
    engine = await webllm.CreateMLCEngine(
      { model: "Qwen2.5-0.5B-Instruct-q4f16_1-MLC" }, // ✅ bekende model-id
      { gpuMemoryUtility: 0.9 } // iets vriendelijker met VRAM
    );
  } catch (e) {
    add('Error', 'Model load failed. Check network/HTTPS or try a different browser.');
    console.error(e);
    return;
  }
  status.textContent = 'Model ready.';

  async function ask(q){
    const sys = `You are a helpful assistant that ONLY answers using the provided profile context.
If the question is unrelated, say briefly that you only answer about Lars.
### PROFILE CONTEXT
${context}`;
    try {
      const out = await engine.chat.completions.create({
        messages: [{role:'system',content:sys},{role:'user',content:q}],
        temperature: 0.2, max_tokens: 256
      });
      return out.choices[0].message.content;
    } catch (e) {
      console.error(e);
      return 'Sorry, something went wrong while generating an answer.';
    }
  }

  document.getElementById('send').onclick = async () => {
    const box = document.getElementById('q');
    const q = box.value.trim();
    if(!q) return;
    add('You', q);
    box.value = '';
    status.textContent = 'Thinking…';
    const a = await ask(q);
    status.textContent = '';
    add('Bot', a);
  };
})();
</script>
