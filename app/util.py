from flask import render_template
from flask_mail import Message
from app import mail

def send_email(to, subject, template, **kwargs):
    """
    Send an email using Flask-Mail.

    :param to: Recipient email address
    :param subject: Email subject
    :param template: The template name (e.g., 'welcome_email.html')
    :param kwargs: Additional parameters to pass to the template
    """
    try:
        # Render the email template
        html_body = render_template(template, **kwargs)

        # Create the email message
        msg = Message(
            subject=subject,
            recipients=[to],
            html=html_body
        )

        # Send the email
        with mail.connect() as conn:
            conn.send(msg)
        print(f"Email sent to {to}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False