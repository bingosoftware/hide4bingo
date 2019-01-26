# External Libaries

1) This software relies upon a Python library: os.

   Please ensure that it is installed in your computer.

2) Please ensure that you are running the latest version of Python2.7.

3) Please ensure that you have HIDE installed, which can be done by following the steps below:

i) git clone https://github.com/cosmo-ethz/hide

ii) cd hide

iii) pip install -r requirements.txt

iv) python setup.py install

# Running the code

1) First copy your local hide4bingo: git clone https://bitbucket.org/lolivari/hide4bingo/src/master/

2) Then go to the hide4bingo directory and type in a terminal: python hide4bingo_install.py

3) Please, before doing the item 2, change the destination and working paths in hide4bingo_install.py!

# Output of the code

1) This software will modify HIDE so it can simulate the BINGO experiment. The extensive documentation on how to use HIDE for BINGO is on the directory "documentation".

# Running the test data

1) First update the paths in "run_hide.py" and in "make_fake_bingo_model_1.py";

2) In the "data" directory, type in a terminal: python make_fake_bingo_model_1.py;

3) In the "hide" directory, type in a terminal: python run_hide.py.

Your output will be in the "hide" directory e and will be named "2018".

To plot part of the TOD that have been generated, type in a terminal: python plot.tod.py. The figure will be named "tod.png".
