# coding: utf-8
import cos_config


def main_menu():
    for index, citation_type in enumerate(cos_config.citation_config.keys()):
        print(f"{index+1}. {citation_type}")

    choice = input("Make a choice : ")
    if not choice.isdigit() or not (0 < int(choice) < (index + 2)):
        print("Error, relaunch the programm.")
        return

    return list(cos_config.citation_config)[int(choice)-1]


def get_elements(choice):
    print("Please give the following elements.")
    elements = []
    for index, element in enumerate(cos_config.citation_config[choice]):
        input_element = input(f"{index + 1}. {element} : ")


        if cos_config.citation_config[choice][element]['obligatory'] and input_element is None:
            print("It is obligatory to enter this element.")
            while input_element is not None :
                input_element = input(f"Retry :: {index}. {choice} : ")

        if cos_config.citation_config[choice][element]['uppercase']:
            input_element = input_element.upper()

        if cos_config.citation_config[choice][element]['lowercase']:
            input_element = input_element.lower()

        if cos_config.citation_config[choice][element]['surrounded']:
            input_element = cos_config.citation_config[choice][element]['surrounded'][0] + input_element + cos_config.citation_config[choice][element]['surrounded'][1]

        if input_element != "":
            elements.append(input_element)

    print(', '.join(elements) + '.')
    print("--")
    if input("Is there another source to generate ?") in ["yes", "y"]:
        get_elements(main_menu())
    else:
        return


get_elements(main_menu())
