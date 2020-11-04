import os
import yaml

CONFIGURATION_FILE = "configuration.yaml"

class ParcelParser:
    """ Parcel Analyzer Utility """    
    def __init__(self, configurationFilePath=os.path.join(os.path.dirname(os.path.realpath(__file__)),"../","conf", CONFIGURATION_FILE)):
        """ Loads Configuration file when Object is initialized
        """
        try:
            ENV = os.getenv('ENV', 'DEV')
            with open(configurationFilePath, 'r') as configFile:
                self.configuration = yaml.safe_load(configFile)
                self.envConfig = self.configuration[ENV]
                self.thresholdWeight = self.envConfig.get('weightLimit')
                self.packageCostUnit = self.envConfig.get('packageCostUnit')
                self.packageDimensionUnit = self.envConfig.get('packageDimensionUnit')
                self.errors = self.envConfig.get('ERROR_RESPONSES')
        except FileNotFoundError:
            print(CONFIGURATION_FILE+ "is missing .....!")
        except Exception as error:
            print(error)

    def checkWeight(self, packageWeight):
        """Validates/Checks input packageWeight with configurred Threshold Value
        Args:
            packageWeight (float): A decimal value
        Returns:
            Boolean: True, if Weight is below Threshold
        """        
        try:
            if packageWeight > self.thresholdWeight.get('value'):
                print('weight exceeded limit i.e., '+ str(self.thresholdWeight.get('value'))+' '+ self.thresholdWeight.get('unit'))
                return False
            else:
                print('weight validation completed!')
                return True
        except TypeError:
            raise TypeError(self.errors['typeError']) 
        except Exception as error:
            print(error)    
            


    def checkDimensions(self,packageDimensions):        
        """User package dimensions are iterated against packages Available to suggest the best package
        Args:
            packageDimensions (dict): package dimensions as a Dictionary Object
        Returns:
            dict: package Type and Cost
        """
        try:
            if not all(isinstance(x, (int,float)) for x in list(packageDimensions.values())):
                print('Non-Standard input detected!')
                raise TypeError('Non-Standard Input package detected...!')

            outputObject = dict.fromkeys(['packageType','cost'])
            for package in sorted(self.envConfig.get('packages',[]), key = lambda i: i['length']):
                dimensionCounter = 0; dimensionsList = list(packageDimensions.keys())
                for key in dimensionsList:
                    if package[key] >= packageDimensions[key]:
                        dimensionCounter+=1
                        if dimensionCounter == len(dimensionsList):
                            outputObject['packageType']= package.get('type')
                            outputObject['cost']= """{}{}""".format(self.packageCostUnit, package.get('cost'))
                            return outputObject
            
            outputObject['exception'] = self.errors['packageNotFound']
            return outputObject
        except TypeError:
            raise TypeError(self.errors['typeError'])   
        except Exception as error:
            print(error)   