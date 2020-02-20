def filter_classads(classads):
    """
    Remove attributes that you do not want the service to expose

    :param classads: The classads to filter
    :return: The filtered classads
    """
    # redacted = ['environment','env']
    for i, item in enumerate(classads):
        classads[i]['classad']['environment'] = 'redacted'
        classads[i]['classad']['env'] = 'redacted'
    return classads