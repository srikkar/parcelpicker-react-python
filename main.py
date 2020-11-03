from parcelParser import ParcelParser

print ("++++++++++   Welcome to Parcel Expense Calculator   +++++++++++++")
userInput = {}
inputWeight = float(input ('Enter Package Weight (In Kgs): '))

ppObj = ParcelParser()
if ppObj.checkWeight(inputWeight):
    
    userInput['length'] = float(input ('Enter Package length (In mm): '))
    userInput['breadth'] = float(input ('Enter Package breadth (In mm): '))
    userInput['height'] = float(input ('Enter Package height (In mm): '))

    print(ppObj.checkDimensions(userInput))