
def query_serializer(schema, results):
    ret = []
    for result in results:
        ret.append(schema.dump(result).data)
    return ret


def get_request_arg(key, base_value):
    try:
        result = request.args.get(key, base_value)
    except ValueError:
        result = base_value
    return result
