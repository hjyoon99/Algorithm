import re

def solution(new_id):
    
    clean_id = re.sub(r'[^a-z0-9\-_.]','', new_id.lower())
    clean_id = re.sub(r'\.+', '.', clean_id).strip('.')
    if not clean_id:
        clean_id = 'a'
    if len(clean_id) >= 16:
        clean_id = clean_id[:15].rstrip('.')
    if len(clean_id) <= 2:
        while len(clean_id) != 3:
            clean_id += clean_id[-1]
    
    return clean_id    
    