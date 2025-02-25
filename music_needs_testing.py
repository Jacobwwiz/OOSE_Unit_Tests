from datetime import datetime
from typing import List, Optional

class Event:
    """Represents an event with available tickets."""
    def __init__(self, event_id: int, name: str, date: str, time: str, available_tickets: int, price: float):
        self.event_id = event_id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M:%S").time()
        self.available_tickets = available_tickets
        self.price = price

    def is_ticket_available(self) -> bool:
        """Check if tickets are available for this event."""
        return self.available_tickets > 0

    def book_ticket(self) -> Optional[str]:
        """Attempt to book a ticket for this event."""
        if self.is_ticket_available():
            self.available_tickets -= 1
            return f"Ticket booked for {self.name} on {self.date} at {self.time}."
        return "No tickets available."

    def share_event(self) -> str:
        """Generate a message to share event details."""
        return f"Check out {self.name} happening on {self.date} at {self.time}!"

class TicketSystem:
    """Manages events and ticket purchases."""
    def __init__(self):
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """Add a new event to the system."""
        self.events.append(event)

    def find_event(self, event_id: int) -> Optional[Event]:
        """Find an event by its ID."""
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None