from pydantic import BaseModel, ConfigDict, Field


class MessageResponse(BaseModel):
    message: str


class GenerationRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    text: str = Field(min_length=1, max_length=1000, examples=["Once upon a time"])
    max_new_tokens: int = Field(default=50, ge=1, le=200)
    temperature: float = Field(default=0.7, gt=0, le=2)


class GenerationResponse(BaseModel):
    model: str
    input_text: str
    continuation: str
    generated_text: str
