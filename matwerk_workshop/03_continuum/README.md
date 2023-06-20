# pyiron hands-on session

<img src='https://raw.githubusercontent.com/pyiron/pyiron.github.io/main/images/logo_dark.png' width="300em">

Berlin February 8, 2023

- Implementation example of [`DAMASK`](https://damask.mpie.de)
- Combination with atomistic simulation
- Creation of workflow using `ScriptJob`

# Implementation example with [`DAMASK`](https://damask.mpie.de)

[`Damask`](https://damask.mpie.de) is a unified multi-physics crystal plasticity simulation package.

In this example: Loading test

But hey, how about:

element -> `LAMMPS` -> elastic constants -> `DAMASK` -> stress & strain ?

## How to implement external codes in pyiron

### `ScriptJob`

Create a wrapper around an external program

### `TemplateJob`

pyiron template class with input and output, as well as internal routine functions such as `job.check_setup`

### `AtomisticGenericJob` `GenericDFGJob` etc.

pyiron template class with physically meaningful contents such as
- `job.structure`
- `job.output.temperature`

## Template classes as an example of PhD thesis

### `ScriptJob`

Write your phd in Word, Latex, Notepad or anything you like

### `TemplateJob`

Here's `template.tex` with pre-defined header and footer. Fill out the rest as you like

### `AtomisticGenericJob` etc.

Here's `template.tex` with the following pre-defined sections:

- Introduction
  - Scientific background
  - Technical challenges
  - Previous studies
  - Main results of this thesis
- Experimental setup
- Results
- Discussion
- Conclusion

And feel free to create more sections if needed.

Note: This is a figurative comparison which does not have one to one equivalence in pyiron

# How to use `ScriptJob`

## Step I: Run a notebook from another notebook

In `submitter.ipynb`:

```python
from pyiron import Project
pr = Project('submission')
job = pr.create.job.ScriptJob('calculation')
job.script_path = 'calculation.ipynb'
job.run()
```

In `calculation.ipynb`:

```python
from pyiron import Project
pr = Project('calculation')
def calculation(value):
    return 2 * value
result = calculation(5)
print(result)
```

## Step II: Configure input and output

In `submitter.ipynb`:

```python
from pyiron import Project

pr = Project('submission')
job = pr.create.job.ScriptJob('calculation')
job.script_path = 'calculation.ipynb'
job.input['value'] = 5 # New
job.run()
print(job['output/result']) # New
```

In `calculation.ipynb`:

```python
from pyiron import Project
from pyiron import Notebook # New

pr = Project(default_working_directory=True) # Changed
external_input = pr.get_external_input() # New
def calculation(value):
    return 2 * value
result = calculation(external_input['value'])
Notebook().store_custom_output_dict( # New
    {"result": result}
)
```

# How to use `TemplateJob`

```python
from pyiron_base import Project, PythonTemplateJob

def calculation(value):
    return 2 * value

class ToyJob(PythonTemplateJob):
    def __init__(self, project, job_name):
        super().__init__(project, job_name) 
        self.input.value = None

    def run_static(self):
        self.output.result = calculation(self.input.value)
        self.status.finished = True
        self.to_hdf()

pr = Project('template')
job = pr.create_job(job_type=ToyJob, job_name="toy")
job.input.value = 5
job.run()
```

## Example of `TemplateJob` with internal routines

```python
from pyiron_base import Project, PythonTemplateJob

def calculation(value):
    return 2 * value

class ToyJob(PythonTemplateJob):
    def __init__(self, project, job_name):
        super().__init__(project, job_name) 
        self.input.value = None

    def validate_ready_to_run(self): # New
        super().validate_ready_to_run()
        if self.input.value is None:
            raise ValueError('job.input.value not set')

    def run_static(self):
        self.output.result = calculation(self.input.value)
        self.status.finished = True
        self.to_hdf()

pr = Project('template')
job = pr.create_job(job_type=ToyJob, job_name="toy")
job.run()
```

# Perspectives

## Where's the beautiful workflow diagram?

Now it's under construction (ironflow). Likely to be made available in the first half of 2023

## Why should I use pyiron (and not other workflow tools)?

- pyiron is **highly** interactive
- Flexible level of granularity

Currently we are going through an important structural transformation -> Your chance to get involved in feature suggestions!
