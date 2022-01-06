import sqlite3


class BotDB:
    def __init__(self, db_file):
        print("opening")
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def leaderboard(self, discord_group_id, out):
        result = self.cursor.execute(
            "SELECT `eolymp_nickname`, `discord_user_id` FROM `users` WHERE `discord_group_id` = ?",
            (discord_group_id,),
        )
        bd_users_output = result.fetchall()
        if out:
            users = []
            for user in bd_users_output:
                users.append(user[0])
            return users
        else:
            return bd_users_output

    def close(self):
        """Закрываем соединение с БД"""
        print("closing")
        self.conn.close()


botDB_ = BotDB("eolymp_users.db")
print(botDB_.leaderboard(909078994568228865, True))
botDB_.close()
