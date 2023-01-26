from ConfigReader import ConfigReader as cr
from scipy.stats import chi2_contingency
import pandas as pd
import statsmodels.api as sm
from sklearn.feature_selection import chi2
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
class ChiSquareTest:
    def __init__(self, path):
        self.config = cr.read(path)
    def create_crosstab(self, var1, var2):
        # creating crosstab data frame
        tabs = pd.crosstab(var1, var2)
        # creating a statsmodels table object
        table = sm.stats.Table(tabs)
        return tabs
    def execute(self, data, vis=False) -> dict:
        result = {}
        if len(data.axes[1]) > 2:
            chi2 = chi2(data[self.config['x']], data[self.config['y']])
            result['stat'] = chi2[0]
            result['p'] = chi2[1]
        else : 
            crosstabs = self.create_crosstab(data[self.config['x'][0]], data[self.config['y'][0]])
            stat, p, dof, expected = chi2_contingency(crosstabs)
            result = {
                        'stat' : stat,
                        'p' : p,
                        'dof' : dof,
                        'expected' : list(expected)
                     }
        if vis:
            plt.figure(figsize=(12,8)) 
            sns.heatmap(crosstabs, annot=True, cmap="YlGnBu")
            plt.show()
        return result, crosstabs

class CramersV(ChiSquareTest):
    def __init__(self, config_path):
        super().__init__(config_path)
    def execute_cramer(self, data):
        result, crosstab = self.execute(data)
        n = crosstab.sum().sum()
        dof = min(crosstab.shape) - 1
        v = np.sqrt(result['stat'] / (n * dof))
        result = {
            'v' : v,
            "dof" : dof,
        }
        return result

if __name__ == '__main__':
    cst = ChiSquareTest('Configs/stats-test01.yaml')
    df = pd.DataFrame({'Gender' : ['M', 'M', 'M', 'F', 'F'] * 10,
                   'isSmoker' : ['Smoker', 'Smoker', 'Non-Smpoker', 'Non-Smpoker', 'Smoker'] * 10
                  })
    result = cst.execute(df, vis=True)[0]
    crv = CramersV('Configs/stats-test01.yaml')
    cramer_result = crv.execute_cramer(df)
    print(result)
    print(cramer_result)