# Lazyspectra
Insert description here
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)

### Installation
1. Open the terminal and clone the repository locally:
   Clone using a password protected SSH key (preferred)
   ```
   $ git clone 
   ```
   or Clone with HTTPS using the web URL
   ```
   $ git clone https://github.com/matteo-brg/lazyspectra.git
   ```

2. Install virtualenv using `python >= 3.8`
   ```
   $ sudo pip install virtualenv
   ```
   Create the lazyspectra virtual environment based on python3.X (X>=8)
   ```
   $ virtualenv -p `which python3.X` ~/lazyenv
   ```
   Run the following command to activate the virtual environment
   ```
   $ source lazyenv/bin/activate
   ```
   (optional) Check the version of python being used in the virtual environment
   ```
   (lazyenv) $ python -V
   ```

3. Install the required Python packages and dependencies, which include CmdStanPy. With the virtual environment active, move into the `baynes` folder
   ```
   (lazyenv) $ cd lazyspectra
   ```
   and type
   ```
   (lazyenv) $ pip install .
   ```


### Project top-level directory layout

    baynes
    │
    ├── src                            # Project source code
    ├── scripts                        # Directory for scripts and executables
    ├── config                         # Directory for config files
    ├── notebook                       # Directory for jupyter notebook and guides
    ├── requirements.txt               # Requirements file specifing the lists of packages to install
    ├── setup.py                       #
    ├── .gitignore                     # Specifies intentionally untracked files to ignore
    └── README.md                      # README file

 ASCII art tree structure taken from [here](https://codepen.io/patrickhlauke/pen/azbYWZ)

### Documentation
*

 ### About README
 The README files are text files that introduces and explains a project. It contains information that is commonly required to understand what the project is about.
 At this [link](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) a basic guide on the writing and formatting syntax
