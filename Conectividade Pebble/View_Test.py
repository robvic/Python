import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=testdb;'
                              'uid=sa;pwd=P@ssw0rd')


