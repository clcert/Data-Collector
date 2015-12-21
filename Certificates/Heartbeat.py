
def parse_heartbeat(output, data):
    if 'heartbleedData' in data:
        heartbleed_data = data['heartbleedData']
        if 'heartbeat' in heartbleed_data:
            heartbeat = heartbleed_data['heartbeat']
            if heartbeat:
                output.write(data['ip'])

# TODO Finish the merge method
# def merge_heartbleed(grabber_input, script_input, output):
