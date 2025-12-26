from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    res = {}
    for i in users_id:
        d = 0
        s = ''
        for j in data['messages']:
            if j['type'] == 'message':
                if i == j['from_id']:
                    d+=1
                    s = j['from']
        res[s] = d
    return res 

if __name__ == '__main__':
    print(find_user_message_count(read_data('data/result.json'),find_all_users_id(read_data('data/result.json'))))
