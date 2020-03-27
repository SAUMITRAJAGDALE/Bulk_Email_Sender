import pandas as pd
import smtplib

SenderAddress = "framesvashi@gmail.com"
password = "fr123alumni"

e = pd.read_excel("test.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
greeting = "Dear Alumni,"
msg="It was an incredible reunion of Alumni, Students, Faculty and Staff members at the lawn of Fr. Conceicao Rodrigues Institute of Technology. Thank you very much again. The event was a great success in its prime motive of Connecting and Networking the alumnus and the present students. Last but not the least we would like to have feedback on the overall event from the social media to the food we had."
link=" Your feedback is highly appreciated and will deinitely help us to improve. Please fill the feedback from the link \n https://forms.gle/pUfDbaTyRbbyKXaQ7"
end="We hope to see you next time."
regards="With Regards"
name="FRAMES Association"
subject = "Feedback: Alumni Meet 2020"
body = "Subject: {}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n{}".format(subject,greeting,msg,link,end,regards,name)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
