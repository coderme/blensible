# Copyright (2017) CoderMe.com


def make_range(frames_count, hosts_count):
    if frames_count < 1 or hosts_count < 1:
        return []

    # make frames_count divisible if its not already
    origin_count = frames_count
    while frames_count % hosts_count != 0:
        frames_count += 1

    per_host = frames_count / hosts_count
    frames_range = []
    start = 1

    while hosts_count > 0:
        if hosts_count > 1:
            end = start + per_host - 1
        else:
            end = origin_count

        frames_range.append({
            "start": start,
            "end": end,
            })
        start += per_host 
        hosts_count -= 1

    return frames_range



class FilterModule(object):
    def filters(self):
        return {
                "make_range": make_range,
                }

