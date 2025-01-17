from collections import UserDict

class LenException(Exception):
    pass

class Field: # Base class for record fields.
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field): # For storing contact name
    def __init__(self, value):
        super().__init__(value)
        
class Phone(Field): # For storing contact phone numbers
    def __init__(self, value):
        super().__init__(value)
        if len(value) != 10:
            raise LenException('Your phone does not meet requirements. Must be 10 nums')
    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

class Record: # For storing contact information, including name and phone list.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
        return self.phones
    
    def remove_phone(self, phone):
        try:
            phone = Phone(phone)
            for num in self.phones:
                if num.value == phone.value:
                    self.phones.remove(num)
        except ValueError:
            raise ValueError
    def edit_phone(self, phone, new_phone: str):
        try:
            self.find_phone(phone)
            self.remove_phone(phone)
            self.add_phone(new_phone)
        except ValueError:
            raise ValueError
               
    def find_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            return phone
        else: return None
           
    def __str__(self) -> str:
        return (f"Contact name: {self.name.value}, phones: {[p.value for p in self.phones]}")

class AddressBook(UserDict): # For storing and managing records.
    def add_record(self, record: Record):
        if record not in self.data:
            self.data[record.name.value] = record
            return 'Record is successfully added.'
        else: return 'Record is already added.'
    
    def find(self, found_name: str):
        if found_name in self.data:
            return self.data.get(found_name)
        else: return None
        
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            return 'Record was successfully deleted.'
        else: return 'There is no record for this name.'
        
    def __str__(self):
        return '\n'.join(f"Contact name: {recordname}, phones: {recordphone}" for recordname, recordphone in self.data.items())


book = AddressBook() # Creating a new address book

# Creating a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding record John to the address book
book.add_record(john_record)

# Creating a record for Jane and adding to the address book
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Displaying all records in a book
print(book)

# Finding and editing the phone for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Deleting a Jane record
book.delete("Jane")
print(book)