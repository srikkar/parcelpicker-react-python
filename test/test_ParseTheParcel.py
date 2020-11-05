import os
import sys
import unittest
import logging
import logging.config
LOG_FILE_NAME = 'logging.conf'
logging.config.fileConfig(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../conf", LOG_FILE_NAME))

# create logger
logger = logging.getLogger('PackageSolutionService')

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../'))
from utils import parcelParser


class packageSolutionTests(unittest.TestCase):
    
    def test_checkWeightWithinLimits_True(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        self.assertEqual(subject.checkWeight(20),True)
    

    def test_checkWeightWithinLimits_False(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        self.assertEqual(subject.checkWeight(29),False)

    
    def test_checkWeight_BoundaryValue_True(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        self.assertEqual(subject.checkWeight(25),True)
    
    def test_checkWeight_NonStandardInputs_TypeError(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        with self.assertRaises(TypeError):
            subject.checkWeight('hello')
    
    def test_checkDimensions_NonStandardInputs_TypeError(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 110, 'breadth': '300', 'height': 150}
        with self.assertRaises(TypeError):
            subject.checkDimensions(userInput)
    
    def test_checkDimensions_StandardInputs_dictObject(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 110, 'breadth': 300, 'height': 150}
        self.assertIsInstance(subject.checkDimensions(userInput),dict)
    
    def test_checkDimensions_Inputs_small(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 110, 'breadth': 300, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Small')

    def test_checkDimensions_Inputs_Medium(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 300, 'breadth': 300, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Medium')

    def test_checkDimensions_Inputs_Large(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 100, 'breadth': 500, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Large')
    
    def test_checkDimensions_Inputs_ExceededLimits(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 300, 'breadth': 300, 'height': 350}
        self.assertEqual(subject.checkDimensions(userInput)['exception'],subject.errors['packageNotFound'])
    
    def test_checkDimensions_Inputs_NonRealZERO(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 300, 'breadth': 0, 'height': 350}
        self.assertEqual(subject.checkDimensions(userInput)['exception'],subject.errors['packageNotFound'])

    def test_getpackageSolution_Inputs_weightInLimit(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 300, 'breadth': 0, 'height': 350, 'weight': 20}
        self.assertIsInstance(subject.getpackageSolution(userInput),dict)
    
    def test_getpackageSolution_Inputs_weightExceededLimit(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': 300, 'breadth': 0, 'height': 350, 'weight': 30}
        self.assertIsInstance(subject.getpackageSolution(userInput),dict)
    
    def test_getpackageSolution_Inputs_Strings(self):
        
        subject = parcelParser.ParcelParser(logger=logger)
        userInput = {'length': '300', 'breadth': 'hello', 'height': 'hi', 'weight': '0'}
        self.assertIsInstance(subject.getpackageSolution(userInput),dict)


            
        
    
        