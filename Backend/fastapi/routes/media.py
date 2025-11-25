from fastapi import APIRouter, Query
from Backend.fastapi.db import db
import traceback   # <-- add this import

router = APIRouter()

@router.get("/api/media/list")
async def list_media(
    media_type: str = Query(..., regex="^(movie|show)$"),
    page: int = 1,
    page_size: int = 24,
    search: str = ""
):
    try:
        collection = db[media_type]
        query = {}
        if search:
            query = {"title": {"$regex": search, "$options": "i"}}

        cursor = collection.find(query).skip((page-1)*page_size).limit(page_size)
        items = await cursor.to_list(length=page_size)
        return {"items": items, "page": page, "page_size": page_size}
    except Exception as e:
        traceback.print_exc()   # <-- yahan add karo
        return {"error": str(e)}
