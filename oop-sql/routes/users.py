from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users")
users = [
    {"id": 1, "username": "alex_199"},
    {"id": 2, "username": "jordan_dev"},
    {"id": 3, "username": "sky_watcher"},
    {"id": 4, "username": "coder_99"},
    {"id": 5, "username": "pixel_art"},
    {"id": 6, "username": " luna_byte"},
    {"id": 7, "username": "nova_codex"},
    {"id": 8, "username": "byte_meister"},
    {"id": 9, "username": "code_nomad"},
    {"id": 10, "username": "alpha_build"}
]
@router.post("/")
def get_root_users(data: dict):
    if not ("id" in data and "username" in data):
        raise HTTPException(400, "miss required fields")
    
    return {"data": data}