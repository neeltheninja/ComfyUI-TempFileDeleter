import os

class TempCleaner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
                "any_input": ("*",),  # Wildcard input type that accepts anything
            },
        }

    RETURN_TYPES = ("*",)  # Return whatever type we received
    FUNCTION = "clean"
    OUTPUT_NODE = True
    CATEGORY = "🧹 Utils"

    def clean(self, folder_path, enabled, any_input):
        if not enabled:
            print("Temp folder cleanup is disabled.")
            return (any_input,)

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
        
        return (any_input,)  # Pass through whatever input we received