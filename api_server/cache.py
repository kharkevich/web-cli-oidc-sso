import redis

from api_server.config import Config

redis_client = redis.Redis(
    host=Config.redis_host,
    port=Config.redis_port,
    password=Config.redis_password,
    db=Config.redis_db,
    decode_responses=True,
)
