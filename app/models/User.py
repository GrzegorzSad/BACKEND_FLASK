from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[int] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[int] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[Optional[int]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def from_dict(self, data, new_user = False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def to_dict(self, include_email = False):
        data = {
            'id': self.id,
            'username': self.username,
            'post_count': self.post_count()
        }
        if include_email:
            data['email'] = self.email
        return data
    
from app.models.Post import Post
    
