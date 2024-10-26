import os
from typing import Any

class TempCleaner:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "any_value": ("*",),
            },
            "hidden": {
                # Reserved for future use
            },
        }

    CATEGORY = "🧹 Utils"
    INPUT_IS_LIST = True
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("pass_through",)
    OUTPUT_NODE = True
    FUNCTION = "execute"

    def execute(self, folder_path: str, enabled: bool, any_value: Any = None) -> dict:
        # Initialize response
        result_text = "No action taken"
        
        if enabled:
            try:
                count = 0
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        count += 1
                result_text = f"Deleted {count} files from {folder_path}"
            except Exception as e:
                result_text = f"Error: {e}"
        else:
            result_text = "Cleanup disabled"

        # Print result to console
        print(result_text)

        # Return both UI update and pass-through value
        return {
            "ui": {"text": [result_text]},
            "result": (any_value[0] if isinstance(any_value, list) and any_value else None,)
        }