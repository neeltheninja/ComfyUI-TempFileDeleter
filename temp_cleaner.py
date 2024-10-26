import os
from typing import Any

class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False
    
any_type = AlwaysEqualProxy("*")

class TempCleaner:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}, "optional": {"anything": (any_type, {}), },
                "hidden": {"unique_id": "UNIQUE_ID", "extra_pnginfo": "EXTRA_PNGINFO",
                           }}

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('output',)
    INPUT_IS_LIST = True
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (False,)
    CATEGORY = "🧹 Utils"
    FUNCTION = "execute"

    def execute(self, folder_path: str, enabled: bool, **kwargs):
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

        # Return all inputs as outputs, None if not connected
        return tuple(kwargs.get(name) for name in self.RETURN_NAMES)