from transformers import pipeline

def model_pipeline(text: str, config: dict):
  summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
  min_length = config.get("min_length", 50)
  max_length = config.get("max_length", 100)
  do_sample = config.get("do_sample", False)

  return summarizer(text, min_length=min_length, max_length=max_length, do_sample=do_sample)