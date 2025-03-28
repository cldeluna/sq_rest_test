# Sample Generic Function for SuzieQ REST API

## Virtual environment setup
Install the following packages:
  - os
  - requests
  - python-dotenv


## Environment variables:
- SQ_API_TOKEN


## Tips for using this repository and script

The try_sq_rest_call function is my go to call.  

I have other functions (I provided an example of one I use to pull all the namespaces) that I use to craft the call itself as you see.
In the main function, i just call get_namespace_list.  
That function crafts the call to get the namespace list (basically namespace show in the CLI) and then calls the  try_sq_rest_call .  

The only changes you need to make are:
1. In line 54 of rest_test.py, update the API_ENDPOINT with your SuzieQ instance.
2. Rename .env_sample to .env
3. Update the variable SQ_API_TOKEN in .env with your token

Execute example: python rest_test.py (if it works you should see a list of the SuzieQ namespaces print out)


