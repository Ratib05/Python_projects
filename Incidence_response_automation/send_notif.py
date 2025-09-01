# connect to smtp server and send emails
import smtplib

# construct plain text email messages
from email.mime.text import MIMEText

# allows interaction with system-specific parameters and functions like command-line arguments.
import sys

def send_notification(subject, body, to_email):
    
    # set sender details
    from_email = "ratibhoque@gmail.com"
    password = "********"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:

        # establish secure connection
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        
        # auto login to email
        server.login(from_email, password)
        
        # auto send email
        server.sendmail(from_email, [to_email], msg.as_string)
        
        # terminate connection
        server.quit()
        print(f"Notification sent to {to_email}")
    
    # catch errors
    except Exception as e :
        print("Failed to send notification")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Done")
        sys.exit(1)
    send_notification(sys.argv[1], sys.argv[2], sys.argv[3])