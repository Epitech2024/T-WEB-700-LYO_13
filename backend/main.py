from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import router as user_router
from routes.preferences import router as preferences_router
from routes.global_preferences import router as global_preferences_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(preferences_router)
app.include_router(global_preferences_router)
