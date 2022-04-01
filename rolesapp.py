import sys 
class rolesapp(object):

  def __init__(self):
    self.user = {
        'username' : '',
        'password' : '',
        'role' : 'user',
    }

    self.database = {
        'username' : [],
        'password' : [],
        'role' : [],
    }
    with open('database.txt','r') as f:
      i = 0
      for w in f.readlines():
        if w != '':
          if i%3 == 0:
            self.database['username'].append(w.replace('\n',''))
          elif i%3 == 1:
            self.database['password'].append(w.replace('\n',''))
          elif i%3 == 2:
            self.database['role'].append(w.replace('\n',''))
          i = i + 1

  user = {
      
  }

  database = {
        
  }

  
  def menu(self):    
    print('''
                                    Menu

      1) Форум
      2) Пользователи
      3) Вход

      0) Выйти
    ''')
    act = int(input("Выберите действие: "))      
    if act == 0:
      self.close()
    elif act == 1:
      self.forum()
    elif act == 2:
      if self.user['role'] == 'admin' or self.user['role'] == 'moder':
        self.userinfo()
      else:
        print('отказано в доступе!')
        self.menu()
    elif act == 3:      
      self.login()
    else:
      self.menu()
  
  
  def forum(self):
    print('''
                                    Forum
      Здравствуйте, {0}, это форум!
      Тут что-то написано
      

      0) Назад
    '''.format(self.user['username']))
    act = int(input("Выберите действие: "))     
    self.menu()

  
  def userinfo(self):  
    print('''
                                    User info

                                      База    
    ''')
    
    print('username', 'password', 'role', sep = '\t')
    for i in range(len(self.database['username'])):
      print('{0})'.format(i+1),  self.database['username'][i], self.database['password'][i], self.database['role'][i], sep = '\t')

    print('''
      
      Выберите пользователя.      
      
      0) Назад
    ''')
    act = int(input("Выберите действие: "))  
    if act == 0:
      self.menu()
    else:
      choice = act - 1
      print(self.database['username'][choice], self.database['password'][choice], self.database['role'][choice], sep = '\t')

      print('''
        1) Изменить роль

        0) Назад
      ''')
      act = int(input("Выберите действие: "))

      if act == 1:
        while act != 0:
          print('''
          Выберите на какую роль поменять
          1) user
          2) moder
          3) admin

          0) Назад
          ''')
          act = int(input("Выберите действие: "))
          
          if act == 1:
            self.database['role'][choice] = 'user'
          elif act == 2:
            self.database['role'][choice] = 'moder'
          elif act == 3:
            self.database['role'][choice] = 'admin'
          else:
            self.userinfo()

          with open('database.txt', 'w') as f:
            text = ''
            print(self.database)
            for i in range(len(self.database['role'])):
              text = text + '{0}\n{1}\n{2}\n'.format(self.database['username'][i],self.database['password'][i],self.database['role'][i])
              print(text)
            f.write(text)
      else:
        self.userinfo()
      

      

    
      
  
  def login(self):     
    print('''
                                    Login
      1) Продолжить
      2) Зарегистрироваться

      0) Назад
    ''')
    
    act = int(input("Выберите действие: "))
    while act != 0:      
      if act == 1:
        while act != 0:
          t = 0
          us = input('Введите имя пользователя: ')
          for i in range(len(self.database['username'])):
            if us == self.database['username'][i]:
              t = i
              while act != 0:
                ps = input('Введите пароль: ')
                if ps == self.database['password'][t]:
                  self.user['username'] = self.database['username'][t]
                  self.user['password'] = self.database['password'][t]
                  self.user['role'] = self.database['role'][t]
                  print('Добро пожаловать, {0}!'.format(us))
                  self.menu()
                else:
                  print('Неверный пароль!')
                  act = input('')
            else:
              print('Имя пользователя не найдено!')
    if act == 0:
      self.menu()
                
                  



      

  
  def signin(self):  
    print('''
                                    Sign in
      0) Выйти
    ''')
    act = int(input("Выберите действие: "))  

  
  def close(self):
    print('До свидания!')
  
  



myapp = rolesapp()

myapp.menu()