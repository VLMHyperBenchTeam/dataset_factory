import os
import json
import glob
from typing import List, Dict, Any
from ..base_iterator import BaseDatasetIterator
from ..models import DatasetItem

class SnilsIterator(BaseDatasetIterator):
    """
    Iterator for SNILS dataset.
    Expected structure:
    root/
      images/clean/*.jpg
      jsons/*.json (filenames match image names)
    """
    def _load_items(self, **kwargs):
        images_dir = os.path.join(self.dataset_dir_path, "images", "clean")
        jsons_dir = os.path.join(self.dataset_dir_path, "jsons")
        
        image_files = sorted(glob.glob(os.path.join(images_dir, "*.jpg")))
        
        for img_path in image_files:
            basename = os.path.splitext(os.path.basename(img_path))[0]
            json_path = os.path.join(jsons_dir, f"{basename}.json")
            
            if not os.path.exists(json_path):
                continue
                
            with open(json_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # Стандартный промпт для извлечения информации
            prompt = "Extract all fields from this SNILS document as JSON. The output should contain a 'fields' object with keys like 'Полное имя', 'Номер СНИЛС', etc."
            
            self.items.append(DatasetItem(
                image_path=img_path,
                text=prompt,
                metadata=metadata
            ))