
from enum import Enum
from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix = '/blog',
    tags = ['blog'],
)


class BlogType(str, Enum):
    short = 'short'
    story = 'story'

@router.get("/type/{type}")
def getBlog(type: BlogType, response: Response):
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog type is {type}"}
