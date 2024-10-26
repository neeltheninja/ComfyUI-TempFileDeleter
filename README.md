# TempCleaner Node for ComfyUI

## Overview
This node is designed to streamline your workflow in ComfyUI by efficiently cleaning up temporary files on each run. This node takes no input. You can specify "on" or "off" in the node itself, or just bypass to not use use it. 
## WARNING
This node can delete any files in the folder mentioned in "folder_path" in the node. Be aware of this and change the file path correctly before running any workflow with this node. I will NOT be responsible for random deleted files. 
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

## Usage
Change directory path to the full path of your temp folder inside ComfyUI. 
Refer to example workflow

