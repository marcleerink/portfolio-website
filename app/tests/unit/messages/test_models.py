import pytest
from app.messages.models import Message, User
from app.extensions.database import db


def test_user_update(client):
    # updates User model
    user = User(name = 'Test tester', email = 'test@test.com', password = 'testtest')
    db.session.add(user)
    db.session.commit()

    user.email = 'maleerink@gmail.com'
    user.save()

    updated_user = User.query.filter_by(name='Test tester').first()
    assert updated_user.email == 'maleerink@gmail.com'
