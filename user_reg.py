import covid_19_project.mysql_connector as mc
def user_reg(name,email):
    query = "insert into reg_users (name,email_id) values('{}','{}');".format(name, email)
    print(query)
    mc.cursor.execute(query)
    mc.dbc.commit()
