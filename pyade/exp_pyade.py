import numpy as np
import ioh

from pyade.shade import shade
from pyade.ilshade import ilshade
from pyade.lshade import lshade
from pyade.mpede import mpede
from pyade.sade import sade
from pyade.de import de

versions = ["shade", "ilshade", "lshade", "mpede", "sade", "de"]

class DE_evaluator():
    def __init__(self, version, corr_method):
        self.alg = eval(f"{version}")
        self.corr_method = corr_method
    
    def __call__(self, func):
        self.p = self.alg.get_default_params(dim=func.meta_data.n_variables)
        self.p['bounds'] = np.array([[-5, 5]] * func.meta_data.n_variables)
        self.p['func'] = func
        self.p['corr_method'] = self.corr_method
        self.alg.apply(**self.p)
        
if __name__ == '__main__':
    for sdis in ['saturate', 'mirror', 'COTN', 'unif_resample', 'toroidal']:
        for version in versions:
            de = DE_evaluator(version, sdis)
            exp = ioh.Experiment(algorithm = DE_evaluator(version), #Set the optimization algorithm
            fids = range(1,25), iids = [1,2,3,4,5], dims = [5,10], reps = 5, problem_type = 'BBOB', #Problem definitions
            njobs = 25, #Enable paralellization
            logged = True, folder_name = f'/datanaco/vermettendl/pyade{version}_{sdis}', algorithm_name = f'{version}', store_positions = True, #Logging specifications
            experiment_attributes = {'SDIS' : f'{sdis}'}, #Attribute tracking
            merge_output = True, zip_output = True, remove_data = True #Only keep data as a single zip-file
            )
            exp()