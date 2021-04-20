import pymysql

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'tkddnr783!',
    db ='busan'
)

sql = '''
  CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
sql_1="INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네 ㅠㅠ', '김태경');"
sql_2="INSERT INTO `busan`.`users` (`username`, `mail`, `name`, `password`) VALUES ('여러분들~~', 'i@naver.com', '이상욱', '12345');"
#title = input('제목을 적으세요')
#body = input('내용을 적으세요')
#author = input('누구세요')
#sql_3="INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('%s', '%s', '%s');"
#input_data = [title, body, author]

cursor = db.cursor() #쿼리문 날리기
#cursor.execute(sql, input_data)
#db.commit()
#db.close()
cursor.execute('SELECT * FROM users;')
users = cursor.fetchall()
print(cursor.rowcount, users)