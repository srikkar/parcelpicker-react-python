from parcelParser import ParcelParser

print ("++++++++++   Welcome to Parcel packaging Solution   +++++++++++++")
def startApp():
    try:

        ppObj = ParcelParser()
        inputWeight = float(input ('Enter Package Weight (In '+ppObj.thresholdWeight.get('unit', 'Kgs')+'): '))
        if ppObj.checkWeight(inputWeight):
        
            userInput = {}
            print('Please enter Package Dimensions in (In '+ppObj.configuration.get('packageDimensionsUnit','mm')+')')
            userInput['length'] = float(input ('Enter Package length: '))
            userInput['breadth'] = float(input ('Enter Package breadth: '))
            userInput['height'] = float(input ('Enter Package height: '))
            packageSolution = ppObj.checkDimensions(userInput)
            print('Package Type: '+packageSolution.get('packageType'))
            print('Package Cost: '+ str(ppObj.packageCostUnit)+''+str(packageSolution.get('cost')))
    except Exception:
        print('Unexpected Input detected....!')
        print('Restarting App...')
        startApp()

if __name__ == "__main__":
    startApp()

