import re
import datetime
import json
from locust import HttpLocust, TaskSet, task

class BrowseDocumentation(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome to the Simple Travel Agency!.*")
    HOME_PAGE_TITLE_XPATH = "//h1[contains(text(),'Welcome to the Simple Travel Agency!')]";
    HOME_PAGE_TITLE_CSS = ".jumbotron h1";

    @task
    def index_page_with_regex_assertion(self):
        r = self.client.get("/")
        assert self.HOME_PAGE_TITLE_REGEX.search(r.text) is not None, \
            "Expected title has not been found!"

    @task
    def index_page_with_response_code_assertion(self):
        r = self.client.get("/")
        assert r.status_code is 200, "Unexpected response code: " + r.status_code


    @task
    def index_page_with_response_duration_assertion(self):
        r = self.client.get("/")
        assert r.elapsed < datetime.timedelta(seconds = 1), "Request took more than 1 second"


class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation   
    min_wait = 1 * 1000
    max_wait = 5 * 1000