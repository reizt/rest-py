from dotenv import load_dotenv

load_dotenv()

from app import create_app  # noqa: E402 -- to load .env in advance

app = create_app()
