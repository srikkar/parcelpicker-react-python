import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../'))
from utils import parcelParser

class packageSolutionTests(unittest.TestCase):
    
    def test_checkWeightWithinLimits_True(self):
        
        subject = parcelParser.ParcelParser()
        self.assertEqual(subject.checkWeight(20),True)
    

    def test_checkWeightWithinLimits_False(self):
        
        subject = parcelParser.ParcelParser()
        self.assertEqual(subject.checkWeight(29),False)

    
    def test_checkWeight_BoundaryValue_True(self):
        
        subject = parcelParser.ParcelParser()
        self.assertEqual(subject.checkWeight(25),True)
    
    def test_checkWeight_NonStandardInputs_TypeError(self):
        
        subject = parcelParser.ParcelParser()
        with self.assertRaises(TypeError):
            subject.checkWeight('hello')
    
    def test_checkDimensions_NonStandardInputs_TypeError(self):
        
        subject = parcelParser.ParcelParser()
        userInput = {'length': 110, 'breadth': '300', 'height': 150}
        with self.assertRaises(TypeError):
            subject.checkDimensions(userInput)
    
    def test_checkDimensions_StandardInputs_dictObject(self):
        
        subject = parcelParser.ParcelParser()
        userInput = {'length': 110, 'breadth': 300, 'height': 150}
        self.assertIsInstance(subject.checkDimensions(userInput),dict)
    
    def test_checkDimensions_Inputs_small(self):
        
        subject = parcelParser.ParcelParser()
        userInput = {'length': 110, 'breadth': 300, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Small')

    def test_checkDimensions_Inputs_Medium(self):
        
        subject = parcelParser.ParcelParser()
        userInput = {'length': 300, 'breadth': 300, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Medium')

    def test_checkDimensions_Inputs_Large(self):
        
        subject = parcelParser.ParcelParser()
        userInput = {'length': 100, 'breadth': 500, 'height': 150}
        self.assertEqual(subject.checkDimensions(userInput)['packageType'],'Large')


            
        
    
        