import uvicorn as uv

from testproject.asgi import application

if __name__ == '__main__':
    uv.run(application)