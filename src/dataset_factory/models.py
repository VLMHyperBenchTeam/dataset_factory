from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class DatasetItem(BaseModel):
    """
    Unified object representing a single item in a dataset.
    """
    image_path: Optional[str] = Field(None, description="Path to the image file")
    text: Optional[str] = Field(None, description="Text content (e.g., question or prompt)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata for the item")