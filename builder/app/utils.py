def filter_dict(d, desired_keys):
    return {k: v for k, v in d.items() if k in desired_keys}
