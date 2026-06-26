from storage import Storage
storage = Storage("contacts.db")

storage.open()
print(storage.is_open())