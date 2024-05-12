import requests

# Endpoint URL where the model is deployed
endpoint_url = "http://172.172.241.242:5000/"

def test_server(image_path):
    # Open the image file
    with open(image_path, "rb") as file:
        image_data = file.read()

    # Create the payload for the POST request
    payload = {"image": image_data}

    # Send the POST request to the server
    response = requests.post(endpoint_url, files=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the prediction returned by the server
        print("Prediction:", response.json())
    else:
        print("Error:", response.text)



# Path to the image file you want to test
image_path = "./test/M2.jpg"

# Call the test_server function with the image path
test_server(image_path)
