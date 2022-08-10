from typing import List
from rating.models import Lecture


async def add_lecture(*, name: str, description: str) -> None:
    lecture = Lecture(name=name, description=description)
    await lecture.save()

async def list_lectures() -> List[Lecture]:
    return await Lecture.all()

async def find_lecture(*, id: int) -> Lecture:
    return await Lecture.get(id=id)

