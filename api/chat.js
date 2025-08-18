// api/chat.js  (Vercel serverless function)
export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Use POST" });

  try {
    const { question, profileContext } = req.body || {};
    if (!question) return res.status(400).json({ error: "Missing question" });

    // --- Construct a simple instruction prompt (works across many instruct models)
    const system = `You are an assistant that ONLY answers questions about Lars using the PROFILE CONTEXT.
- Do not quote the context verbatim; answer in your own words.
- If the question is unrelated to Lars, say so briefly.
- Keep answers short: max 3 sentences.

PROFILE CONTEXT:
${profileContext || ""}`;

    const prompt = `${system}\n\nUser: ${question}\nAssistant:`;

    // --- Choose a free, strong multilingual instruct model
    // Tip: start with a lighter one for quota/speed; you can switch to Qwen2.5-7B-Instruct later.
    const MODEL = process.env.HF_MODEL_ID || "Qwen/Qwen2.5-3B-Instruct";

    const r = await fetch(`https://api-inference.huggingface.co/models/${MODEL}`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.HUGGINGFACE_API_TOKEN}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        inputs: prompt,
        parameters: {
          max_new_tokens: 220,
          temperature: 0.2,
          return_full_text: false,
          repetition_penalty: 1.05
        }
      })
    });

    if (!r.ok) {
      const txt = await r.text();
      return res.status(r.status).json({ error: `HF error: ${txt}` });
    }
    const data = await r.json();
    // HF Inference API returns an array of { generated_text }
    const answer = Array.isArray(data) ? data[0]?.generated_text : data?.generated_text || "";

    res.status(200).json({ answer: (answer || "").trim() });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
}
