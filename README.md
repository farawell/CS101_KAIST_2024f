# CS101 Lab (KAIST)
This repository provides instructions for setting up your miniconda environment to complete CS101 labs on your local machine, without relying on Elice. While some codes may need to be tested on the Elice platform, this setup allows you to work offline. These instructions are optimized for Mac users with M-series chips (e.g., M1, M1 Pro, M4, etc). If you encounter any issues, feel free to email me at *farawell777 at kaist.ac.kr*.

***I recommend using Miniconda rather than directly on your Mac. Running it without isolating the environment may lead to errors (It actually happened to me). To ensure smooth operation on your local machine, it’s essential to create and work within a dedicated conda environment. Additionally, after setting up all the necessary steps, in VSCode, ensure that you select the Python interpreter associated with the conda environment you've created. This will allow VSCode to execute your code using the correct environment and dependencies.***

___

## Setting up Miniconda
Miniconda is sufficient for this setup; you won't need the full Anaconda package. Elice uses Python 3.6 (as verified by running `import sys; sys.version`), but since Miniconda does not support Python 3.6, we will use Python 3.8 (version 3.8.19). Follow these steps to configure your conda environment:

1. Download Miniconda:  
   [https://docs.anaconda.com/miniconda/](https://docs.anaconda.com/miniconda/)
2. Open a terminal and run the following commands (change the environment name if desired):
   ```bash
   conda update conda
   conda create --name cs101 python=3.8
   conda activate cs101
   conda install pillow
To deactivate the environment, use:
```bash
conda deactivate
```

## Setting up site-packages for your Python environment
You must place 'cs101_libraries_py35' directory and 'worlds' directory insdie the site-package directory. To check the absolute path for the site-package directory, do the following:

1. Modify cs1robots.py
To enable load_world() to work with relative paths (e.g., load_world(worlds/harvest1.wld)), follow these steps:

First, add the following import at the beginning of the file, where other imports are listed:
```python
import os
```

Modify the load_world() function. Right before the line txt = open(filename, 'r').read(), add:
```python
if not os.path.isabs(filename):
        filename = os.path.join('/path/to/your/site-packages/directory', filename)
```

2. Activate your conda environment and start Python:
  ```bash
  conda activate cs101
  python3
  ```

3. Print and check the Python path:
```python
import sys
print(sys.path)
```
Look for a directory that contains the string 'site-packages'. This is your target directory.

4. Place the cs101_libraries_py35 and worlds directories in the site-packages directory you identified earlier. For example:

```bash
cd /path/to/the/two/directories/we/will/move/
cp -r cs101_libraries_py35 worlds /path/to/your/site-packages/directory
```

The -r option is used to recursively copy all files inside the directory.

## You're all set!
Enjoy working on your CS101 labs on your local Mac!
