import smtplib
def otp_sender(rec_mail,otp):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('system.gen.noreply@gmail.com', 'apsj#12345678')
    message = str(otp)
    s.sendmail("system.gen.noreply@gmail.com",rec_mail, message)
    s.quit()