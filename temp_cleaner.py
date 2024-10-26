import os

class TempCleaner:
    def __init__(self):
        self.type_aliases = {
            "IMAGE": "IMAGE",
            "LATENT": "LATENT",
            "MODEL": "MODEL",
            "CLIP": "CLIP",
            "VAE": "VAE",
            "CONDITIONING": "CONDITIONING",
            "STRING": "STRING",
            "INT": "INT",
            "FLOAT": "FLOAT",
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "temp"}),
                "enabled": ("BOOLEAN", {"default": True}),
                "input": (list(cls().type_aliases.keys()),),  # Accept any of these types
            },
        }

    RETURN_TYPES = tuple(list(cls().type_aliases.keys()))  # Return any of these types
    FUNCTION = "clean"
    OUTPUT_NODE = True
    CATEGORY = "🧹 Utils"

    def clean(self, folder_path, enabled, input):
        if not enabled:
            print("Temp folder cleanup is disabled.")
            return (input,)

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
        
        return (input,)