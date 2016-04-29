# UNIT TESTS USING TEST DATA

# Import required packages used in this testing script

import os
import unittest
import inspect
import projectburg

# Path of current directory

def data_directory():
    rtn = os.path.join(os.path.dirname(os.path.abspath(inspect.getsourcefile(data_directory))), "data")
    assert os.path.isdir(rtn)
    return rtn

# Define the test

class TestProjectBurg(unittest.TestCase):

    def test_simple_data(self):
        data_file = os.path.join(data_directory(), "simple_data.sql")
        dat = projectburg.dataFactory.sql.create_tic_dat_from_sql(data_file)
        soln = projectburg.solve(dat,1,5,18)
        self.assertTrue(soln.utilisation[0][vancrew] = 7 * 3 * 2))

        # if I put member 1 on leave for the week, then he/she should be scheduled as such
        for d in range(1,7):
            dat.leave[1,d]["value"] = 1
        soln2 = projectburg.solve(dat,1,5,18)
        for d in range(1,7):
            self.assertTrue(soln.roster[1,d]["value"] = 17)
        # and not more members can be utilised (van crew)
        self.assertTrue(soln.utilisation[0][vancrew] >= soln.utilisation[0][vancrew])

        # can add more behavioural tests

# Run the tests

if __name__ == "__main__":
    unittest.main()
