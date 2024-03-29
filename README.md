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

3. Install the required Python packages and dependencies. With the virtual environment active, move into the `lazyspectra` folder
   ```
   (lazyenv) $ cd lazyspectra
   ```
   and type
   ```
   (lazyenv) $ pip install .
   ```
4. Install Betashape following the instruction http://www.lnhb.fr/rd-activities/spectrum-processing-software/ (V2.3 tested).

   I suggest you to follow these steps: download the betashape folder, make every file inside the main betashape folder executable 
   ```
   chmod +x file_name
   ```
   I highly suggest you to create a virtual link to the betashape directory. If the betashape directory has, let's say, betashape_path, create a virtual link in the chosen path (path_target)
   ```
   cd path_target
   ln -s betashape_path path_target/betashape_rightversion
   ```
   If you download a new betashape version, just change the previous link.

   Make sure that the betashape directory is defined in the PATH. Write the following lines in your bashrc file
   ```
   #ADDED FOR BETASHAPE
   export PATH="$PATH:path_target/betashape_rightversion"
   ```
   reboot your terminal, and you should be good to go! 

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
