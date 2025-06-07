import openai
import os

def summarize_text(text, api_key, model="gpt-4", max_tokens=300):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert text summarizer."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        max_tokens=max_tokens,
        temperature=0.5,
    )

    summary = response['choices'][0]['message']['content'].strip()
    return summary

if __name__ == "__main__":
    text_input = input("Enter the text to summarize:\n")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Enter your OpenAI API key: ")

    summary = summarize_text(text_input, api_key)
    print("\n📌 Summary:\n", summary)
