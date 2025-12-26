from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    messages = 0
    for i in data['messages']:
        if i['type'] == 'message':
            messages+=1
    return messages

if __name__ == '__main__':
    print(find_number_of_messages(read_data('data/result.json')))
