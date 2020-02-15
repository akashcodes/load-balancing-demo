from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("/")
    
    @task(60)
    def dad_joke(self):
        self.client.get("/dad-joke")
    

    @task(5)
    def fetch(self):
        self.client.get("/fetch")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 1)