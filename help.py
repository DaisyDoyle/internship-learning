import time
import yaml


def open_yaml(yaml_file):
    with open(yaml_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_selected_topic_or_return_to_menu(options, topic):
    """
    TODO
    """
    string_options = "\n".join(
        f"{option_num} - {option_name}"
        for option_num, option_name
        in options.items()
    )

    input_option = input(f"Please select a {topic} topic \n{string_options} \nAnswer: ")

    if int(input_option) not in options.keys():
        print(f"Invalid option, please select a number between 1 and {max(options.keys())}")
        return get_selected_topic_or_return_to_menu(options, topic)
    return input_option


def print_yaml_content_return_to_menu(yaml_file, topic_name, menu):
    yaml_content = open_yaml(yaml_file)
    print(yaml_content[topic_name])
    time.sleep(1)
    menu()
