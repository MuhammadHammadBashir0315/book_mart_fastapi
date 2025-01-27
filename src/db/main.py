from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import config


engine = AsyncEngine(create_engine(
    url=config.DATABASE_URL,
    echo=True
))

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())
async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session