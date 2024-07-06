const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: "1149fab84aab45c9a10165cc5145b5c2",
  basePath: "https://api.aimlapi.com/",
});
const openai = new OpenAIApi(configuration);

async function run() {
  const response = await openai.createCompletion({
    model: "mistralai/Mistral-7B-Instruct-v0.2",
    prompt: "Tell me a joke",
    max_tokens: 50,
  });
  console.log(response.data.choices[0].text);
}

run();
