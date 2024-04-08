0x16. API advanced
..................

Resources
--------
Read or watch:
-------------

. Reddit API Documentation - https://www.reddit.com/dev/api/
. Query String - https://en.wikipedia.org/wiki/Query_string


Learning Objectives
-------------------
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
-------
a) How to read API documentation to find the endpoints you’re looking for
....................................................................
Reading API documentation can be daunting at first, but with some practice and understanding of the typical structure, you can quickly find the endpoints you're looking for. Here's a step-by-step guide:

1. **Identify the Base URL**: This is the starting point for all API requests. It's often mentioned at the beginning of the documentation or in a prominent location. It typically looks like `https://api.example.com`.

2. **Understand Authentication**: Determine if the API requires authentication, and if so, what type (e.g., API key, OAuth token). This information is usually in the authentication section of the documentation.

3. **Browse Endpoints or Routes**: Look for sections or headings in the documentation that discuss endpoints, routes, or resources. These are usually organized logically based on the functionality they provide. For example, you might find sections like "User Management", "Products", or "Orders".

4. **HTTP Methods**: Each endpoint will support one or more HTTP methods (GET, POST, PUT, DELETE, etc.). Understand what each method does:
   - **GET**: Retrieve data.
   - **POST**: Create new data.
   - **PUT**: Update existing data.
   - **DELETE**: Remove data.

5. **Endpoint URLs**: Pay attention to the structure of endpoint URLs. They often follow a pattern. For example:
   - `GET /users`: Retrieve a list of users.
   - `GET /users/{id}`: Retrieve a specific user by ID.
   - `POST /users`: Create a new user.
   - `PUT /users/{id}`: Update a specific user.
   - `DELETE /users/{id}`: Delete a specific user.

6. **Request Parameters**: Endpoints may accept parameters in the URL, query string, or request body. These parameters can be used to filter, sort, or customize the results. Look for documentation on parameters such as query parameters, path parameters, headers, and request bodies.

7. **Response Format**: Understand the format of the response returned by each endpoint. This includes the HTTP status codes and the structure of the response body. Typically, the documentation will provide examples of both successful and error responses.

8. **Error Handling**: Pay attention to how errors are handled and what error codes may be returned. This will help you troubleshoot issues when interacting with the API.

9. **Rate Limiting**: Check if the API has any rate limits or usage restrictions. This information is crucial to avoid getting blocked or throttled.

10. **SDKs and Libraries**: Some APIs offer SDKs or libraries in various programming languages to make integration easier. These often come with documentation and code examples that can help you get started quickly.

By following these steps and familiarizing yourself with the structure of API documentation, you'll be able to efficiently locate the endpoints you need and understand how to interact with them.

-------------------------------------------------------------------

How to use an API with pagination
.................................


Pagination is a common technique used by APIs to manage large sets of data by breaking them into smaller, more manageable chunks. Here's how you can use an API with pagination:

1. **Understand Pagination Parameters**: Most APIs that support pagination will have parameters that allow you to control the pagination behavior. These parameters typically include:
   - `page` or `offset`: Specifies which page of results to retrieve.
   - `limit` or `per_page`: Specifies the number of results to include per page.

2. **Make an Initial Request**: Start by making an initial request to the API endpoint you're interested in, specifying the pagination parameters. For example:
   ```
   GET /api/resource?page=1&per_page=10
   ```

3. **Receive Response**: The API will respond with a subset of the total data, along with metadata indicating the total number of results and possibly links to the next and previous pages.

4. **Process the Response**: Process the data returned in the response according to your application's needs. Typically, this involves displaying the data to the user or performing further operations on it.

5. **Check for Pagination Metadata**: Check the metadata included in the response to see if there are additional pages of data available. Common pagination metadata includes:
   - `total`: Total number of results available.
   - `next_page`: Link to the next page of results, if available.
   - `prev_page`: Link to the previous page of results, if available.

6. **Retrieve Additional Pages**: If there are more pages of data available, make additional requests to retrieve them using the appropriate pagination parameters. For example:
   ```
   GET /api/resource?page=2&per_page=10
   ```

7. **Continue Pagination**: Repeat steps 3-6 until you have retrieved all the data you need or reached a predetermined stopping point.

8. **Handle Errors and Edge Cases**: Be sure to handle edge cases such as reaching the end of the dataset or encountering errors gracefully. This may involve checking for null or empty values in the pagination metadata and handling errors returned by the API.

