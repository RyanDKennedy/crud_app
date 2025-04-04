"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
March 18, 2025
"""

# CREATE TABLE books (
#     id integer auto_increment unique not null,
#     name text not null,
#     year_released integer,
#     page_amt integer,
#     price float,
#     author_id integer not null,
#     PRIMARY KEY (id),
#     FOREIGN KEY (author_id) REFERENCES authors(id)
# );

class BookRecord:

    # default constructor
    def __init__(self):
        self.id = -1
        self.name = "None"
        self.year_released = 0
        self.page_amt = 0
        self.price = 0
        self.author_id = 0

    # fill the record with values
    def fill(self, id, name, year_released, page_amt, price, author_id):
        self.id = id
        self.name = name
        self.year_released = year_released
        self.page_amt = page_amt
        self.price = price
        self.author_id = author_id

    def to_string(self):
        result = "id: "+str(self.id)
        result += "\nname: "+str(self.name)
        result += "\nyear released: "+str(self.year_released)
        result += "\npage amount: "+str(self.page_amt)
        result += "\nprice: "+str(self.price)
        result += "\nauthor id: "+str(self.author_id)
        return result
