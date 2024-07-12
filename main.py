from contextlib import asynccontextmanager

from fastapi import FastAPI

import router
from database import create_tables, drop_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
  await drop_tables()
  print('База очищена!')
  await create_tables()
  print('База готова!')
  yield
  print('Выключение!')

app = FastAPI(lifespan=lifespan)
app.include_router(router.router)
