# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ###document!

from change_detection import functions as chg
from ebmdatalab import bq
from lib.outliers import * 

# NBVAL_IGNORE_OUTPUT
# ^this is a magic comment to work around this issue https://github.com/ebmdatalab/custom-docker/issues/10
doac = chg.ChangeDetection('ccg_data_doac%',
                                    measure=True,
                                    direction='up',
                                    use_cache=True,
                                    overwrite=False,
                                    verbose=False,
                                    draw_figures='no')
doac.run()

doacs = doac.concatenate_outputs()
doacs.head()

# +
filtered_sparkline(doacs,
                  'ccg_data_doac/ccg_data_doacs',
                   'ccg_data_doacs'
                  )


#File data/ccg_data_doac/bq_cache.csv does not exist: 'data/ccg_data_doac/bq_cache.csv'
# -




