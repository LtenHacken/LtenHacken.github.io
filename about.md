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

<!-- === SIMPLE WEBLLM CHAT (WORKING MINIMAL) === -->
<div id="llm-chat" style="max-width:900px;margin:auto">
  <h3>Ask about me</h3>
  <div id="llm-log" style="border:1px solid #ddd;height:320px;overflow:auto;padding:10px;font-family:monospace;white-space:pre-wrap"></div>
  <div style="margin-top:8px;display:flex;gap:8px">
    <input id="llm-q" placeholder="Ask about my research, projects, skills…" style="flex:1">
    <button id="llm-send">Send</button>
  </div>
  <div id="llm-status" style="margin-top:6px;color:#666"></div>
</div>

<script type="module">
  import { CreateMLCEngine, prebuiltAppConfig } from "https://esm.run/@mlc-ai/web-llm@0.2.79";

  // --- Simple DOM helpers ---
  const logEl = document.getElementById("llm-log");
  const statusEl = document.getElementById("llm-status");
  const qEl = document.getElementById("llm-q");
  const sendBtn = document.getElementById("llm-send");
  const add = (who, text) => {
    const d = document.createElement("div");
    d.textContent = `${who}: ${text}`;
    logEl.appendChild(d);
    logEl.scrollTop = logEl.scrollHeight;
  };

  // --- Basic checks ---
  if (!("gpu" in navigator)) {
    add("Error", "WebGPU not available. Use latest Chrome/Edge via HTTPS.");
    throw new Error("No WebGPU");
  }

  // --- Pick a valid small instruct model automatically from SDK list ---
  // Prefer smallest VRAM "Instruct" model; fallback to the first in list.
  const models = prebuiltAppConfig.model_list || [];
  const instruct = models.filter(m => /Instruct/.test(m.model_id))
                         .sort((a,b) => (a.vram_required_mb||1e9) - (b.vram_required_mb||1e9));
  const MODEL_ID = (instruct[0]?.model_id) || (models[0]?.model_id);
  if (!MODEL_ID) {
    add("Error", "No prebuilt models available in this WebLLM version.");
    throw new Error("No models in prebuiltAppConfig");
  }

  // --- Progress callback (shows exactly what is loading) ---
  const initProgressCallback = (p) => {
    statusEl.textContent = p.text + (p.url ? " :: " + p.url : "");
    // console.log(p); // uncomment to see detailed steps in console
  };

  // --- Init engine (IMPORTANT: pass model as STRING per current API) ---
  let engine;
  try {
    statusEl.textContent = `Loading model: ${MODEL_ID} … (first time may take a minute)`;
    engine = await CreateMLCEngine(
      MODEL_ID,
      { initProgressCallback, wasmNumThreads: 1, gpuMemoryUtility: 0.9 }
    );
    statusEl.textContent = `Model ready: ${MODEL_ID}`;
  } catch (e) {
    console.error("Model load failed", e);
    statusEl.textContent = "Model load failed. See console.";
    add("Error", "Model load failed. Try refreshing or another Chromium browser.");
    throw e;
  }

  // --- Ask helper ---
  async function ask(q) {
    const out = await engine.chat.completions.create({
      messages: [
        { role: "system", content: "Answer concisely about Lars and his work." },
        { role: "user", content: q }
      ],
      temperature: 0.2,
      max_tokens: 256
    });
    return out.choices[0].message.content;
  }

  // --- Wire up UI ---
  async function handleSend() {
    const q = qEl.value.trim();
    if (!q) return;
    add("You", q);
    qEl.value = "";
    statusEl.textContent = "Thinking…";
    try {
      const a = await ask(q);
      add("Bot", a);
    } catch (e) {
      console.error(e);
      add("Error", "Generation error.");
    } finally {
      statusEl.textContent = "";
    }
  }
  sendBtn.addEventListener("click", handleSend);
  qEl.addEventListener("keydown", (ev) => {
    if (ev.key === "Enter") handleSend();
  });

  // Optional: initial hello
  add("System", `Loaded ${MODEL_ID}. Ask me something!`);
</script>
