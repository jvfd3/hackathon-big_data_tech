import requests

def get_zipcode_data(zipcode, country_code='us'):
  """
  Fetches data for a given zipcode using the Zippopotam.us API.

  Args:
    zipcode (str): The zipcode to look up.
    country_code (str): The country code (default is 'us').

  Returns:
    dict: The API response as a dictionary, or None if not found.
  """
  url = f"http://api.zippopotam.us/{country_code}/{zipcode}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None

# Example usage:
if __name__ == "__main__":
  zipcode_1 = 8107
  zipcode_2 = 90920
  data = get_zipcode_data(zipcode_2)
  
  if data:
    print(data)
  else:
    print("No data found for the given zipcode.")