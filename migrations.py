import secrets

from faker import Factory

from models import db, Contact, Note

fake = Factory.create()

# Reload tables
db.drop_all()
db.create_all()

# Make 100 fake contacts
for num in range(50):
    fullname = fake.name().split()
    name = fullname[0]
    surname = " ".join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    fake_contact = Contact(
        uid=secrets.token_urlsafe(8),
        name=name,
        surname=surname,
        email=email,
        phone=phone,
    )
    db.session.add(fake_contact)

db.session.commit()

contacts = Contact.query.order_by(Contact.name).all()
for contact in contacts:
    for i in range(5):
        new_remark = Note(
            rid=secrets.token_urlsafe(8),
            to=contact.uid,
            text=fake.sentence(nb_words=2, variable_nb_words=True),
        )
        db.session.add(new_remark)

db.session.commit()
