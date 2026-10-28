import json
from pathlib import Path

from app.client import client, MODEL
from app.tools import TOOLS, FUNCTIONS

MAX_STEPS = 6

POLICIES = (Path(__file__).parent.parent / "files" / "company_policies.md").read_text()

INSTRUCTIONS = f"""# Persona
You are Coursera bot, a support assistant for company X.

# Context
You serve employees and customers of company X. The company policy document below is your only source for policy facts.

<company_policies>
{POLICIES}
</company_policies>

# Task
Answer questions about TypeScript, large language models and generative AI, and the policies of company X.
For policy questions, answer only from the policy document; if it does not cover the question, say so.
For employee email addresses, always use the get_email_by_name tool; never build an email yourself.
Politely refuse questions about anything else.

# Format
Short, plain-language answers. Never include code.
For email address questions, reply with only the email address and nothing else."""


def get_model_response(thread: list) -> str:
    for _ in range(MAX_STEPS):
        res = client.chat.completions.create(
            model=MODEL, messages=thread, tools=TOOLS, tool_choice="auto", reasoning_effort="medium"
        )
        msg = res.choices[0].message
        thread.append(msg)
        if reasoning := getattr(msg, "reasoning", None):
            print(f"[think] {reasoning}")
        print(f"[usage] in={res.usage.prompt_tokens} out={res.usage.completion_tokens}")

        if not msg.tool_calls:
            return msg.content

        for call in msg.tool_calls:
            try:
                result = FUNCTIONS[call.function.name](**json.loads(call.function.arguments))
            except Exception as e:
                result = {"error": f"{type(e).__name__}: {e}"}
            print(f"[tool] {call.function.name}({call.function.arguments})\n[result] {result}")
            thread.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

    return "Stopped: too many steps."
