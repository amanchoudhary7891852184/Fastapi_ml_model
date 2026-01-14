from pydantic import BaseModel, Field

class UrineInput(BaseModel):
    gravity: float = Field(..., description="Urine specific gravity")
    ph: float = Field(..., description="Urine pH")
    osmo: float = Field(..., description="Osmolarity")
    cond: float = Field(..., description="Conductivity")
    urea: float = Field(..., description="Urea concentration")
    calc: float = Field(..., description="Calcium concentration")

class PredictionOutput(BaseModel):
    prediction: int
    result: str
