import ollama
import feedparser

def get_latest_threat():
    print("Fetching latest threat report...\n")
    feed = feedparser.parse("https://www.bleepingcomputer.com/feed/")
    latest_story = feed.entries[0].summary
    print(f"Raw Threat Data: {latest_story}\n")
    return latest_story

def test_local_ai(text):
    print("Sending to local Llama 3 for summarization...\n")
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': f'Summarize this cyber threat in one sentence: {text}'}
    ])
    print(f"Llama 3 Summary: {response['message']['content']}")

if __name__ == "__main__":
    threat_text = get_latest_threat()
    test_local_ai(threat_text)