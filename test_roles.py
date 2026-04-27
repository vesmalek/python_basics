# test_roles.py
import unittest
from roles import check_role_access

class TestRoleAccess(unittest.TestCase):
    
    def test_admin_role(self):
        # We pass "Admin" (mixed case) to make sure .lower() is working
        result = check_role_access("Admin")
        self.assertEqual(result, "You can do everything.")

    def test_editor_role(self):
        result = check_role_access("editor")
        self.assertEqual(result, "You can create and edit.")

    def test_viewer_role(self):
        result = check_role_access("Viewer")
        self.assertEqual(result, "You can only read.")

    def test_invalid_role(self):
        # Testing a random word to trigger the 'else' block
        result = check_role_access("Guest")
        self.assertEqual(result, "Invalid role. Denied!")

if __name__ == "__main__":
    unittest.main()