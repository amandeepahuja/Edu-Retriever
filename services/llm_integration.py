# services/llm_integration.py

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch

# Load the Flan-T5 model and tokenizer
model_name = "google/flan-t5-base"  # or consider "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Optional summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

def summarize_context(relevant_chunks):
    """Summarize relevant chunks to create a concise context."""
    context = "\n".join(relevant_chunks)
    summary = summarizer(context, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    return summary

def generate_answer_with_llm(user_query, relevant_chunks):
    """
    Uses Flan-T5 to generate a response based on the query and summarized context.
    """
    # Summarize context for better coherence
    context_summary = summarize_context(relevant_chunks)
    
    # Create an explicit, structured prompt
    prompt = (f"Given the following summarized context, answer the question clearly and in detail.\n\n"
              f"Summarized Context: {context_summary}\n\n"
              f"Question: {user_query}\n\n"
              f"Please provide an answer with an explanation and examples where relevant.\n\n"
              f"Answer:")

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

    # Generate the response with fine-tuned hyperparameters
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_length=150,
            num_beams=7,
            early_stopping=True,
            temperature=0.7,
            top_p=0.9
        )

    # Decode and return the response
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
