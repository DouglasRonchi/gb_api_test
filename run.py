import uvicorn

from app.main import app
from app.utils.authentication import generate_token

if __name__ == "__main__":
    print(generate_token())
    uvicorn.run(app, host="127.0.0.1", port=8000)
