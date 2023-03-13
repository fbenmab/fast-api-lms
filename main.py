from typing import Optional, List
from fastapi import FastAPI, Path, Query

import api.users
from api import users, sections, courses

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "fbm",
        "email": "fbm@ts.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)





