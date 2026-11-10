from functools import lru_cache

from transformers import Pipeline, pipeline

MODEL_NAME = "gpt2"


@lru_cache
def get_generator() -> Pipeline:
    return pipeline("text-generation", model=MODEL_NAME)


def generate_text(text: str, max_new_tokens: int, temperature: float) -> str:
    generator = get_generator()
    result = generator(
        text,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2,
        return_full_text=False,
        pad_token_id=generator.tokenizer.eos_token_id,
    )
    return result[0]["generated_text"]
