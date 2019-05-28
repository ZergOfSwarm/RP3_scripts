MTP_from="majordomo.info@gmail.com"
SMTP_to="majordomo.info@gmail.com"
SMTP_serv="smtp.gmail.com:587"
SMTP_user="majordomo.info@gmail.com"
SMTP_pass="MDoi123ckd"
msg_body="as above"
subject="testing"

#sendEmail -f $SMTP_from -t $SMTP_to -u $subject -m $msg_body -s $SMTP_serv [color=red][b]-xu $SMTP_user[/b][/color] -xp $SMTP_pass
sendEmail -f "majordomo.info@gmail.com" -t "majordomo.info@gmail.com" -o message-charset=utf-8 -u "Photos..." -m "Тут идет небольшое тело письма..." -s smtp.gmail.com -xu majordomo.info@gmail.com -xp MDoi123ckd
