from app.structure import INSTRUCTIONS, get_model_response

MAX_MESSAGES = 20

thread = [{"role": "system", "content": INSTRUCTIONS}]

while (query := input("What would you like to ask? ")) != "exit":
    if len(thread) > MAX_MESSAGES:
        print("[session] message limit reached, starting a new conversation\n")
        thread = thread[:1]
    thread.append({"role": "user", "content": query})
    print(f"[answer] {get_model_response(thread)}\n")
