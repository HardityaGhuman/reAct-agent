from app.client import client, MODEL
from app.structure import INSTRUCTIONS

for question in ["How many PTO days do I have as an employee at X?", "What is the weather like in Berlin?"]:
    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": INSTRUCTIONS}, {"role": "user", "content": question}],
        reasoning_effort="medium",
    )
    print(f"Q: {question}\nA: {res.choices[0].message.content}\n[tokens in={res.usage.prompt_tokens} out={res.usage.completion_tokens}]\n")
