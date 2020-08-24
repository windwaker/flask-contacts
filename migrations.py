from models import db, Contact, Note
from faker import Factory
import secrets 

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
for num in range(50):
    fullname = fake.name().split()
    name = fullname[0]
    surname = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    mi_contacto = Contact(
        uid=secrets.token_urlsafe(8),
        name=name,
        surname=surname,
        email=email,
        phone=phone)
    db.session.add(mi_contacto)

db.session.commit()

contacts = Contact.query.order_by(Contact.name).all()
for contact in contacts:
    for i in range(5):
        new_remark = Note(
            rid=secrets.token_urlsafe(8),
            to = contact.uid,
            text = fake.sentence()
            )
        db.session.add(new_remark)
db.session.commit()