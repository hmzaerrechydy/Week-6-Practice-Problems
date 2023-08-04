Link: https://cs50.harvard.edu/x/2023/problems/6/


# Seven Day Averages



```Python
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)
```

### requests.get()

An HTTP GET request is used to retrieve data from the specified resource, such as a website.


### response.content

Python requests are generally used to fetch the content from a particular resource, whenever we make an HTTP GET request, it returns a response object, this response object would be used to access certain features such as content, headers, etc. 


### decode()

This method is used to convert from one encoding scheme to another. 


### splitlines()

Split a string into a list where each line is a list item. 

The DictReader() is used to read the file of the csv in the format of the dict object.
