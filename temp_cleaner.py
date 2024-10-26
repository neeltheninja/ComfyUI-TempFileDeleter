import os

class TempCleaner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "trigger": ("*", {}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("files_deleted",)
    FUNCTION = "clean"
    OUTPUT_NODE = True
    CATEGORY = "🧹 Utils"

    def clean(self, folder_path, enabled, trigger=None):
        if not enabled:
            print("Temp folder cleanup is disabled.")
            return (0,)

        try:
            count = 0
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    count += 1
            print(f"Deleted {count} files from {folder_path}")
            return (count,)
        except Exception as e:
            print(f"Error: {e}")
            return (0,)