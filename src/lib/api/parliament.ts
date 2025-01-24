const BILLS_API_BASE = 'https://bills-api.parliament.uk/api/v1';
const MEMBERS_API_BASE = 'https://members-api.parliament.uk/api/v1';

export type Bill = {
  billId: number;
  title: string;
  currentStage: {
    id: number;
    description: string;
  };
  lastUpdate: string;
};

export type Member = {
  id: number;
  nameDisplayAs: string;
  party: string;
  constituency?: string;
  currentPost?: string;
};

export async function getBills(): Promise<Bill[]> {
  const response = await fetch(`${BILLS_API_BASE}/Bills`);
  if (!response.ok) {
    throw new Error('Failed to fetch bills');
  }
  return response.json();
}

export async function getMembers(): Promise<Member[]> {
  const response = await fetch(`${MEMBERS_API_BASE}/Members`);
  if (!response.ok) {
    throw new Error('Failed to fetch members');
  }
  return response.json();
}

export async function getMember(id: number): Promise<Member> {
  const response = await fetch(`${MEMBERS_API_BASE}/Members/${id}`);
  if (!response.ok) {
    throw new Error('Failed to fetch member');
  }
  return response.json();
}