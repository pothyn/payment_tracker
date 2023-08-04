import json

def add_row():
    # Take in data
    print("Add")

def update_row():
    # Update data using ID
    print("Update")
    
def delete_row():
    # Delete data using ID
    print("Delete")
    
# Connect to Google Sheets or alternatively store locally in csv
# Both options potentially but Sheets would need payment?


# For Google Sheets implementation
def get_api_key():
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            return config["api_key"]
    except FileNotFoundError:
        print("Please enter an API Key for google sheets.")
        # NEED: A way to enter in the API Key
        
def update_config_file(api_key):
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        config["api_key"] = api_key
    with open("config.json", "w") as config_file:
        json.dump(config, config_file)


# Now you can use the API key in your code
api_key = get_api_key()

print(api_key)

# set MY_API_KEY_ENV_VARIABLE=your_api_key_here
# python your_script.py