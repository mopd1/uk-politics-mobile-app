from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.parliament_bills_api import ParliamentBillsAPI
from api.parliament_members_api import ParliamentMembersAPI
from typing import List, Dict

app = FastAPI(title="UK Politics Mobile App API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize API clients
bills_api = ParliamentBillsAPI()
members_api = ParliamentMembersAPI()

@app.get("/")
async def read_root():
    return {"message": "UK Politics Mobile App API"}

@app.get("/bills/")
async def get_bills() -> List[Dict]:
    try:
        return await bills_api.get_bills()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bills/{bill_id}")
async def get_bill(bill_id: int) -> Dict:
    try:
        return await bills_api.get_bill_by_id(bill_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/members/")
async def get_members(house: str = "Commons") -> List[Dict]:
    try:
        return await members_api.get_members(house)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/members/{member_id}")
async def get_member(member_id: int) -> Dict:
    try:
        return await members_api.get_member_by_id(member_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/members/{member_id}/votes")
async def get_member_votes(member_id: int) -> List[Dict]:
    try:
        return await members_api.get_member_voting_record(member_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)