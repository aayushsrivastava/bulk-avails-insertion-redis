def generate_redis_protocol(*cmd):
    instruction = cmd[0]

    if instruction == 'HSET':
        return generate_redis_protocol_HSET(*cmd)

    return ""

def generate_redis_protocol_HSET(*cmd):
    proto = (f"*{len(cmd)}\r\n")
    proto += "".join([f'${len(e)}\r\n{e}\r\n' for e in cmd])
    return proto
