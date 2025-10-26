from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: int = Field(
        ...,
        description="The predicted category",
        example= 1
    )

    confidence: float = Field(
        ...,
        description="Model's confidence score ",
        example= 0.85
    )

    class_probabilities : Dict[int, float] = Field(
        ...,
        description="Probabilities distribution across all classes",
        example = {0:0.45, 1:0.55}
    )