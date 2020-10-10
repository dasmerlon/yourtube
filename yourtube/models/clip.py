"""The sqlalchemy model for a clip."""
from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.orm import relationship

from yourtube.db import base


class Clip(base):

    __tablename__ = "clips"

    id = Column(String, primary_key=True)
    name = Column(String)
    creator_username = Column(
        String, ForeignKey("creators.username"), nullable=False, index=True
    )
    published_at = Column(DateTime)

    creator = relationship("Creator")

    # Debug time
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __init__(self, id, name, creator_username, published_at):
        self.id = id
        self.name = name
        self.creator_username = creator_username
        self.published_at = published_at