# lib/testing/test_student.py
import unittest
from lib.student import Student
from lib.chatty_student import ChattyStudent

class TestStudent(unittest.TestCase):
    def test_student_hello(self):
        student = Student()
        self.assertEqual(student.hello(), None)

    def test_student_raise_hand(self):
        student = Student()
        self.assertEqual(student.raise_hand(), None)

class TestChattyStudent(unittest.TestCase):
    def test_chatty_student_hello(self):
        chatty_student = ChattyStudent()
        self.assertEqual(chatty_student.hello(), None)

    def test_chatty_student_raise_hand(self):
        chatty_student = ChattyStudent()
        self.assertEqual(chatty_student.raise_hand(), None)

if __name__ == '__main__':
    unittest.main()
