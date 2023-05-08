import sys
import logging
from logging.handlers import RotatingFileHandler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import os.path

logger = logging.getLogger("Email Distribution Log")
# Mirror logging to stream out.
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# Format logger.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Logger file.
# Logger file.
log_file = "Logs\email_distribution_log.log"
# Add a rotating handler to the code.
handler = RotatingFileHandler(log_file, maxBytes=20000000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)

current_dt = datetime.datetime.now()


class MailHost:
    def __init__(self, from_email, to_email, email_subject):
        self.from_email_address = from_email
        self.to_email_address = to_email
        self.email_subject_line = email_subject
        self.html_wrapper_header = \
            "<html>" \
            "<style>" \
            "p {font-family: 'Courier New'}" \
            "</style>" \
            "<head></head><body>"\
            "<p>"
        self.html_wrapper_footer = \
            "</p>" \
            "</body></html>"
        self.email_body = ""

    def send_email(self):
        """
        Send internal email given a to email address, from email address, and email subject line (all strings).
        :return: Sent email.
        """
        if self.email_body == "":
            html = self.html_wrapper_header + \
                "This is a <b>test email</b> to demonstrate sending an <i>internal</i> " \
                "email via Python on " + str(current_dt.date()) + "." \
                + self.html_wrapper_footer
        else:
            self.edit_email_body(self.email_body)
            html = self.email_body

        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email_address
        msg['To'] = self.to_email_address
        msg['Subject'] = self.email_subject_line
        msg.attach(MIMEText(html, 'html'))
        mail_s = smtplib.SMTP('mailhost.jpmchase.net')
        mail_s.ehlo_or_helo_if_needed()
        mail_s.verify(self.from_email_address)
        mail_s.sendmail(self.from_email_address, self.to_email_address.split(','), msg.as_string())
        mail_s.quit()

        logger.info("Email sent to %s from %s with subject line %s",
                    self.to_email_address, self.from_email_address, self.email_subject_line)

    def send_email_with_attachment(self,filename):
        """
        Send internal email given a to email address, from email address, and email subject line (all strings).
        :return: Sent email.
        """
        if self.email_body == "":
            html = self.html_wrapper_header + \
                   "This is a <b>test email</b> to demonstrate sending an <i>internal</i> " \
                   "email via Python on " + str(current_dt.date()) + "." \
                   + self.html_wrapper_footer
        else:
            self.edit_email_body(self.email_body)
            html = self.email_body

        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email_address
        msg['To'] = self.to_email_address
        msg['Subject'] = self.email_subject_line

        with open(filename, 'rb') as a_file:
            basename = os.path.basename(filename)
            part = MIMEApplication(a_file.read(), Name=basename)

        part['Content-Disposition'] = 'attachment; filename="%s"' % basename
        msg.attach(part)

        msg.attach(MIMEText(html, 'html'))
        mail_s = smtplib.SMTP('mailhost.jpmchase.net')
        mail_s.ehlo_or_helo_if_needed()
        mail_s.verify(self.from_email_address)
        mail_s.sendmail(self.from_email_address, self.to_email_address.split(','), msg.as_string())
        mail_s.quit()

        logger.info("Email sent to %s from %s with subject line %s",
                    self.to_email_address, self.from_email_address, self.email_subject_line)

    def edit_email_body(self, body_text):
        """
        Edits the body of the email by adding an HTML header and footer wrapper to an input string of text.
        :param body_text: String of text for body of email.
        :return: MailHost object with new body of text.
        """
        self.email_body = self.html_wrapper_header + body_text + self.html_wrapper_footer

    def add_multiple_recipients(self, recipient_list):
        """
        Adds multiple recipients to MailHost object as to send the same email to multpile contacts.
        :param recipient_list: List of recipients.
        :return: MailHost object with newly added list of recipients.
        """
        pass

    def add_cc_recipients(self):
        pass

    def add_bcc_recipients(self):
        pass