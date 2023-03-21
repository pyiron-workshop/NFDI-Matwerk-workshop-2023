# This file contains some useful helper functions to make the notebooks more readable

import pandas as pd
import os

pot_ace = pd.DataFrame({
    'Name': ['LiAl_yace'],
    'Filename': [[os.path.abspath("../potentials/ACE/AlLi-6gen-18May.yace")]],
    'Model': ["ACE"],
    'Species': [['Al', 'Li']],
    'Config': [['pair_style pace\n', 'pair_coeff * * AlLi-6gen-18May.yace Al Li\n']]
})


def get_clean_project_name(pot):    
    if isinstance(pot, pd.DataFrame):
        return pot["Name"][0]
    else:
        raise ValueError("Invalid potential type")
