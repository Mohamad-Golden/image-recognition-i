import re
from pathlib import Path

import uvicorn
from fastapi import Body, FastAPI

app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent


@app.post("/rs")
def receive_sms(text: str = Body(embed=True)):
    criteria = re.search(r"خودرو", text)
    if criteria:
        code_re = re.search(r"\d{5,}", text)
        code = code_re.group(0)
        with open(BASE_DIR / "sms.txt", "w") as f:
            f.write(code)
    return {}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
