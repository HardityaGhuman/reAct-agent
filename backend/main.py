from app.client import client, MODEL

res = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
    reasoning_effort="low",
)
print(res.choices[0].message.content)
print(res.usage)
