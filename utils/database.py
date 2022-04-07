import os

from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    def __init__(self):
        self.mongo = AsyncIOMotorClient(os.getenv('mongo'))
        self.db = self.mongo['parcelbot']

