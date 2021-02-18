import covid_19_project.mysql_connector as mc
def user_auth(email,count):
    fetch_query = "select * from reg_users;"
    mc.cursor.execute(fetch_query)
    for i in mc.cursor:
        if i[2] == email:
            count = 1
            break
    return count