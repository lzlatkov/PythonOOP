from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_1 = Student("Student1", {"Python": ["n1", "n2", "n3"],
                                              "JS": ["n1", "n1"]})
        self.student_2 = Student("Student2")

    def test_init_with_courses(self):
        self.assertEqual("Student1", self.student_1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n1"]}, self.student_1.courses)

    def test_enroll_existing_course(self):
        result = self.student_1.enroll("Python", ["n4", "n5"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5"],
                          "JS": ["n1", "n1"]}, self.student_1.courses)

    def test_enroll_not_existing_course_add_notes_Y(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n1"],
                          "C#": ["n1", "n2"]}, self.student_1.courses)

    def test_enroll_not_existing_course_add_notes_empty_string(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n1"],
                          "C#": ["n1", "n2"]}, self.student_1.courses)

    def test_enroll_not_existing_course_without_notes(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n1"],
                          "C#": []}, self.student_1.courses)

    def test_add_notes_in_existing_course(self):
        result = self.student_1.add_notes("JS", "n3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n1", "n3"], self.student_1.courses["JS"])

    def test_add_notes_in_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("JS", "n1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_1.leave_course("JS")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("JS", self.student_1.courses)

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
