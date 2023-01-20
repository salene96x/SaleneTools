import sys
import yaml
class Visualization:
    def __init__(self, lib_type):
        self.lib_type = lib_type
    def histogram(self, config):
        pass
    def scatter(self, config):
        pass
    def barplot(self, config):
        pass
    def violinplot(self, config):
        pass
    
if __name__ == '__main__':
    try : 
        system = sys.argv[1]
    except:
        raise ValueError("No system name was provided."+
        "\nDefault = default" + 
        "\nSpark = spark")