from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represent a King from the Baratheon and Lannister families."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a King with a first name and alive status."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the King's eye color."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the King's hair color."""
        self.hairs = hairs

    def get_eyes(self):
        """Return the King's eye color."""
        return self.eyes
    
    def get_hairs(self):
        """Return the King's hair color."""
        return self.hairs