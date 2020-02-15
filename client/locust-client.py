from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("/")
    
    @task
    def dad_joke(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 1)