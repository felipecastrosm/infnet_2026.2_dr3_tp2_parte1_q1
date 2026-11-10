from fastapi import APIRouter

from models import GenerationRequest, GenerationResponse, MessageResponse
from services import MODEL_NAME, generate_text

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def home():
    return MessageResponse(message="GPT-2 Text Generation API is running")


@router.post("/generate", response_model=GenerationResponse)
def generate(data: GenerationRequest):
    continuation = generate_text(data.text, data.max_new_tokens, data.temperature)
    return GenerationResponse(
        model=MODEL_NAME,
        input_text=data.text,
        continuation=continuation,
        generated_text=f"{data.text}{continuation}",
    )
