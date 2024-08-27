from fastapi import FastAPI

from moon.router.agent import agent_router

""" 初始化FastAPI """
app = FastAPI()

""" 初始化路由 """
app.include_router(agent_router, prefix="/moon/agent", tags=["人机交互和工具调用等模型交互接口"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
