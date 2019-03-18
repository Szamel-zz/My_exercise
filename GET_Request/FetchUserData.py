import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get Request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)
print(response.headers)

# Validate Status Code
print(response.status_code)
assert response.status_code == 200
#assert response.status_code == 201 #AssertionError

# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

# Fetch Elapsed Time
print(response.elapsed)

# Fetch Response Content
print(response.content)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 4
first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name[0])

for i in range(3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])










