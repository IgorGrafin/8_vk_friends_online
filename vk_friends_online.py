import vk
import getpass


APP_ID = 6379260


def get_user_login():
    return input("Введите логин: ")


def get_user_password():
    return getpass.getpass("Введите пароль: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)

    return api.users.get(
        user_ids=api.friends.getOnline(),
        fields='first_name, last_name, online'
    )


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("{0} {1}".format(
            friend["first_name"],
            friend["last_name"]
        ))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        exit("Неверные логин/пароль")
    output_friends_to_console(friends_online)
