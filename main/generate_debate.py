from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("vectorstore", embedding_model, allow_dangerous_deserialization=True)

retriever = db.as_retriever()

model_name = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    trust_remote_code=True
)

def query_llm(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def generate_debate(topic):
    relevant_docs = db.similarity_search(topic, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs]) if relevant_docs else ""

    if context and len(context.strip()) > 20:
        prompt = f"""You are an expert debate bot. Based ONLY on the following context, generate:
- A strong argument **in favor** of the topic: "{topic}"
- A strong argument **against** the topic

Context:
{context}
"""
    else:
        prompt = f"""You are an expert debate bot. Generate two well-reasoned and balanced arguments:
- One **in favor** of the topic: "{topic}"
- One **against** it

Use general knowledge, logical reasoning, and rhetorical techniques.
"""
    return query_llm(prompt)
