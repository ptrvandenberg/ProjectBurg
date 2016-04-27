# Project Burg [working title] Excel data: field force rostering.

# Copyright 2016, Peter van den Berg

# This file solves the model with the data provided by the Excel file "projectburgxlsdata.xls".
# It prints the summary information to the screen and writes the solution into Excel file "solution.xls".

from dietmodel import solve, dataFactory, solutionFactory
import os

# read the data
dat = dataFactory.xls.create_tic_dat("projectburgdata.xls", freeze_it=True)

solution =  solve(dat)

if solution :
    print('\nVanCrew: %g' % solution.utilisation[0]["vancrew"])
    solutionFactory.xls.write_file(solution, "solution.xls", allow_overwrite=True)
else :
    print('\nNo solution')
