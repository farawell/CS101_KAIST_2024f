# CS101_lab_KAIST
This page illustrates how to do your labs on your local machine, not using Alice. Some CS101 lab may need to be tested on the Alice webpage, but still, you can work without internet anytime you want if you do so. I'm working on M1 mac(FYU, it's M1 pro chip with 16GB of RAM). So at least if you're using M-series chip-based Mac, everything will work fine. If you have any problem, email me (farawell777@kaist.ac.kr).

## Configuring miniconda
First of all, miniconda is sufficient. You won't need anaconda.
The base Python version of Alice is 3.6 (As I checked by import sys; sys.version), but since miniconda doesn't support Python 3.6, I used Python 3.8 (3.8.19, actually.). Following are the steps for configuring the conda environment:

1. Download miniconda:
 https://docs.anaconda.com/miniconda/
2. Type the below in the Mac terminal and if no error occurs, you're done! I named the environment as 'cs101', but you may change it if you want.
   ```bash
   conda update conda
   conda create --name cs101 python=3.8
   conda activate cs101
   conda install pillow
   ```
Plus, if you want to deactivate the environment, just type:
```bash
conda deactivate
```

## Configuring site-packages for Python inside your conda environment
You must place 'cs101_libraries_py35' directory and 'worlds' directory insdie the site-package directory. To check the absolute path for the site-package directory, do the following:

1. First activate the environemnt and activate Python.
  ```bash
  conda activate cs101
  python3
  ```

2. Check for the path
```python
import sys
print(sys.path)
```
This will print out several directories, and if one of them contains 'site-packages', that's our target directory.

3. Edit cs1robots.py
In order to let load_world() work just by passing it the relative path (load_world(worlds/harvest1.wld), for example.), you must add the following:

First, add the following in the beginning of the file, where numerous imports are taking place:
```
import os
```

Then, add the below at the line right before 'txt = open(filename, 'r').read()' in the load_world function:
```python
if not os.path.isabs(filename):
        filename = os.path.join('/path/to/your/site-packages/directory', filename)
```

Finally, place 'cs101_libraries_py35' directory and 'worlds' directory inside the path you checked above, for example:

```bash
cd /path/to/the/two/directories/we/will/move/
cp -r cs101_libraries_py35 worlds /path/to/your/site-packages/directory
```

-r option is needed to copy all the files inside the directory.

## Now, have fun!