By following these steps, you can effectively use an API with pagination to retrieve large sets of data in a controlled and efficient manner.
-------------------------------------------------------------
How to parse JSON results from an API
....................................
Parsing JSON results from an API involves converting the JSON data received from the API into a format that your programming language can work with, such as objects, arrays, or dictionaries. Here's a general guide on how to parse JSON results:

1. **Retrieve JSON Data**: Make a request to the API endpoint using a library or tool that can handle HTTP requests. This could be libraries like `requests` in Python, `fetch` in JavaScript, or similar tools in other programming languages.

2. **Receive JSON Response**: The API will respond with JSON data. This data may represent a single object, an array of objects, or a more complex structure.

3. **Decode JSON Data**: Use a JSON parsing library provided by your programming language to decode the JSON data into a native data structure. Most modern programming languages have built-in or third-party libraries for parsing JSON.

    - In Python, you can use the `json` module:
        ```python
        import json

        json_data = '{"key": "value"}'
        parsed_data = json.loads(json_data)
        ```

    - In JavaScript, you can use the `JSON.parse()` method:
        ```javascript
        const jsonString = '{"key": "value"}';
        const parsedData = JSON.parse(jsonString);
        ```

4. **Access Parsed Data**: Once the JSON data is parsed, you can access its elements as you would with any other data structure in your programming language. For example, in Python:
    ```python
    print(parsed_data['key'])
    ```

5. **Iterate Over Arrays**: If the JSON data represents an array of objects, you'll typically iterate over the array to access each object individually. For example, in Python:
    ```python
    for item in parsed_data:
        print(item['key'])
    ```

6. **Handle Errors**: JSON parsing can fail if the data is not properly formatted. Be sure to handle errors gracefully by catching exceptions or checking for errors in the response before attempting to parse the data.

By following these steps, you can effectively parse JSON results from an API and work with the data in your application.
---------------------------------------------
How to make a recursive API call
................................
Making a recursive API call involves repeatedly calling the API endpoint until a certain condition is met. This is commonly used when dealing with paginated data or when you need to fetch data recursively based on some criteria. Here's a general approach to making recursive API calls:

1. **Define Recursive Function**: Create a function that will make the API call and handle the response. This function should have parameters that allow it to control the recursion, such as the current page number or any other necessary parameters.

2. **Make API Call**: Inside the recursive function, make the API call to the desired endpoint. Include any necessary parameters, such as pagination parameters, in the request.

3. **Handle Response**: Process the response returned by the API call. This may involve parsing the JSON data, extracting relevant information, and performing any required operations on it.

4. **Check Termination Condition**: Determine whether the recursion should continue based on the response received. This could involve checking if there are more pages of data to fetch, if a certain condition has been met, or if an error has occurred.

5. **Recursively Call Function**: If the termination condition has not been met, recursively call the function again with updated parameters. This typically involves incrementing a page number or updating other parameters as necessary.

6. **Base Case**: Define a base case that stops the recursion. This could be reaching the end of the dataset, encountering an error, or meeting a specific condition.

Here's a Python example demonstrating a recursive API call to fetch paginated data:

```python
import requests

def fetch_data(page=1):
    url = f"https://api.example.com/data?page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        process_data(data)
        # Check if there are more pages to fetch
        if data.get('next_page'):
            fetch_data(page + 1)  # Recursively call function with next page number
    else:
        print(f"Error fetching data: {response.status_code}")

def process_data(data):
    # Process the data here
    pass

# Start the recursive API call
fetch_data()
```

In this example, the `fetch_data` function recursively calls itself with an incremented page number until there are no more pages to fetch. The `process_data` function is called to handle the data returned by each API call.
---------------------------------------------------------------
How to sort a dictionary by value
................................
To sort a dictionary by its values in Python, you can use the `sorted()` function along with a custom sorting key. Here's how you can do it:

```python
# Define a sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

# Sort the dictionary by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Print the sorted dictionary
print(sorted_dict)
```

In this code:

- `sorted()` function is used to sort the dictionary items.
- `my_dict.items()` returns a list of key-value pairs `(key, value)` from the dictionary.
- `key=lambda item: item[1]` specifies a custom sorting key, where `item[1]` represents the value of each key-value pair.
- The resulting sorted list of tuples is then converted back into a dictionary using the `dict()` constructor.

This will output the dictionary sorted by its values:

```
{'banana': 2, 'grape': 3, 'apple': 5, 'orange': 8}
```

If you want to sort the dictionary in descending order, you can add the `reverse=True` parameter to the `sorted()` function:

```python
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
``` 

This would sort the dictionary by values in descending order.
--------------------------------------------------------------
