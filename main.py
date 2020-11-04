from utils import parcelParser

print ("++++++++++   Welcome to Parcel packaging Solution   +++++++++++++")
def startApp():
    try:

        packageSolutionObj = parcelParser.ParcelParser()
        inputWeight = float(input ('Enter Package Weight (In '+packageSolutionObj.thresholdWeight.get('unit', 'Kgs')+'): '))
        if packageSolutionObj.checkWeight(inputWeight):
        
            userInput = {}
            print('Please enter Package Dimensions in (In '+packageSolutionObj.configuration.get('packageDimensionsUnit','mm')+')')
            userInput['length'] = float(input ('Enter Package length: '))
            userInput['breadth'] = float(input ('Enter Package breadth: '))
            userInput['height'] = float(input ('Enter Package height: '))
            packageSolution = packageSolutionObj.checkDimensions(userInput)
            print('Package Type: '+packageSolution.get('packageType'))
            print('Package Cost: '+ str(packageSolutionObj.packageCostUnit)+''+str(packageSolution.get('cost')))
    except Exception:
        print('Unexpected Input detected....!')
        print('Restarting App...')
        startApp()

if __name__ == "__main__":
    startApp()

