import uvicorn
from asgiref.wsgi import WsgiToAsgi
from app import create_app
app=create_app()

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    uvicorn.run(asgi_app, host="127.0.0.1", port=8000, log_level="debug", reload=True)