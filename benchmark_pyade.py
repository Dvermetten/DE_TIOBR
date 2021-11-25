import numpy as np
import ioh
from itertools import product
from multiprocessing import Pool, cpu_count

from pyade.shade import shade
from pyade.ilshade import ilshade
from pyade.lshade import lshade
from pyade.mpede import mpede
from pyade.sade import sade
from pyade.de import de

versions = ["shade", "ilshade", "lshade", "mpede", "sade", "de"]
sdiss = ['saturate', 'mirror', 'COTN', 'unif_resample', 'toroidal']

def runParallelFunction(runFunction, arguments):
    """
        Return the output of runFunction for each set of arguments,
        making use of as much parallelization as possible on this system

        :param runFunction: The function that can be executed in parallel
        :param arguments:   List of tuples, where each tuple are the arguments
                            to pass to the function
        :return:
    """
    

    arguments = list(arguments)
    p = Pool(min(cpu_count(), len(arguments)))
    results = p.map(runFunction, arguments)
    p.close()
    return results

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
        
def run_de_sdis(temp):
    version, sdis = temp
    print(version, sdis)
    exp = ioh.Experiment(algorithm = DE_evaluator(version, sdis), #Set the optimization algorithm
    fids = range(1,25), iids = [1,2,3,4,5], dims = [30], reps = 5, problem_type = 'BBOB', #Problem definitions
    njobs = 1, #Disable this level of paralellization
    logged = True, folder_name = f'pyade_data/pyade_30D_{version}_{sdis}', algorithm_name = f'{version}', store_positions = True, #Logging specifications
    experiment_attributes = {'SDIS' : f'{sdis}'}, #Attribute tracking
    merge_output = True, zip_output = True, remove_data = True #Only keep data as a single zip-file
    )
    exp()
    return [version, sdis]

if __name__ == '__main__':
    args = product(versions, sdiss)
    runParallelFunction(run_de_sdis, args)