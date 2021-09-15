from selenium import webdriver
import time
import smtplib, ssl, email, pyautogui
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
import schedule

def main():
    doAndSendCheck()

def doAndSendCheck():

        #in directory: "C:\Users\Cougk\Documents\AtomCode\Bellproj.py"

    web = webdriver.Chrome()
    web.get('https://survey.dailyhealthcheck.com/#/surveys/8b947026-958e-458e-a6ae-5173a1894b96?qr_code_recipient=true')

    time.sleep(1)

    first = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/input')
    first.send_keys("Kyle")

    last = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div/input')
    last.send_keys("Hawkins")

    number = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[4]/div/input')
    number.send_keys("2533813534")

    reason = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[5]/div/textarea')
    reason.send_keys("School")

        #break for button clicks

    q1 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[1]/div[3]/div[2]')
    q1.click()

    q2 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/div[3]/div[2]')
    q2.click()

    q3 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[3]/div[3]/div[2]')
    q3.click()

    q4 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[4]/div[3]/div[2]')
    q4.click()

    q5 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[5]/div[3]/div[2]')
    q5.click()

    q6 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[6]/div[3]/div[2]')
    q6.click()

    q7 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[7]/div[3]/div[2]')
    q7.click()

    q8 = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[8]/div[3]/div[2]')
    q8.click()

        #break for end of button clicks. Next declaration and submittal

    declare = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div[3]/div/div[1]')
    declare.click()

    submit = web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[5]')
    submit.click()

    time.sleep(1)

    confirmation_text = web.find_element_by_css_selector('.status-message')
    print()
    print(confirmation_text.text)


        # part that screen shots the health check
    screenshotImage = pyautogui.screenshot('codeScreenShot.jpeg', region=(100, 50, 1800, 1800))
    screenshotImage.save(r"C:\Users\Cougk\Documents\AtomCode\codeScreenShot.jpeg")

     #commented out #Image.open('codeScreenShot.png').show()


        #This is the break that marks the start of the email function
        #creating the email message

    message = MIMEMultipart()

    emailSender = "codethrowawaybellarmine@gmail.com"
    emailRecipient = "21HawkinsKyle@bprep.org"

    #message['From'] = 'Computer <{codethrowawaybellarmine@gmail.com}>'.format(sender = gmail)
    message['From'] = emailSender
    message['To'] = '21HawkinsKyle@Bprep.org'
    message['Subject'] = 'Health Check'

    #attachmentPath = "C:\Users\Cougk\Documents\AtomCode\codeScreenShot.jpeg"

    file = "codeScreenShot.jpeg"
    attachment = open(file,'rb')
    #obj = MIMEBase('application','octet-stream')

    msgImage = MIMEImage(attachment.read())
    attachment.close()
    msgImage.add_header('Content-Disposition',"attachment; filename= "+file)

    #obj.set_payload((attachment).read())
    #encoders.encode_base64(obj)
    #obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(msgImage) # change to obj if wrong



    part = MIMEBase('application', "octet-stream")
    part.set_payload("codeScreenShot.jpeg")
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="codeScreenShot.jpeg"')

    message.attach(part)

    my_message = message.as_string()
        #done with message now need to establish server connection and send the message.


    #mySMTP = smtplib.SMTP("smtp.google.com")
    smtpServer = "smtp.gmail.com"
    port = 587
    password = "iH8teJ@va"
    context = ssl.create_default_context()




    newEmail = """From: From Kyle <codethrowawaybellarmine@gmail.com>
    To: To Kyle <21HawkinsKyle@bprep.org>
    Subject: Email Test
    This is the body of the email.
    """

    try:
        server = smtplib.SMTP(smtpServer,port)
        server.starttls(context=context)
        server.login(emailSender, password)
        server.sendmail(emailSender, emailRecipient, my_message) #could use 'newEmail in here for just text'
    except Exception as e:
        print("the email could not be sent.")
    finally:
        server.quit()


    print("Sent")

# ####
# schedule.every().day.at("08:45").do(doAndSendCheck)

# while True:
#     schedule.run_pending()
#     time.sleep(30)
# ####
main()