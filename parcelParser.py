import os
import yaml

CONFIGURATION_FILE = "conf.yaml"
THRESHOLD_WEIGHT_NAME = "thresholdWeight"

class ParcelParser:
    def __init__(self):
        """Loads configuration yaml file"""
        try:
            configurationFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),CONFIGURATION_FILE)
            with open(configurationFilePath, 'r') as configFile:
                self.configuration = yaml.safe_load(configFile)
                self.thresholdWeight = self.configuration.get(THRESHOLD_WEIGHT_NAME)
        except FileNotFoundError:
            print(CONFIGURATION_FILE+ "is missing .....!")
        except Exception as error:
            print(error)

    def checkWeight(self, packageWeight):
        """ Checking Weight Compatability """
        if packageWeight > self.thresholdWeight:
            print('weight exceeded threshold!')
            return False
        else:
            print('weight validation completed!')
            return True
    
    def checkDimensions(self,packageDimensions):
        """ Checking Dimensions Compatability w.r.to packageTypes available"""
        response = dict.fromkeys(['packageType','cost'])
        for packageType in self.configuration.get('packages'):
            dimensionCounter = 0
            for key in list(packageDimensions.keys()):
                if list(packageType.values())[0][key] >= packageDimensions[key]:
                    dimensionCounter+=1
                    if dimensionCounter == len(list(packageDimensions.keys())):
                        #return {'packageType': list(packageType.keys())[0], 'cost':list(packageType.values())[0]['cost']}
                        response['packageType']= list(packageType.keys())[0]
                        response['cost']= list(packageType.values())[0]['cost']
                        return response
        return response
        
    
