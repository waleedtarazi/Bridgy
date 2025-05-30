from fastapi import FastAPI, Header, HTTPException, Request
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/check-house")
def check_house(request: Request):
    headers = request.headers
    print(' -- > the header <--- ')
    print(headers)
    print(" headers TYPE ")
    print( type(headers) )
    number_of_adults = headers.get('number-of-adults')
    logging.info(f"API received with number_of_adults = {number_of_adults}")
    if int(number_of_adults) > 3:
        return {"can_have_house": "NO"}
    return {"can_have_house": "YES"}
