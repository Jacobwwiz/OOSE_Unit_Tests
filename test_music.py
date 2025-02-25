import unittest
from unittest.mock import MagicMock
from music_needs_testing import TicketSystem, Event

class TestTicketSystem(unittest.TestCase):

    def setUp(self):
        """Set up test data before each test."""
        self.system = TicketSystem()
        self.event = Event(1, "Concert Night", "2025-06-15", "20:00:00", available_tickets=2, price=50.0)
        self.system.add_event(self.event)

    def test_find_event(self):
        """Test if an event can be found by ID."""
        event = self.system.find_event(1)
        self.assertIsNotNone(event)
        self.assertEqual(event.name, "Concert Night")

    def test_book_ticket_success(self):
        """Test booking a ticket when available."""
        result = self.event.book_ticket()
        self.assertEqual(result, "Ticket booked for Concert Night on 2025-06-15 at 20:00:00.")
        self.assertEqual(self.event.available_tickets, 1)  # One ticket should be left

    def test_book_ticket_no_availability(self):
        """Test booking a ticket when none are left."""
        self.event.book_ticket()  # First ticket
        self.event.book_ticket()  # Second ticket
        result = self.event.book_ticket()  # No more tickets
        self.assertEqual(result, "No tickets available.")
        self.assertEqual(self.event.available_tickets, 0)  # No tickets left

    def test_mock_ticket_availability(self):
        """Test ticket booking with a mocked ticket availability check."""
        self.event.is_ticket_available = MagicMock(return_value=False)
        result = self.event.book_ticket()
        self.assertEqual(result, "No tickets available.")  # Simulated ticket sellout

    def test_share_event(self):
        """Test event sharing message."""
        message = self.event.share_event()
        self.assertEqual(message, "Check out Concert Night happening on 2025-06-15 at 20:00:00!")

if __name__ == '__main__':
    unittest.main()
