from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[int] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[int] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[Optional[int]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def __repr__(self):
        return "<User {}>".format(self.username)
    
from app.models.Post import Post