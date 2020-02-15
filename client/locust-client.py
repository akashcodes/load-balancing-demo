from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("/")
    
    @task
    def dad_joke(self):
        self.client.get("/dad-joke")
    
    @task
    def fetch(self):
        self.client.get("/fetch")
    
    @task
    def loop(self):
        self.client.get("/loop/10000")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 10)