
# CREATE TABLE authors (
#     id integer auto_increment unique not null,
#     name text not null,
#     birth_year integer,
#     PRIMARY KEY (id)
# );

class AuthorRecord:

    def __init__(self):
        self.id = -1
        self.name = "None"
        self.birth_year = 0

    def fill(self, id, name, birth_year):
        self.id = id
        self.name = name
        self.birth_year = birth_year


