# -*- coding: utf-8 -*-
import os
import yaml
from enum import Enum

class PackageProps(Enum):
    LENGTH = 'length'
    BREADTH = 'breadth'
    HEIGHT = 'height'
    WEIGHT = 'weight'

DIMENSIONS = [PackageProps.LENGTH.value, PackageProps.BREADTH.value, PackageProps.HEIGHT.value]
DIMENSION_UNIT = 'packageDimensionUnit'
WEIGHTLIMIT = 'weightLimit'
COSTUNIT = 'packageCostUnit'
PACKAGE = ['packageType', 'cost']
OUTPUT = ["packageType", "cost", "exception"]


class ParcelParser:
    """ Parcel Analyzer Utility """

    def __init__(self, logger):
        """ Loads Configuration file when Object is initialized
        """
        try:
            ENV = os.getenv('ENV', 'DEV')
            self.logger = logger
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../", "conf", "configuration.yaml"), 'r') as configFile:
                self.configuration = yaml.safe_load(configFile)
            self.envConfig = self.configuration[ENV]
            
            self.thresholdWeight = self.envConfig.get(WEIGHTLIMIT)
            self.packageCostUnit = self.envConfig.get(COSTUNIT)
            self.packageDimensionUnit = self.envConfig.get(DIMENSION_UNIT)
            self.errors = self.envConfig.get('ERROR_RESPONSES')
        except FileNotFoundError:
            self.logger.critical("Configuration file is missing .....!")
        except Exception as error:
            self.logger.error(error)

    def checkWeight(self, packageWeight):
        """Validates/Checks input packageWeight with configurred Threshold Value
        Args:
            packageWeight (float): A decimal value
        Returns:
            Boolean: True, if Weight is below Threshold
        """
        try:
            if packageWeight <= self.thresholdWeight.get('value') and packageWeight > 0:
                self.logger.debug('weight validation completed!')
                return True
            else:
                self.logger.warning('weight is not in the expected range 0 to ' +
                                    str(self.thresholdWeight.get('value')) + ' ' + self.thresholdWeight.get('unit'))
                return False

        except TypeError:
            raise TypeError(self.errors['typeError'])
        except Exception as error:
            self.logger.error(error)

    def checkDimensions(self, packageDimensions):
        """User package dimensions are iterated against packages Available to suggest the best package
        Args:
            packageDimensions (dict): package dimensions as a Dictionary Object
        Returns:
            dict: package Type and Cost
        """
        try:
            if not all(isinstance(x, (int, float)) for x in list(packageDimensions.values())):
                self.logger.warning('Non-Numeric input detected!')
                raise TypeError('Non-Numeric Input package detected...!')

            outputObject = dict.fromkeys(PACKAGE)
            for package in sorted(self.envConfig.get('packages', []), key=lambda i: i['length']):
                dimensionCounter = 0
                dimensionsList = list(packageDimensions.keys())
                for key in dimensionsList:
                    if package[key] >= packageDimensions[key] and packageDimensions[key] > 0:
                        dimensionCounter += 1
                        if dimensionCounter == len(dimensionsList):
                            outputObject['packageType'] = package.get('type')
                            outputObject['cost'] = """{}{}""".format(self.packageCostUnit, package.get('cost'))
                            return outputObject

            outputObject['exception'] = self.errors['packageNotFound']
            return outputObject
        except TypeError:
            raise TypeError(self.errors['typeError'])
        except Exception as error:
            self.logger.error(error)

    def getpackageSolution(self, userInput):
        
        outputDict =dict.fromkeys(OUTPUT)
        fetchedDimensions = dict.fromkeys(DIMENSIONS)
        for key in fetchedDimensions:
            fetchedDimensions[key] = userInput[key]
        weightCheck = self.checkWeight(userInput.get('weight'))
        
        if weightCheck:
            self.logger.debug("userInput: {}".format(fetchedDimensions))
            outputDict.update(self.checkDimensions(fetchedDimensions))
        else:
            outputDict['weight'] = "Not Allowed"
            outputDict['exception']=self.errors.get('weightException').format(self.thresholdWeight.get('value'), self.thresholdWeight.get('unit'))
        return outputDict
