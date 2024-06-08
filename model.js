const { OpenAI } = require("openai");

const openai = new OpenAI({
  apiKey: "your_api_key_here",
  baseURL: "https://api.aimlapi.com",
});

(async () => {
  const chatCompletion = await openai.chat.completions.create({
    model: "mistralai/Mistral-7B-Instruct-v0.2",
    messages: [
      { role: "system", content: "You are a travel agent. Be descriptive and helpful" },
      { role: "user", content: "Tell me about San Francisco" }
    ],
    temperature: 0.7,
    max_tokens: 128,
  });
  console.log("AI/ML API:\n", chatCompletion.choices[0].message.content);
})();