#!/bin/bash
uvicorn main:asgi_app  --host 0.0.0.0 --port 9000 --reload

