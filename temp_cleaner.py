import os

class TempCleaner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
                "trigger": ("*", {})  # Move trigger to required to handle connections better
            }
        }

    RETURN_TYPES = ("*",)  # Return same type as input for proper chaining
    RETURN_NAMES = ("trigger_out",)
    FUNCTION = "clean"
    CATEGORY = "🧹 Utils"

    def clean(self, folder_path, enabled, trigger):
        if not enabled:
            print("Temp folder cleanup is disabled.")
            return (trigger,)  # Pass through the trigger value

        try:
            count = 0
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    count += 1
            print(f"Deleted {count} files from {folder_path}")
        except Exception as e:
            print(f"Error: {e}")
        
        return (trigger,)  # Pass through the trigger value