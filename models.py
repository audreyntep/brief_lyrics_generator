from transformers import pipeline

def get_lstm_generator(text):
    generator = pipeline("text-generation")
    outputs = generator(text, max_length=20)
    return outputs[0]['generated_text']
