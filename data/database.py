import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
# Use the service_role key if this backend needs to bypass RLS policies
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in .env")

# Initialize a single client instance
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# FastAPI Dependency
def get_db() -> Client:
    return supabase