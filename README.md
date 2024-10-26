# TempCleaner Node for ComfyUI
![shapes](/Workflows/workflow.png)
## Overview
This node is designed to streamline your workflow in ComfyUI by efficiently cleaning up temporary files on each run. This node takes no input. You can specify "on" or "off" in the node itself, or just bypass to not use use it. 
## WARNING
This node can delete any files in the folder mentioned in "folder_path" in the node. Be aware of this and change the folder path correctly before running any workflow with this node. I will NOT be responsible for wrongly deleted files because you didn't read this beforehand. 
## Installation

1. Change directory to custom nodes of **ComfyUI**:

   ```bash
   cd ~/ComfyUI/custom_nodes
   ```

2. Clone this repo here:

   ```bash
   git clone https://github.com/neeltheninja/ComfyUI-TempFileDeleter.git
   ```

3. Restart **ComfyUI**.
4. Find the node by searching for "Temp Cleaner" in your workflow. Make sure to restart your ComfyUI and refresh your workflow before trying this. 

## Usage
Change directory path to the full path of your temp folder inside ComfyUI. 
Refer to example workflow

