# Homework 05: Undone (The Sweater Container)

## Overview

Homework 05 has us modify homework 04's python script, `iss_tracker.py`, to include two
new routes, `/help`, `/delete-data`, and `/post-data`, while also adding query parameters
to the already existing route, /epochs. 

### New Routes

1. `/help` - this route will return information regarding all the routes listed
in the file.  
2. `/delete-data` - this route will delete the data uploaded from the xml file created by NASA to track the ISS trajectory using the `DELETE` method. 
3. `/post-data` - this route will reinstate the previously deleted data using the 'POST' method


### Modified Routes
The route `/epochs` has been modified to account for two query parameters: offset and limit. 

1. The offset parameter will indicate which epoch should be listed first. For example, 
if the user inputs 1994 as the offset value, the file will return epochs and their values
from the year 1994 and onward. 

2. The limit parameter indicates how many epoch values the user wants returned. If the user 
inputs a value of 3, the file will return a maximum of 3 epochs. 

## Instructions
This file has been written while keeping the Flask App in mind. 
In one terminal, please clone this repository and run the file using the command 
`flask --app iss_tracker --debug run`. In a separate terminal, please use the command
`curl localhost:5000[route]`. 

### Calling Routes
The first route `curl localhost:5000/` will return all the data in the XML file as >Below is an example of what the data returned should look like:

```
 {
                "EPOCH": "2023-063T12:00:00.000Z",
                "X": {
                  "#text": "2820.04422055639",
                  "@units": "km"
                },
                "X_DOT": {
                  "#text": "5.0375825820999403",
                  "@units": "km/s"
                },
                "Y": {
                  "#text": "-5957.89709645725",
                  "@units": "km"
                },
                "Y_DOT": {
                  "#text": "0.78494316057540003",
                  "@units": "km/s"
                },
                "Z": {
                  "#text": "1652.0698653803699",
                  "@units": "km"
                },
                "Z_DOT": {
                  "#text": "-5.7191913150960803",
                  "@units": "km/s"
                }
              }
            ]
 },
          "metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-048T12:00:00.000Z",
            "STOP_TIME": "2023-063T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-049T01:38:49.191Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```

The second route `curl localhost:5000/epochs` will only display only all the epochs:
```
"2023-063T11:19:00.000Z",
  "2023-063T11:23:00.000Z",
  "2023-063T11:27:00.000Z",
  "2023-063T11:31:00.000Z",
  "2023-063T11:35:00.000Z",
  "2023-063T11:39:00.000Z",
  "2023-063T11:43:00.000Z",
  "2023-063T11:47:00.000Z",
  "2023-063T11:51:00.000Z",
  "2023-063T11:55:00.000Z",
  "2023-063T11:59:00.000Z",
  "2023-063T12:00:00.000Z"
]
```
However, with the new modifications, if the user has specified an offset and limit parameter of 2 and 5 respectively, the following would be the output:
`
[
  "2023-063T11:23:00.000Z",
  "2023-063T11:27:00.000Z",
  "2023-063T11:31:00.000Z",
  "2023-063T11:35:00.000Z",
  "2023-063T11:39:00.000Z",
]
`
The third route `curl localhost:5000/epochs/<epoch>` will return the data for one s>When using the command `curl localhost:5000/epochs/2023-063T11:27:00.000Z`

```
{
  "EPOCH": "2023-063T11:27:00.000Z",
  "X": -5254.8392497479,
  "X_DOT": -0.59440880720024,
  "Y": 3114.55097873129,
  "Y_DOT": -5.78052149060741,
  "Z": 2961.7924901551,
  "Z_DOT": 5.00312313061336
}
```
The last route will return the velocity calculated at the specific epoch. Using the>`
7.6680500515795895
`dw
