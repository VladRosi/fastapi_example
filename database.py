from sqlalchemy import Integer, String, Text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
  "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class BaseModel(DeclarativeBase):
  id: Mapped[int] = mapped_column(primary_key=True)

class TaskModel(BaseModel):
  __tablename__ = 'task'
  name: Mapped[str] = mapped_column(String(255))
  description: Mapped[str | None] = mapped_column(Text, nullable=True)

async def create_tables():
  async with engine.begin() as conn:
    await conn.run_sync(BaseModel.metadata.create_all)

async def drop_tables():
  async with engine.begin() as conn:
    await conn.run_sync(BaseModel.metadata.drop_all)
