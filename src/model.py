from transformers import pipeline
import torch

class TextGenerator:
    def __init__(self, model_name="GlebNoNeGolubin/results"):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.pipe = pipeline("text2text-generation", model=model_name, device=self.device)

    def generate(self, text, max_length=768, num_return_sequences=1,
                repetition_penalty=2.0, temperature=0.9, do_sample=True):
        try:
            output = self.pipe(
                text,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                repetition_penalty=repetition_penalty,
                temperature=temperature,
                do_sample=do_sample
            )
            return output[0]['generated_text']
        except Exception as e:
            raise Exception(f"Generation error: {str(e)}")