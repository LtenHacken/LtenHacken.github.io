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
  import { CreateMLCEngine, prebuiltAppConfig } from "https://esm.run/@mlc-ai/web-llm@0.2.79";

  // 1) Laat zien welke modellen deze versie kent (100% juiste IDs)
  console.table(prebuiltAppConfig.model_list.map(m => ({
    id: m.model_id, // ← dit is de modelID die je moet gebruiken
    sizeMB: m.vram_required_mb
  })));

  // Kies een kleine die zeker bestaat, bv. Llama 3.2 1B of Phi 1.1
  // (of pak er programmatic eentje uit de lijst)
  const MODEL_ID = "Llama-3.2-1B-Instruct-q4f16_1-MLC";

  // 2) Progress tonen (zodat je ziet wát eventueel faalt)
  const statusEl = document.getElementById("status");
  const initProgressCallback = (p) => {
    if (statusEl) statusEl.textContent = p.text + (p.url ? " :: " + p.url : "");
    console.log(p);
  };

  // 3) **Juiste** API-call volgens docs: model **als string** meegeven
  let engine;
  try {
    engine = await CreateMLCEngine(
      MODEL_ID,                                 // ← string, geen object!
      { initProgressCallback, wasmNumThreads: 1, gpuMemoryUtility: 0.9 }
    );
    if (statusEl) statusEl.textContent = `Model ready: ${MODEL_ID}`;
  } catch (e) {
    console.error("Model load failed", e);
    if (statusEl) statusEl.textContent = "Model load failed.";
    // Tip: kies hier automatisch een andere uit prebuiltAppConfig.model_list
    return;
  }

  // 4) Kleine rooktest (werkt zonder jouw about.json)
  const out = await engine.chat.completions.create({
    messages: [
      { role: "system", content: "You answer in one short sentence." },
      { role: "user", content: "Say hi." }
    ],
    temperature: 0.2, max_tokens: 32
  });
  console.log(out.choices[0].message.content);
</script>
