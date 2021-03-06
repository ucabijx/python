# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 12:37:53 2015

@author: davekensinger
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh import mpl
from bokeh.plotting import show

# We generated random data
data = 1 + np.random.randn(20, 6)

# And then just call the violinplot from Seaborn
sns.violinplot(data)

plt.title("Seaborn violin plot in bokeh.")

show(mpl.to_bokeh())