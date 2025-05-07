from fastapi import FastAPI, Header, HTTPException
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/check-house")
def check_house(number_of_adults: str = Header(...)):
    print(f"Received number_of_adults: {number_of_adults}")
    logging.info(f"API received with number_of_adults = {number_of_adults}")
    if number_of_adults > 3:
        return {"can_have_house": False}
    return {"can_have_house": True}
