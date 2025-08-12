from project.senior_student import SeniorStudent
from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    def setUp(self):
        self.student = SeniorStudent(student_id="1234", name="Gosho", student_gpa=5.5)

    def test_init(self):
        self.assertEqual(self.student.student_id, "1234")
        self.assertEqual(self.student.name, "Gosho")
        self.assertEqual(self.student.student_gpa, 5.5)
        ########### ????????????????
        self.assertEqual(self.student.colleges, set())

    def test_valid_student_id(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = "12"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_valid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.student.name = " "
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_student_gpa(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = 0.1
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_college_with_success(self):
        input = self.student.apply_to_college(3.5, "UNSS")
        self.assertEqual("Gosho successfully applied to UNSS.", input)
        self.assertIn("UNSS", self.student.colleges)

    def test_apply_college_without_success(self):
        input = self.student.apply_to_college(6.5, "UNSS")
        self.assertEqual("Application failed!", input)
        self.assertNotIn("UNSS", self.student.colleges)

    def test_update_gpa_with_success(self):
        input = self.student.update_gpa(5.8)
        self.assertEqual("Student GPA was successfully updated.", input)
        self.assertEqual(self.student.student_gpa, 5.8)

    def test_update_gpa_without_success(self):
        input = self.student.update_gpa(0.1)
        self.assertEqual("The GPA has not been changed!", input)
        self.assertEqual(self.student.student_gpa, 5.5)

    def test_eq_same_gpa(self):
        other_student = SeniorStudent("8888", "Pesho", 5.5)
        self.assertTrue(self.student == other_student)

    def test_eq_different_gpa(self):
        other_student = SeniorStudent("8888", "Pesho", 4.5)
        self.assertFalse(self.student == other_student)


if __name__ == "__main__":
    main()