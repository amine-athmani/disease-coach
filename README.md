# Disease Coach

A chat assistant for people living with a chronic disease (diabetes, asthma or heart disease). The user fills in a short profile (age, height, weight, sex, activity level, diet, preferred cuisine, allergies), then asks questions. The profile goes into the system prompt, so answers take the user's diet and allergies into account.

Built in August 2024 as a follow-up to DAIT, our LEAP 2024 hackathon assistant that plans meals and exercise for diabetics. The model is Falcon 180B chat, called through the AI71 API with the OpenAI Python client.

The assistant gives general information only. It is not medical advice and it tells users to see a doctor for diagnosis, medication or urgent symptoms.

## What is in the repo

- `app.py`: Streamlit app with the profile form and the chat.
- `telegram/server.py`: the same assistant as a Telegram bot, set up for Type 1 diabetes.
- `falcon_test.py`: a minimal call to the API, plain and streaming.

## Run it

Python 3.9 or later.

```bash
git clone https://github.com/amine-athmani/disease-coach.git
cd disease-coach
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Streamlit app: put your key in `.streamlit/secrets.toml`, then start it.

```toml
AI71_API_KEY = "your-key"
# Optional: any OpenAI-compatible endpoint and model
# AI71_BASE_URL = "https://api.ai71.ai/v1/"
# MODEL = "tiiuae/falcon-180b-chat"
```

```bash
streamlit run app.py
```

Telegram bot: put `AI71_API_KEY` and `TELEGRAM_TOKEN` in a `.env` file (optionally `AI71_BASE_URL` and `MODEL`), then run `python telegram/server.py`.

Both entry points read the base URL and model name from configuration, so you can point them at another OpenAI-compatible provider if the AI71 endpoint is not available to you.

## License

MIT
