from flask import  request, jsonify
from functools import wraps
import jwt
import datetime

class CustomJWT:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize the JWT extension with the Flask app.
        """
        self.app = app
        self.app.config.setdefault('JWT_SECRET_KEY', 'your-secret-key')  # Default secret key
        self.app.config.setdefault('JWT_ALGORITHM', 'HS256')  # Default algorithm
        self.app.config.setdefault('JWT_EXPIRATION_DELTA', datetime.timedelta(hours=1))  # Default expiration

    def create_access_token(self, identity):
        """
        Create a JWT token for the given identity (e.g., user ID or username).
        """
        payload = {
            'identity': identity,
            'exp': datetime.datetime.utcnow() + self.app.config['JWT_EXPIRATION_DELTA']
        }
        token = jwt.encode(payload, self.app.config['JWT_SECRET_KEY'], algorithm=self.app.config['JWT_ALGORITHM'])
        return token

    def validate_token(self, token):
        """
        Validate a JWT token and return the payload if valid.
        """
        try:
            payload = jwt.decode(token, self.app.config['JWT_SECRET_KEY'], algorithms=[self.app.config['JWT_ALGORITHM']])
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token has expired
        except jwt.InvalidTokenError:
            return None  # Token is invalid

    def jwt_required(self, f):
        """
        Decorator to ensure a valid JWT token is present in the request.
        """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"message": "Token is missing"}), 401

            # Remove 'Bearer ' prefix if present
            if token.startswith('Bearer '):
                token = token[7:]

            payload = self.validate_token(token)
            if not payload:
                return jsonify({"message": "Invalid or expired token"}), 401

            # Attach the payload to the request for use in the route
            request.current_user = payload
            return f(*args, **kwargs)
        return decorated_function