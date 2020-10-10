"""The sqlalchemy model for a creator."""
from sqlalchemy import Column, func
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.orm import relationship

from yourtube.db import base


class Creator(base):

    __tablename__ = "creators"

    username = Column(String, primary_key=True)
    channel_name = Column(String)

    clips = relationship("Clip")

    # Debug time
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def __init__(self, id, username, channel_name):
        self.id = id
        self.username = username
        self.channel_name = channel_name