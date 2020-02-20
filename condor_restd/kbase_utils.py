import re


def filter_classads(classads):
    """
    Remove attributes that you do not want the service to expose

    :param classads: The classads to filter
    :return: The filtered classads
    """
    # redacted = ['environment','env']
    for i, item in enumerate(classads):
        env = classads[i]['classad']['environment']
        env = re.sub(r'KB_AUTH_TOKEN=\w+\s?', 'KB_AUTH_TOKEN=Removed ', env)
        env = re.sub(r'KB_ADMIN_AUTH_TOKEN=\w+\s?', 'KB_ADMIN_AUTH_TOKEN=Removed ', env)
        classads[i]['classad']['environment'] = env

    return classads
