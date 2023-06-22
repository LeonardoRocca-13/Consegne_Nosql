import redis

# Connect to Redis
# r = redis.Redis(host='your host here!', port=17474, password='password')

r = redis.Redis(
  host='redis-16571.c293.eu-central-1-1.ec2.cloud.redislabs.com',
  port=16571,
  password='hAtjcrludDL3IofW4mtnFdBbJbzlbesk')


def identify_user():
    print('=== User Identification ===')

    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user_id = r.get(f'email:{email}')

    if not user_id:
        user_id = r.incr('user_id')

        r.hset(f'user:{user_id}', 'email', email)
        r.hset(f'user:{user_id}', 'username', username)
        r.hset(f'user:{user_id}', 'password', password)

        r.set(f'email:{email}', user_id)
        print('New user created successfully!')
    else:
        user_id = int(user_id)
        user_data = r.hgetall(f'user:{user_id}')

        if user_data[b'username'].decode() != username or user_data[b'password'].decode() != password:
            print('User verification failed. Invalid username or password.')
            return None
        print(f'User verified with ID: {user_id}')

    return user_id


def write_message(user_id, message):
    message_key = f'messages:{user_id}'
    r.lpush(message_key, message)


def read_all_messages():
    all_messages = {}
    user_keys = r.keys('user:*')

    for user_key in user_keys:
        user_id = user_key.decode().split(':')[1]
        username = r.hget(f'user:{user_id}', 'username').decode()
        messages_key = f'messages:{user_id}'

        messages = r.lrange(messages_key, -10, -1)
        all_messages[username] = [msg.decode() for msg in messages]

    return all_messages


def delete_user(user_id):
    user_key = f'user:{user_id}'
    user_data = r.hgetall(user_key)

    email = user_data[b'email'].decode()
    messages_key = f'messages:{user_id}'

    r.delete(user_key, f'email:{email}', messages_key)


def clear_database():
    r.flushall()


def print_chat_messages(chat_messages):
    for username, messages in chat_messages.items():
        print(f'{username}:')
        for msg in messages:
            print(f'- {msg}')


def print_menu():
    print('1. Identify user')
    print('2. Write message')
    print('3. Read last 10 chat messages')
    print('4. Delete user')
    print('5. Clear database')
    print('6. Exit')


# Main program loop
user_id = None

while True:
    print('\n=== Chat Program ===')
    print_menu()
    choice = input('Enter your choice (1-6): ')

    match choice:
        case '1':
            user_id = identify_user()
        case '2':
            if not user_id:
                print('You need to identify yourself before writing a message!')
            else:
                message = input('Enter your message: ')
                write_message(user_id, message)
                print('Message written successfully!')
        case '3':
            chat_messages = read_all_messages()
            if not chat_messages:
                print("No chat messages available.")
            else:
                print("Last 10 chat messages:")
                print_chat_messages(chat_messages)
        case '4':
            if not user_id:
                print("You need to identify yourself before deleting your user.")
            else:
                delete_user(user_id)
                print("User deleted successfully!")
                user_id = None
        case '5':
            confirm = input("Are you sure you want to clear the database? This action cannot be undone. (y/n): ")
            if confirm.lower() == 'y':
                clear_database()
                print("Database cleared successfully!")
                user_id = None
            else:
                print("Clear database operation canceled.")

        case '6':
            print("Exiting the program...")
            break

        case default:
            print("Invalid choice. Please try again.")
