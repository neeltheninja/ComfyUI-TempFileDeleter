import os

class TempCleaner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
            },
            "optional": {
                "trigger": ("*", {}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "clean"
    OUTPUT_NODE = True
    CATEGORY = "🧹 Utils"

    def clean(self, folder_path, trigger=None):
        try:
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print(f"Files in {folder_path} have been deleted.")
        except Exception as e:
            print(f"Error: {e}")
        return {}