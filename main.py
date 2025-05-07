from fastapi import FastAPI, Header, HTTPException, Request
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/check-house")
def check_house(request: Request):
    headers = request.headers
    print(' -- > the header <--- ')
    print(header)
    print(" headers TYPE ")
    print( type(header) )
    number_of_adults = header.get('number_of_adults')
    logging.info(f"API received with number_of_adults = {number_of_adults}")
    if int(number_of_adults) > 3:
        return {"can_have_house": False}
    return {"can_have_house": True}
