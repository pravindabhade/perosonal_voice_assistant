from ollama import chat

conversation = []

def ask_ai(text):

    conversation.append(
        {"role": "user", "content": text}
    )

    response = chat(
        model="llama3",
        messages=conversation
    )

    reply = response["message"]["content"]

    conversation.append(
        {"role": "assistant", "content": reply}
    )

    return reply