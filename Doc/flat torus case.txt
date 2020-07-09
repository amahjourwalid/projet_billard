#flat torus case  billard

## table of contents 
 1. Installing and Implementing
 2. Special depencies 
 3. flat torus case billar animation 
 4. flat torus case billar statistics 

### 1. installing and Iplementig 
* Installing from github 
To install this package from github the user can put the prompt:
$ pip install git+https://github.com/amahjourwalid/projet_billard

### 2. Special depencies 
to correctly use this package please install theses packages 
﻿matplotlib==3.2.1
numpy==1.18.4
pandas==1.0.3
pytest==5.4.2
scipy==1.4.1
seaborn==0.10.1

### 3.flat torus case billard animation 
In order to see the animation please run "flat torus case billard" code, a graphical user interface window will pop out, enter an angle press enter the click on start button. the result name and  an array containing the start angle, number of "V"s and number of "H"s will be returned.


### 4. flat torus case billard statistics 
To get some basic statistics on square case the billard please run all the code chunks in "flat torus case billard statistics ".
the code returns: 
* a dataframe containing diffrent set of angles and the numbers of "V" and "H" in every result name of the different angles,
* a summary table of the dataframe containing : count, mean , standard deviation ,... 
* a correlation matrix between the numbers of "V" and "H" ande the angles
* a correlation grafic between the numbers of "V" and "H" ande the angles


