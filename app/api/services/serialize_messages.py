def serialize_users(users):
    users_list = []

    for user in users:
        users_list.append({
            'id': user.id,
            'name':user.name,
            'email': user.email,
            'password': user.password,
            'messages_sent': serialize_messages(user.messages_sent),
        })

    return users_list

def serialize_messages(messages):
    messages_list = []

    for message in messages:
        messages_list.append({
            'id': message.id,
            'subject': message.subject,
            'message': message.message,
            'timestamp': message.timestamp,
        })
    
    return messages_list