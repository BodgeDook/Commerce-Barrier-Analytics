from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class QwenEmailGenerator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-4B-Instruct")
        self.model = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen3-4B-Instruct",
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate_email(self, barrier, user_data):
        prompt = f"""
        You are an e-commerce email marketer.
        User barrier: {barrier}
        User behavior: {user_data}
        Generate a short persuasive email.
        """

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        output = self.model.generate(**inputs, max_new_tokens=200)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
