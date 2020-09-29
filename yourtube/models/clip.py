"""The sqlalchemy model for a clip."""
from sqlalchemy import Column, func
from sqlalchemy.types import DateTime, Integer, String

from yourtube.db import base


class Clip(base):

    __tablename__ = "clips"

    id = Column(String, primary_key=True)
    name = Column(String)
    creator_name = Column(String)
    published_at = Column(DateTime)

    # Debug time
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __init__(self, id, name, creator_name, published_at):
        self.id = id
        self.name = name
        self.creator_name = creator_name
        self.published_at = published_at