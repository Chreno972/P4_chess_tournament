class Admin:
    def __init__(self, name, prename):
        self.name = name
        self.prename = prename

    def create_admin(self):
        the_admin = (
            self.name,
            self.prename,
        )
        return the_admin

    def serialize_admin(self):
        serialized_admin = {
            "name": self.name + " " + self.prename,
        }
        return serialized_admin
