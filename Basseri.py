def api():
    return "API_KEY"


from openai import OpenAI

client = OpenAI(
    api_key=api(),  # Replace YOUR_API_KEY_HERE with your actual API key
    base_url="https://api.aimlapi.com",
)


def start_chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("Victor: ")

        if user_input.lower() == 'exit':
            print("Exiting the chatbot.")
            break

        system_message = {
            "role": "system",
            "content": "You are an AI assistant who knows everything."
        }
        user_message = {"role": "user", "content": user_input}
        response = client.chat.completions.create(
            model=
            "mistralai/Mistral-7B-Instruct-v0.2",  # Adjust the model as needed
            messages=[system_message, user_message],
        )

        message = response.choices[0].message.content
        print(f"Basseri: {message}")


if __name__ == "__main__":
    start_chatbot()
