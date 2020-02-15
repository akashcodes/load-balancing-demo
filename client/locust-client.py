from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("/")
    
    @task
    def dad_joke(self):
        self.client.post("?n=10000")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 10)