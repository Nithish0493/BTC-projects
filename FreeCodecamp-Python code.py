def add_setting(settings_dict,setting):
    key,value=setting
    key=str(key).lower()
    value=str(value).lower()

    if key in settings_dict:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    if key not in settings_dict:
        settings_dict[key]=value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(settings_dict,setting):
    key,value=setting
    key=str(key).lower()
    value=str(value).lower()

    if key in settings_dict:
        settings_dict[key]=value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    if key not in settings_dict:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings_dict,key):
    key=str(key).lower()
    if key in settings_dict:
        del settings_dict[key]
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'


def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    # Using a generator inside join()
    body = "".join(f"{key.capitalize()}: {value}\n" for key, value in settings_dict.items())
    return f"Current User Settings:\n{body}"


test_settings = {
    'theme': 'light',
    'language': 'english'
}










