#!/bin/bash
uvicorn main:asgi_app --host 192.168.0.112 --port 8000 --reload
