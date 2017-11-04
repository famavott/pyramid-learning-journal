"""Model for learning journal application."""

from sqlalchemy import (
    Column,
    Integer,
    Unicode
)

from .meta import Base


class Journal(Base):
    """Data model for each journal post."""

    __tablename__ = 'learning_journal'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    created = Column(Unicode)

    def to_dict(self):
        """Take all model attrs and render to dict."""
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created': self.created
        }
