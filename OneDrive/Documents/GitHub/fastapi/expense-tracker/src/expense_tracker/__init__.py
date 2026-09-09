import uvicorn


def main() -> None:
    uvicorn.run("main:app", reload=True)
