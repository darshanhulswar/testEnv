# Import os module to access environment variables
import os

# Get all environment variables and store in a dictionary
env_variables = os.environ

# Print each environment variable and its value
for key, value in env_variables.items():
    print(f"{key}: {value}")

# Print the value of TEST environment variable
print(f"TEST: {os.environ.get('TEST')}")