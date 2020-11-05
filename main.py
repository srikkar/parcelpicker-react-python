# -*- coding: utf-8 -*-
import logging
import logging.config
import os
LOG_FILE_NAME = 'logging.conf'
logging.config.fileConfig(os.path.join(os.path.dirname(os.path.realpath(__file__)),"conf", LOG_FILE_NAME))

# create logger
logger = logging.getLogger('PackageSolution')
from utils import parcelParser

logger.info("++++++++++   Welcome to Parcel packaging Solution   +++++++++++++")
def validateNumber(userInput):
    try:
        inputNumber = float(userInput)
        if isinstance(inputNumber, (float)):
            if inputNumber > 0 :
                return inputNumber
        raise ValueError
    except Exception as e:
        logger.error(e)
        raise ValueError

def startApp():
    try:
        packageSolutionObj = parcelParser.ParcelParser(logger=logger)
        userInput = {}
        userInput['weight'] = validateNumber(input ('Enter Package Weight (In '+packageSolutionObj.thresholdWeight.get('unit', 'Kgs')+'): '))
        
        logger.info('Please enter Package Dimensions in (In '+packageSolutionObj.configuration.get('packageDimensionsUnit','mm')+')')
        userInput['length'] = validateNumber(input ('Enter Package length: '))
        userInput['breadth'] = validateNumber(input ('Enter Package breadth: '))
        userInput['height'] = validateNumber(input ('Enter Package height: '))
        packageSolution = packageSolutionObj.getpackageSolution(userInput)
        logger.info('Package Type: '+str(packageSolution.get('packageType')))
        logger.info('Package Cost: '+str(packageSolution.get('cost')))
        exceptionMsg = packageSolution.get('exception')
        logger.info('Thank You!') if not exceptionMsg else logger.info('EXCEPTION: {}'.format(packageSolution.get('exception')))
    except ValueError as e:
        logger.error(e)
        logger.error('Unexpected Input detected....!')
        logger.info('Restarting App...')
        startApp()

    except Exception as e:
        logger.error(e)
        

if __name__ == "__main__":
    startApp()
