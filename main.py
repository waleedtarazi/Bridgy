from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/check-house")
def check_house(number_of_adults: int = Header(...)):
    if number_of_adults > 3:
        return {"can_have_house": False}
    return {"can_have_house": True}
