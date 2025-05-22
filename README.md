# DebateBot
DebateBot is an AI-powered chatbot designed to generate structured pro/con arguments on any given topic using state-of-the-art language models. It leverages prompt engineering and retrieval-augmented generation (RAG) to provide balanced, insightful debate points efficiently.

Features
Generates detailed pro and con arguments on user-supplied topics
Uses advanced transformer-based language models (e.g., Mistral 7B, or alternatives)
Lightweight and optimized for laptops with limited GPU VRAM (6GB+)
Easy to deploy with Streamlit UI for quick interaction
Customizable prompts and debate styles

Installation
Clone this repository:

bash
```
git clone https://github.com/your-username/debatebot.git
cd debatebot
```
(Recommended) Create and activate a Python virtual environment:

bash
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Note: For some models (like Mistral or LLaMA variants), you may need additional setup or model files.

Usage
Configure the model and device in generate_debate.py or relevant config file.

Run the Streamlit app:

```bash
streamlit run app.py
```
Enter a debate topic in the UI and get balanced pro and con arguments generated in real-time.

Model Notes
This bot currently supports models like Mistral 7B optimized for smaller GPUs.

If you experience memory issues, consider using quantized or smaller models.

You can swap models by changing model_name in the code.

Tokenizer installation may require additional libraries like sentencepiece.
