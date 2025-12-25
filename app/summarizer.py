import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

MODEL_NAME = "facebook/bart-large-cnn"
MODEL_DIR = "models/summarizer"

os.makedirs(MODEL_DIR, exist_ok=True)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    cache_dir=MODEL_DIR
)

# Load model
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    cache_dir=MODEL_DIR
)

# Create pipeline ONCE
summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU
)

def summarize_chunks(chunks: list[str]) -> str:
    """
    Hierarchical summarization:
    1. Summarize each chunk
    2. Summarize the combined summaries
    """

    partial_summaries = []

    for i, chunk in enumerate(chunks):
        result = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )
        partial_summaries.append(result[0]["summary_text"])

    combined_summary = " ".join(partial_summaries)

    final_result = summarizer(
        combined_summary,
        max_length=200,
        min_length=80,
        do_sample=False
    )

    return final_result[0]["summary_text"]
