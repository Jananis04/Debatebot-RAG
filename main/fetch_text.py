import wikipediaapi

def fetch_wikipedia_page(topic, max_sections=3):
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(topic)
    if not page.exists():
        return None
    content = page.summary + "\n\n"
    count = 0
    for section in page.sections:
        if count >= max_sections:
            break
        content += section.text + "\n\n"
        count += 1

    return content

if __name__ == "__main__":
    topic = input("Enter Wikipedia topic: ")
    text = fetch_wikipedia_page(topic)
    if text:
        with open(f"corpus/{topic.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Saved Wikipedia content for {topic}")
    else:
        print("Topic not found on Wikipedia.")
