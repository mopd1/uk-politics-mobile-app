import requests
from typing import List, Dict, Optional
from datetime import datetime

class ParliamentBillsAPI:
    def __init__(self, base_url: str = "https://bills-api.parliament.uk/api/v1"):
        self.base_url = base_url

    async def get_bills(self) -> List[Dict]:
        """Fetch all current bills from Parliament API"""
        response = requests.get(f"{self.base_url}/Bills")
        response.raise_for_status()
        return response.json()

    async def get_bill_by_id(self, bill_id: int) -> Dict:
        """Fetch specific bill details"""
        response = requests.get(f"{self.base_url}/Bills/{bill_id}")
        response.raise_for_status()
        return response.json()

    async def get_bill_stages(self, bill_id: int) -> List[Dict]:
        """Fetch stages of a specific bill"""
        response = requests.get(f"{self.base_url}/Bills/{bill_id}/Stages")
        response.raise_for_status()
        return response.json()

    async def get_bill_publications(self, bill_id: int) -> List[Dict]:
        """Fetch publications related to a bill"""
        response = requests.get(f"{self.base_url}/Bills/{bill_id}/Publications")
        response.raise_for_status()
        return response.json()