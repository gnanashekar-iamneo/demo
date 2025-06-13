# from sqlalchemy.ext.declarative import as_declarative,declared_attr
# from sqlalchemy import Column,DateTime
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from datetime import datetime


# @as_declarative()
# class BaseModel:
#     id=Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         index=True
#         )
#     created_at = Column(DateTime,default=datetime.utcnow)
#     updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

#     @declared_attr
#     def __tablename__(cls)->str:
#         return cls.__name__.lower()


# from sqlalchemy.orm import declarative_base
# base = declarative_base()
