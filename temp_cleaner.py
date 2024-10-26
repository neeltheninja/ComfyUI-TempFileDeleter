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
                "image": ("IMAGE",),
                "latent": ("LATENT",),
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "conditioning": ("CONDITIONING",),
                "control_net": ("CONTROL_NET",),
                "string": ("STRING",),
                "any_value": ("*",),
            },
            "hidden": {
                # Reserved for future use
            },
        }

    CATEGORY = "🧹 Utils"
    INPUT_IS_LIST = False
    RETURN_TYPES = ("IMAGE", "LATENT", "MODEL", "CLIP", "VAE", "CONDITIONING", "CONTROL_NET", "STRING",)
    RETURN_NAMES = ("image", "latent", "model", "clip", "vae", "conditioning", "control_net", "string",)
    OUTPUT_NODE = True
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