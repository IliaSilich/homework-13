class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def change_password(self, new_password):
        print(f"{self.name} is changed password {self.password} to {new_password}")


class AuthService:
    def register(self, user):
        print(f"{user.name} is registered with email {user.email} and password {user.password}")

    def login(self, user):
        print(f"{user.name} is logged in with email {user.email} and password {user.password}")

    def logout(self, user):
        print(f"{user.name} is logged out")


class EmailService:
    def send_email(self, user, subject, message, recipients):
        print(f"{user.name} is sent message {message} with {subject} to {recipients}")


class ReportService:
    def generate_report(self, user, data):
        print(f"{user.name} is generated report with data {data}")


user = User("John Doe", "john.doe@example.com", "password123", "user")

auth_service = AuthService()
email_service = EmailService()
report_service = ReportService()

auth_service.register(user)
auth_service.login(user)
email_service.send_email(user, "Subject", "Message", ["recipient@example.com"])
report_service.generate_report(user, "Some data")
user.change_password("newpassword456")
auth_service.logout(user)
