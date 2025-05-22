import wikipedia
import os

# List of topics you want to include in your corpus
topics = [
    "Artificial intelligence",
    "Ethics of artificial intelligence",
    "Algorithmic bias",
    "Data privacy",
    "Surveillance",
    "Autonomous car",
    "EU AI Act",
]

corpus_dir = "corpus"
os.makedirs(corpus_dir, exist_ok=True)

for topic in topics:
    try:
        print(f"Fetching page for: {topic}")
        page = wikipedia.page(topic)
        content = page.content

        # Save to a file named after the topic (replace spaces with underscores)
        filename = f"{topic.replace(' ', '_')}.txt"
        filepath = os.path.join(corpus_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved: {filepath}")
    except Exception as e:
        print(f"Error fetching {topic}: {e}")
