import os
import yaml

CONFIGURATION_FILE = "conf.yaml"

class ParcelParser:
    """ Parcel Analyzer Utility """    
    def __init__(self):
        """ Loads Configuration file when Object is initialized
        """
        try:
            configurationFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),CONFIGURATION_FILE)
            with open(configurationFilePath, 'r') as configFile:
                self.configuration = yaml.safe_load(configFile)
                self.thresholdWeight = self.configuration.get('weightLimit')
                self.packageCostUnit = self.configuration.get('packageCostUnit')
                self.packageDimensionUnit = self.configuration.get('packageDimensionUnit')
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
            raise TypeError('Numeric Input expected!')   
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

            response = dict.fromkeys(['packageType','cost'])
            for package in sorted(self.configuration.get('packages',[]), key = lambda i: i['length']):
                dimensionCounter = 0; dimensionsList = list(packageDimensions.keys())
                for key in dimensionsList:
                    if package[key] >= packageDimensions[key]:
                        dimensionCounter+=1
                        if dimensionCounter == len(dimensionsList):
                            response['packageType']= package.get('type')
                            response['cost']= package.get('cost')
                            return response
            return response
        except TypeError:
            raise TypeError('Numeric Input expected!')   
        except Exception as error:
            print(error)   