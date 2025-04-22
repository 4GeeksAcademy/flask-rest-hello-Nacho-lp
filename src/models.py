from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
import base64

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

        
class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    user_to_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    
    def serialize(self) -> dict:
        return {
            "user_from": self.user_from_id,
            "user_to": self.user_to_id,

    }
class Post(db.Model):
    id: Mapped[int]= mapped_column(primary_key=True)
    user_id: Mapped[int]= mapped_column(ForeignKey("user.id"))
    image: Mapped[bytes]= mapped_column(nullable=False)
    def serialize(self) -> dict:
        image_b64 = base64.b64encode(self.image).decode("utf-8")
        return {
                "user_id": self.user_id,
                "image": image_b64
            }
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    
    def serialize(self):
        return{
            "author": self.author_id,
            "post": self.post_id
        }
class Likes(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    like: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return{
            "like": self.like,
            "post":self.post_id,
            "user": self.user_id
        }