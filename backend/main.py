from app.structure import INSTRUCTIONS, get_model_response

thread = [{"role": "system", "content": INSTRUCTIONS}]

while (query := input("What would you like to ask? ")) != "exit":
    thread.append({"role": "user", "content": query})
    print(f"[answer] {get_model_response(thread)}\n")
