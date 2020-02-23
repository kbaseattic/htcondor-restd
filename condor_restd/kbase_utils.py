import re
import logging
logging.basicConfig(level=logging.INFO)


def clean_environment(env):
    env = re.sub(r'KB_AUTH_TOKEN=\w+\s?', 'KB_AUTH_TOKEN=Removed ', env)
    env = re.sub(r'KB_ADMIN_AUTH_TOKEN=\w+\s?', 'KB_ADMIN_AUTH_TOKEN=Removed ', env)
    return env

def filter_classads(classads):
    """
    Remove attributes that you do not want the service to expose

    :param classads: The classads to filter
    :return: The filtered classads
    """
    # redacted = ['environment','env']

    for classad in classads:
        if classad.get('classad') is not None:
            if classad.get('classad').get('environment') is not None:
                env = classad['classad']['environment']
                classad['classad']['environment'] = clean_environment(env)
        else:
            for key in classad.keys():
                env = classad[key]['environment']
                classad[key]['environment'] = clean_environment(env)

    return classads
