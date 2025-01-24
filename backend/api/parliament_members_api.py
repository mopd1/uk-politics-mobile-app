import requests
from typing import List, Dict, Optional
from datetime import datetime

class ParliamentMembersAPI:
    def __init__(self, base_url: str = "https://members-api.parliament.uk/api/v1"):
        self.base_url = base_url

    async def get_members(self, house: str = "Commons") -> List[Dict]:
        """Fetch all current members from specified house"""
        params = {"House": house}
        response = requests.get(f"{self.base_url}/Members", params=params)
        response.raise_for_status()
        return response.json()

    async def get_member_by_id(self, member_id: int) -> Dict:
        """Fetch specific member details"""
        response = requests.get(f"{self.base_url}/Members/{member_id}")
        response.raise_for_status()
        return response.json()

    async def get_member_voting_record(self, member_id: int) -> List[Dict]:
        """Fetch voting record for a specific member"""
        response = requests.get(f"{self.base_url}/Members/{member_id}/Votes")
        response.raise_for_status()
        return response.json()

    async def get_member_speeches(self, member_id: int) -> List[Dict]:
        """Fetch recent speeches by a member"""
        response = requests.get(f"{self.base_url}/Members/{member_id}/Speeches")
        response.raise_for_status()
        return response.json()

    async def search_members(self, query: str) -> List[Dict]:
        """Search for members by name or constituency"""
        params = {"SearchTerm": query}
        response = requests.get(f"{self.base_url}/Members/Search", params=params)
        response.raise_for_status()
        return response.json()