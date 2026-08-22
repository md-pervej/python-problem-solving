
# -----49:Example 1: Using pathlib.Path.mkdir-----

from pathlib import Path
# Path("css/img").mkdir(parents=True,exist_ok=True)

# Example 2: Using os.makedirs
import os
# os.makedirs("assets/js/js1")

# Example 3: Using distutils.dir_util

import distutils.dir_util
distutils.dir_util.makepath("dummy/folder1/folder2")