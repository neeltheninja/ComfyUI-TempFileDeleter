import os
from typing import Any, Optional, Tuple

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
    def INPUT_TYPES(cls) -> dict:
        """Defines the expected input types for the node."""
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
            }, 
            "optional": {
                "anything": (any_type, {}), 
            },
            "hidden": {
                "unique_id": "UNIQUE_ID", "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('output',)
    OUTPUT_NODE = True
    CATEGORY = "🧹 Utils"
    FUNCTION = "execute"

    def execute(self, folder_path: str, enabled: bool, **kwargs) -> Tuple[Optional[Any]]:
        """Executes the cleaning operation based on the provided inputs."""
        if not enabled:
            print("Cleanup disabled")
            return (kwargs.get('anything', None),)

        result_text = self.cleanup_folder(folder_path)
        print(result_text)
        return (kwargs.get('anything', None),)

    def cleanup_folder(self, folder_path: str) -> str:
        """Deletes files in the specified folder and returns a status message."""
        try:
            count = 0
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    count += 1
            return f"Deleted {count} files in folder '{folder_path}'."
        except FileNotFoundError:
            return f"Error: Folder '{folder_path}' not found."
        except PermissionError:
            return f"Error: Permission denied for '{folder_path}'."
        except Exception as e:
            return f"Error: {e}"
