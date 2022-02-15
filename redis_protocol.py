def generate_redis_protocol(*cmd):
    instruction = cmd[0]

    if instruction == 'HMSET':
        return generate_redis_protocol_HSET(*cmd)
    elif instruction == 'HSET':
        return generate_redis_protocol_HSET(*cmd)
    elif instruction == 'SET':
        return generate_redis_protocol_SET(*cmd)

    return ""

def generate_redis_protocol_SET(*cmd):
    return generate_redis_protocol_HSET(*cmd)

def generate_redis_protocol_HSET(*cmd):
    proto = (f"*{len(cmd)}\r\n")
    proto += "".join([f'${len(e)}\r\n{e}\r\n' for e in cmd])
    return proto
