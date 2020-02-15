from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("/")
    
    @task
    def index(self):
        self.client.get("/dad-joke")
        
    @task
    def about(self):
        self.client.get("/fetch")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)