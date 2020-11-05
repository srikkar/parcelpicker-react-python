# Parse the Parcel #

At Trade Me we're looking to make selling items even easier and so we've decided to build our very own package shipping network. We've dug a tunnel between the North and South Islands that enables us to offer the same rates for parcels sent anywhere in the country, and we've just finished fueling up our fleet of courier vans; all that remains to be done is to update the website so that users can be advised how much their items will cost to send.

Our new service shipping costs are based on size and we offer different prices for small, medium, and large boxes. Unfortunately we're currently unable to move heavy packages so we've placed an upper limit of 25kg per package.

| Package Type | Length | Breadth | Height | Cost |
| ------------ | ------ | ------- | ------ | ---- |
| Small | 200mm | 300mm | 150mm | $5.00 |
| Medium | 300mm | 400mm | 200mm| $7.50 |
| Large | 400mm | 600mm | 250mm | $8.50 |

## Coding Exercise ##

We need you to implement a component that, when supplied the dimensions (length x breadth x height) and weight of a package, can advise on the cost and type of package required. If the package exceeds these dimensions - or is over 25kg - then the service should not return a packaging solution.

### Guidelines ###

You will be expected to produce a solution that solves the above problem. While this is a simple component we would expect it demonstrate anything you’d normally require for a production ready and supportable solution - so think about standards, legibility, robustness, reuse etc. What we don’t require is a fancy user interface - a simple **command line** or **test harness** will suffice. 

You are free to choose how you implement the solution though your choices should ideally align with your skills and the role you are applying for. You are welcome to make assumptions about the solution along with any improvements you think enhance or add value to the solution - though please be aware of the original scope.

### Submissions ###

We will send you an invite to this git repository. Please **fork** this repository, where you can commit or upload your code. Once finished please create a **pull request** and we will review your code. We normally expect to hear back from you within five working days. 

Best of luck, and we look forwards to your response!


### Installing / Getting started ###
A quick introduction of the minimal setup you need to get the Package Solution up & running.
Note: Python 3+ version is required  

1. Clone the Project
```sh
git clone <PROJECT_GIT_URL>
```
2. Create and Activate virtual environment 
```sh
python -m venv virtual_env
source ~/virtual_env/bin/activate
pip install -r requirements.txt
```

3. To host the Solution as webservice
```sh
 cd <Project-directory>/
 python app.py
```   

4. To run the module in Commandline
```sh
 cd <Project-directory>/
 python main.py
```

5. _Optional_   
**Import** postman [misc/ParcelParser.postman_collection.json] file to hit the APIs pre-configurred   
(_listed below in API reference section_)   
Commandline to set the Environment, defaults to DEV (if not provided)
```sh
export ENV=PROD
```

### Developing ###

**Built with** Python 3.7.9 version.   
Packages required are listed in requirements.txt 

### Configuration ###
configuration files are placed under conf directory
configurrable Properties are:
- package types
- dimensions & Unit
- Currency & Unit
- Weight Limit & Unit
- Error Responses
_Also, all the Above are configurrable w.r.to Environments_



### Tests ###
Unit TestCases are defined in test directory .py file(s). 
These tests would ensure if the Module is running in the expected mode.
In case of any code changes, please ensure to run the test cases to see [100% pass] result in the Console
```sh
pytest -v ./test/*.py
```

### Style Guide ###
To Develop ParseTheParcel utility, have taken the Object oriented methodology.
solution is placed in utils package.
Have de-coupled the validators
1. Weight -  To check only weight, returns if it's allowed or not
2. Dimensions - To check only Dimensions, returns suitable package
3. Wrapper method - which takes combined Input to provide Suitable package   

returns corresponding responses based on the Values available in configuration yaml file

_Corresponding Configurations are fetched based on Environment Variable [ENV]_

RESTFul webservice is developed using Python-Flask

### API reference ###

Once the Service is UP, below resources are available from the Service

#### Check if Service is live
Resource [http://127.0.0.1:8001/parseTheParcel/checkAlive](http://127.0.0.1:8001/parseTheParcel/checkAlive)  
**Method:** [GET]
###### Response
```json
{
    "status": "live"
}
```

#### Submit metric for Package Solution 
Resource [http://127.0.0.1:8001/parseTheParcel/packageSolution](http://127.0.0.1:8001/parseTheParcel/packageSolution)  
**Method:** [POST]
###### Request
```json
{
	"length": 100,
    "height" : 20,
	"breadth": 210,
	"weight": 22
}
```

###### Response
```json
{
    "packageType": "Small",
    "cost": "$5.0",
    "exception": null
}
```

#### Checks Weight of the Package against Limit
Resource [http://127.0.0.1:8001/parseTheParcel/checkWeight](http://127.0.0.1:8001/parseTheParcel/checkWeight)  
**Method:** [POST]
###### Request
```json
{
    "weight": 23
}
```
###### Response
```json
{
    "message": "Allowed"
}
```

#### Get Weight Limit
Resource [http://127.0.0.1:8001/parseTheParcel/weightLimit](http://127.0.0.1:8001/parseTheParcel/weightLimit)  
**Method:** [GET]
###### Response
```json
{
    "weightLimit": 25,
    "unit": "Kgs"
}
```

#### Get package types Available
Resource [http://127.0.0.1:8001/parseTheParcel/packageTypes](http://127.0.0.1:8001/parseTheParcel/packageTypes)  
**Method:** [GET]
###### Response
```json
{
    "packages": [
        {
            "type": "Medium",
            "length": 300,
            "breadth": 400,
            "height": 200,
            "cost": 7.5
        },
        {
            "type": "Large",
            "length": 400,
            "breadth": 600,
            "height": 250,
            "cost": 8.5
        },
        {
            "type": "Small",
            "length": 200,
            "breadth": 300,
            "height": 150,
            "cost": 5.0
        }
    ],
    "unit": "mm"
}
```

