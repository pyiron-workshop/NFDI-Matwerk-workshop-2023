# <font style="color:#004A7C" face="Helvetica" > Workflows for materials science simulations with pyiron </font>

Hickel, T. (Speaker)¹; Menon, S. (Speaker)¹; Waseda, O. (Speaker)¹  
  
¹Max-Planck-Institut für Eisenforschung GmbH, Düsseldorf

Presented at the NFDI-Matwerk conference on 29.06.2023


Advanced computational simulations in materials science have reached a maturity that allows one to accurately describe and predict materials properties and processes. The underlying simulation tasks often involve several different models and software that requires expert knowledge to set up a project and to vary input parameters. The accompanying increasing complexity of simulation protocols means that the workflow along the simulation chain becomes an integral part of research. Effective workflow management therefore is important for efficient research and transparent and reproducible results. In this hands-on tutorial we will provide an interactive hands-on introduction into managing workflows with pyiron (www.pyiron.org). Pyiron is an integrated development environment for materials science built on python and Jupyter notebooks that may be used for a wide variety of simulation tasks, from rapid prototyping to high performance computing.


## Creating the environment

The conda environment which includes all the necessary packages is specified in the `environment.yml` file. The environment can be created using:

```
conda env create -f environment.yml  
```

## Building the documentation

To be build the documentation, from the main directory, run:

```
jb build .
```

You can view the documentation at [`_build/index.html`](_build/index.html).
