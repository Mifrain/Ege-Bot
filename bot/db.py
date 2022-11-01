import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        
        
    # LESSONS
    def add_lesson(self, prot:list, type):
        with self.conn:
            self.cur.execute('INSERT INTO lessons VALUES (?,?,?,?,?)', (type, prot[0], prot[1], prot[2], prot[3]))
            
    def del_lesson(self, callback):
        with self.conn:
            self.cur.execute('DELETE FROM lessons WHERE callback = ?',(callback,))
            
    
    def obj_lesson(self, obj, type):
        with self.conn:
            return self.cur.execute('SELECT name, callback FROM lessons WHERE obj = ? AND type = ?', (obj, type)).fetchall()
    
    def name_lesson(self, callback):
        with self.conn:
            return self.cur.execute('SELECT name FROM lessons WHERE callback = ?',(callback,)).fetchone()[0]
    
    def select_file(self, callback):
        with self.conn:
            return self.cur.execute('SELECT file FROM lessons WHERE callback = ?', (callback,)).fetchone()[0]
        
    # favorites lessons
    def all_like_lesson(self, user_id):
        with self.conn:
            return self.cur.execute('SELECT * FROM favorites WHERE user_id = ?', (user_id,)).fetchall()
    
    def add_like_lesson(self, user_id, callback):
        with self.conn:
            self.cur.execute('INSERT INTO favorites VALUES (?,?)', (user_id, callback))
            
    def del_like_lesson(self, user_id, callback):
        with self.conn:
            self.cur.execute('DELETE FROM favorites WHERE user_id = ? AND less_id = ?', (user_id, callback,))

    def check_like_lesson(self, user_id, callback):
        with self.conn:
            a = self.cur.execute('SELECT * FROM favorites WHERE user_id = ? AND less_id = ?', (user_id, callback,)).fetchone()
            if a == None:
                return False
            return True
        


    
    # USER
    def add_user(self, user_id):
        with self.conn:
            self.cur.execute('INSERT INTO user VALUES (?,?,?)',(user_id, 0, 0))
            
    def check_user(self, user_id):
        with self.conn:
            a = self.cur.execute('SELECT user_id FROM user WHERE user_id = ?', (user_id,)).fetchone()
            if a == None:
                return False
            return True
        
    def all_users(self):
        with self.conn:
            return self.cur.execute('SELECT user_id FROM user').fetchall()
    
    
    # ADMIN
    def all_admins(self):
        with self.conn:
            return self.cur.execute('SELECT user_id FROM user WHERE is_admin = 1 AND is_main_admin = 0').fetchall()
    
    def user_add_admin(self, user_id):
        with self.conn:
            self.cur.execute('UPDATE user SET is_admin = 1 WHERE user_id = ?', (user_id,))
    
    def user_del_admin(self, user_id):
        with self.conn:
            self.cur.execute('UPDATE user SET is_admin = 0 WHERE user_id = ?', (user_id,))
            
    
    def user_is_admin(self, user_id):
        with self.conn:
            return self.cur.execute('SELECT is_admin FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]
        
    def user_is_main_admin(self, user_id):
        with self.conn:
            return self.cur.execute('SELECT is_main_admin FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]
        
         
    
pydb = DataBase()
