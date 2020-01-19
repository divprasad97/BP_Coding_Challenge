# Coding Test for George Chandler, BP
# Description: Simple Azure Function that outputs "Hello World!" when called

import logging
import azure.functions as func

# Main method - Does not take any input parameters, simply outputs given string 
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(f"Hello World!")
