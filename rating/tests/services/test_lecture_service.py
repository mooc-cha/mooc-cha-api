import unittest
import pytest

from rating.services import lecture_service


class TestLectureService(unittest.TestCase):
    async def test_list_lectures(self):
        await lecture_service.add_lecture(name="hello", description="world")
        lectures = await lecture_service.list_lectures()
        self.assertEqual(len(lectures), 1)

    async def test_find_lecture(self):
        await lecture_service.add_lecture(name="hello", description="world")
        lectures = await lecture_service.list_lectures()
        lecture = await lecture_service.find_lecture(id=lectures[0].id)
        self.assertEqual(lecture.name, "hello")

