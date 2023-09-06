import csv, pandas as pd, random, requests, string

from faker import Faker


def generate_password(password_len: int = 10) -> str:
    if not isinstance(password_len, int):
        raise TypeError('Invalid Type...')

    choices = string.ascii_letters + string.digits + '#$%&'
    result = ''

    for _ in range(password_len):
        result += random.choice(choices)

    return result


def read_requirements_txt():
    with open('requirements.txt', 'r') as txt_file:
        requirements_content = txt_file.read()

    return requirements_content


def generate_users():
    fake = Faker()

    fake_user = ''
    for _ in range(30):
        fake_user += fake.name() + ' ' + fake.email() + '; '

    return fake_user


def astros_number():
    r = requests.get('http://api.open-notify.org/astros.json')
    astros_number = r.json()["number"]

    return astros_number


def mean_height_weight():
    hw_data = pd.read_csv('hw.csv', index_col='Index')
    hw_data_descr = hw_data.describe()
    mean_hw_series = hw_data_descr.loc["mean"]
    mean_hw_dict = {
        key.strip().replace('"', ''): round(value, 3)
        for key, value in mean_hw_series.items()
    }

    return f'Average height and weight parameters: {mean_hw_dict}'
