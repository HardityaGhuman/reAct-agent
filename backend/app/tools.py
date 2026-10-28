import re


def get_email_by_name(name: str) -> dict:
    parts = [p for p in (re.sub(r"[^a-z]", "", w) for w in name.lower().split()) if p]
    if len(parts) < 2:
        return {"error": "Need the employee's first and last name."}
    return {"email": f"{parts[0]}_{''.join(parts[1:])}_99@companyx.com"}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_email_by_name",
            "description": "Returns the company email address of a company X employee given their full name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Full name (first and last) of the employee to get the email of."}
                },
                "required": ["name"],
            },
        },
    }
]

FUNCTIONS = {"get_email_by_name": get_email_by_name}
