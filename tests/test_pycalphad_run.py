import unittest
import os
import numpy as np
from fmap.core.pycalphad_run import pycalphad_eq,pycalphad_scheil

class TestCalculations(unittest.TestCase):
    
    def setUp(self):
        #path = resources.files('fmap').joinpath('tests/testsCaseFiles')
        path = './testsCaseFiles'
        settings= ((600, 2000, 10),3,3,['AL', 'CU', 'AG'],['Cu', 'Ag', 'Al'],['Ag', 'Al'],path+'/Ag-Al-Cu.TDB',101325,'massFraction')
        np.save(f'{path}/setting.npy',settings)
    def test_pycalphad_eq(self):
        path = './testsCaseFiles'
        pycalphad_eq(path)
        self.assertTrue(path+'/Pycalphad/Equilibrium Simulation/data.json')
    def test_pycalphad_scheil(self):
        path = './testsCaseFiles'
        pycalphad_scheil(path,2000)
        self.assertTrue(path+'/Pycalphad/Scheil Simulation/data.json')      
    # def tearDown(self):
    #     path = './testsCaseFiles'
    #     os.remove(path+'/Pycalphad')


if __name__ == '__main__':
    unittest.main()