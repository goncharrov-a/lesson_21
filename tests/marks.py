import allure


def owner(value: str):
    return allure.label("owner", value)


def layer(value: str):
    return allure.label("layer", value)


def microservice(value: str):
    return allure.label("microservice", value)


def tm4j(value: str):
    return allure.label("tm4j", value)


def jira_issues(*issues: str):
    return allure.label("jira", *issues)
