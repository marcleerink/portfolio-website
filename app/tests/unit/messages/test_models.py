from pickletools import uint4
import pytest
from app.messages.models import Message, User
from app.extensions.database import db


def test_user_delete(client):
    # deletes record User model
    user = User(name = 'Test tester', email = 'test20@test.com', password = 'testtest')
    db.session.add(user)
    db.session.commit()

    user.delete()

    deleted_user = User.query.filter_by(name='Test tester').first()
    assert deleted_user is None

def test_message_delete(client):
    # deletes record Message model
    message = message(subject = 'Test tester', message = 'sgsdgsdgsdgsdgdggdsc')
    db.session.add(message)
    db.session.commit()

    message.delete()

    deleted_message = User.query.filter_by(subject='Test tester').first()
    assert deleted_message is None
