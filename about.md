---
layout: default
title: About
---

# About Me

![Profile picture](assets/images/profile.jpeg){:style="width:200px;border-radius:50%;"}

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

<!-- 
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

  // --- DOM helpers ---
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

  if (!("gpu" in navigator)) {
    add("Error", "WebGPU not available. Use latest Chrome/Edge via HTTPS.");
    throw new Error("No WebGPU");
  }

  // --- Load profile context from JSON ---
  const BASE = "{{ site.baseurl }}" || "";
  let PROFILE = { bio: "", highlights: [], projects: [] };
  try {
    const resp = await fetch(`${BASE}/assets/about.json`, { cache: "no-store" });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    PROFILE = await resp.json();
  } catch (e) {
    add("Error", "Could not load /assets/about.json");
    console.error(e);
  }

  const PROFILE_CONTEXT = `BIO: ${PROFILE.bio}
HIGHLIGHTS: ${PROFILE.highlights?.join("; ")}
PROJECTS: ${(PROFILE.projects||[]).map(p => `${p.title}: ${p.desc}`).join(" | ")}`;

  // --- Pick a small instruct model ---
  const models = prebuiltAppConfig.model_list || [];
  const instruct = models.filter(m => /Instruct/.test(m.model_id))
                         .sort((a,b) => (a.vram_required_mb||1e9) - (b.vram_required_mb||1e9));
  //const MODEL_ID = (instruct[0]?.model_id) || (models[0]?.model_id);
  const MODEL_ID = "Qwen2.5-7B-Instruct-q4f32_1-MLC";
  if (!MODEL_ID) {
    add("Error", "No prebuilt models available.");
    throw new Error("No models");
  }

  const initProgressCallback = (p) => {
    statusEl.textContent = p.text + (p.url ? " :: " + p.url : "");
  };

  let engine;
  try {
    statusEl.textContent = `Loading model: ${MODEL_ID} …`;
    engine = await CreateMLCEngine(MODEL_ID, { initProgressCallback, wasmNumThreads: 1, gpuMemoryUtility: 0.9 });
    statusEl.textContent = `Model ready: ${MODEL_ID}`;
  } catch (e) {
    console.error("Model load failed", e);
    add("Error", "Model load failed.");
    throw e;
  }

  // --- Ask helper with context ---
    async function ask(q) {
    const sys =
    `You are an assistant that answers questions about Lars using the PROFILE CONTEXT.
    - Do NOT quote or reproduce the PROFILE CONTEXT verbatim.
    - Summarize relevant facts from the context in your own words.
    - If a question is unrelated to Lars, say briefly that you only answer questions about Lars.
    - Do not answer politics or religion related questions.
    - Do not fabricate Lars his opinions or beliefs.
    - Keep answers brief with a maximum of three sentences.

    ### EXAMPLES
    Prompt: What programming languages does Lars use?
    Response: Python, MATLAB, C and LaTeX feature most in his work.

    ### PROFILE CONTEXT (DO NOT SHOW THIS IN OUTPUT)
    ${PROFILE_CONTEXT}`;

    const out = await engine.chat.completions.create({
        messages: [
        { role: "system", content: sys },
        { role: "user",   content: q  }
        ],
        temperature: 0.2,
        max_tokens: 192,
        // Optional stop to prevent echoing the section header
        stop: ["### PROFILE CONTEXT"]
    });
    return out.choices[0].message.content.trim();
    }

  // --- UI wiring ---
  async function handleSend() {
    const q = qEl.value.trim();
    if (!q) return;
    add("You", q);
    qEl.value = "";
    statusEl.textContent = "Thinking…";
    try {
      add("Bot", await ask(q));
    } catch (e) {
      console.error(e);
      add("Error", "Generation error.");
    } finally {
      statusEl.textContent = "";
    }
  }
  sendBtn.addEventListener("click", handleSend);
  qEl.addEventListener("keydown", ev => { if (ev.key === "Enter") handleSend(); });

  add("System", `Loaded ${MODEL_ID} with context. Ask me something!`);
</script> -->
