import uuid

def get_random_code():
    code = str(uuid.uuid4())[:11].replace('-', '')  # integer döndüğü için stringe çevirdik
    return code

print(get_random_code())

