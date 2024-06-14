# lib/testing/test_student.py
import unittest
from lib.student import Student
from lib.chatty_student import ChattyStudent

class TestStudent(unittest.TestCase):
    def test_student_hello(self):
        student = Student()
        self.assertIsNone(student.hello())

    def test_student_raise_hand(self):
        student = Student()
        self.assertIsNone(student.raise_hand())

class TestChattyStudent(unittest.TestCase):
    def test_chatty_student_hello(self):
        chatty_student = ChattyStudent()
        self.assertIsNone(chatty_student.hello())

    def test_chatty_student_raise_hand(self):
        chatty_student = ChattyStudent()
        self.assertIsNone(chatty_student.raise_hand())

if __name__ == '__main__':
    unittest.main()
