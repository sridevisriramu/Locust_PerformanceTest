from locust import HttpLocust, TaskSet, between

def login(l):
    l.client.get("https://mail.google.com/mail/", {"username":"sridevisriramu@gmail.com", "password":"Divyasri"})

def logout(l):
    l.client.post("/logout", {"username":"sridevisriramu@gmail.com", "password":"Divyasri"})

def index(l):
    l.client.get("https://mail.google.com/mail/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index: 2}

    def on_start(self):
        pass

    def on_stop(self):
        pass

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)