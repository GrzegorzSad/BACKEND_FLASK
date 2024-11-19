from typing import Optional
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models.User import User

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[int] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(default =lambda: datetime.now(timezone.utc), index=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return "<Post {}>".format(self.body)