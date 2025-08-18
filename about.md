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

<div id="chat" style="max-width:800px;margin:auto">
  <h3>Ask me anything</h3>
  <div id="log" style="border:1px solid #ddd;height:300px;overflow:auto;padding:10px"></div>
  <input id="q" placeholder="Ask about my work…" style="width:75%">
  <button id="send">Send</button>
</div>

<!-- WebLLM runtime (CDN) -->
<script src="https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm/dist/webllm.min.js"></script>
<script>
(async () => {
  const resp = await fetch('/assets/about.json'); const KB = await resp.json();

  // 1) Maak een korte context van jouw data
  const context = `BIO: ${KB.bio}\nHIGHLIGHTS: ${KB.highlights.join('; ')}\nPROJECTS: ${
    KB.projects.map(p=>p.title+': '+p.desc).join(' | ')
  }`;

  // 2) Start een klein browser-model
  const engine = await webllm.CreateMLCEngine({model:"Qwen2.5-0.5B-Instruct-q4f16_1"}, {});

  const log = document.getElementById('log');
  function add(role, text){ const p=document.createElement('div'); p.textContent=`${role}: ${text}`; log.appendChild(p); log.scrollTop=log.scrollHeight; }

  document.getElementById('send').onclick = async () => {
    const q = document.getElementById('q').value.trim(); if(!q) return;
    add('You', q);
    const sys = `You are a helpful assistant that ONLY answers using the provided profile context.
    If the question is unrelated, say briefly that you only answer about Lars.
    ### PROFILE CONTEXT
    ${context}`;
    const out = await engine.chat.completions.create({
      messages: [{role:'system',content:sys},{role:'user',content:q}],
      temperature: 0.2, max_tokens: 256
    });
    add('Bot', out.choices[0].message.content);
    document.getElementById('q').value = '';
  };
})();
</script>
