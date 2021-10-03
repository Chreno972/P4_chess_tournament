"""The administrator module

Returns:
    class: The administrator's class
"""


class Admin:
    """The game administrator class"""

    def __init__(self, name, prename):
        """Game administrator initialisation

        Args:
            name (str): The game administrator name
            prename (str): The game administrator prename
        """
        self.name = name
        self.prename = prename

    def create_admin(self):
        """Affords to create a game administrator

        Returns:
            List: A list with both game administrator's name and prename
        """
        the_admin = (
            self.name,
            self.prename,
        )
        return the_admin

    def serialize_admin(self):
        """Affords to serialize the administrator's informations

        Returns:
            Dict: A dictionnary based on the admin list items
        """
        serialized_admin = {
            "name": self.name + " " + self.prename,
        }
        return serialized_admin
