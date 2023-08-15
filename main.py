from ewelinkpy.Conection import get_authorization_code, get_access_token
from ewelinkpy.Device import  get_devices, get_device_status, set_device_status

if __name__ == "__main__":
    authorization_code = get_authorization_code()
    token = get_access_token(authorization_code)
    device_on = get_device_status(token, "1001xxxxxx")

    if device_on:
        set_device_status(token, "1001xxxxxx", False)
    else:
        set_device_status(token, "1001xxxxxx", True)
