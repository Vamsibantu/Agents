import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [{
    "role": "system",
    "content": "You are a concise assistant. Provide brief, direct, and easy-to-understand answers. Strictly avoid long explanations, fluff, or introductory text. Limit your responses to 1-3 sentences maximum unless explicitly asked for detail."
}]

total_input_tokens = 0
total_output_tokens = 0
total_tokens = 0

MAX_MESSAGES = 10

while True:
    query = input("\nEnter your query: ").strip()

    if query.lower() == "exit":
        print("Goodbye!")
        break

    if not query:
        print("Please enter a valid query.")
        continue

    messages.append({
        "role": "user",
        "content": query
    })

    if len(messages) > 4:
        messages = [messages[0]] + messages[-3:]

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
        )

        if response.usage:
            total_input_tokens += response.usage.prompt_tokens
            total_output_tokens += response.usage.completion_tokens
            total_tokens += response.usage.total_tokens

        message = response.choices[0].message
        answer = message.content

        messages.append({
            "role": "assistant",
            "content": answer
        })

        print("\nVamsi:", answer)
        print(f"Input tokens: {total_input_tokens}")
        print(f"Output tokens: {total_output_tokens}")
        print(f"Total tokens: {total_tokens}")

    except Exception as e:
        print(f"\nError: {e}")