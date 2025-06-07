import sys
from summarizer import summarize_text

def summarize_file(file_path, api_key):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        summary = summarize_text(content, api_key)
        print("\n📌 Summary:\n", summary)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarize_from_file.py <filename.txt>")
        sys.exit(1)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Enter your OpenAI API key: ")

    summarize_file(sys.argv[1], api_key)
