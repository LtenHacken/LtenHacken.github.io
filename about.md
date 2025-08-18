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
  const MODEL_ID = (instruct[0]?.model_id) || (models[0]?.model_id);
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
    const sys = `You are a helpful assistant that ONLY answers about Lars using the PROFILE CONTEXT.
If the question is unrelated, briefly say you only answer about Lars.
### PROFILE CONTEXT
${PROFILE_CONTEXT}`;
    const out = await engine.chat.completions.create({
      messages: [
        { role: "system", content: sys },
        { role: "user", content: q }
      ],
      temperature: 0.2,
      max_tokens: 256
    });
    return out.choices[0].message.content;
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
</script>
