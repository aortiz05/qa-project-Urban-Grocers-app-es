import sender_stand_request
import data

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json().get("authToken")
    assert auth_token != ""
    assert user_response.status_code == 201

    return auth_token

def get_kit_body(name):
    item_body = data.kit_body.copy()
    item_body["content"] = name
    return item_body["content"]

def positive_assert(name):
    kit_body= get_kit_body(name)
    auth_token = get_new_user_token()
    positive_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert positive_response.status_code == 201
    assert positive_response.json()["name"] == kit_body["name"]

def negative_assert(name):
    kit_body= get_kit_body(name)
    auth_token = get_new_user_token()
    negative_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    print(f"response.status_code {negative_response.status_code}")

    assert negative_response.status_code == 404


def test_create_item_with_valid_authorisation():
    positive_assert ({"name": "value"})

def test_create_item_with_exact_number_of_characters():
    positive_assert( {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})

def test_create_item_with_empty_value():
    negative_assert({"name":""})

def test_create_item_with_hig_number_of_characters():
    negative_assert( {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})

def test_create_item_with_special_characters():
    positive_assert( {"name":"\"№%@\","})

def test_create_item_with_spaces():
    positive_assert( {"name":" A Aaa "})

def test_create_item_with_numbers():
    positive_assert( {"name":"123"})

def test_create_item_without_name():
    negative_assert({})

def test_create_item_with_int_value():
    positive_assert( {"name":123})