from help import get_selected_topic_or_return_to_menu, print_yaml_content_return_to_menu, open_yaml


def execute_sql_theory(sql_theory_select_topic):
    """
    Function which returns behaviour of chosen sql theory topic.
    If sql_theory_select_topic is 1, code returns 'What is SQL?'
    this function is then called as part of sql_theory() function.

    """
    # Selecting the topic based on the user input number
    topic_name = {'1': 'what_is_sql',
                  '2': 'ddl',
                  '3': 'dml',
                  '4': 'dbl',
                  '5': 'sql_data_types',
                  '6': 'index_partitioning',
                  '7': 'sql_menu',
                  '8': 'sql_quit'}[sql_theory_select_topic]

    if topic_name == 'sql_menu':
        sql()
    if topic_name == 'sql_quit':
        raise SystemExit

    print_yaml_content_return_to_menu('sql_yaml.yml', topic_name, sql_theory)


def sql_theory():
    sql_theory_options = {"""
    Please select an SQL topic:
    1 - What is SQL?
    2 - DDL
    3 - DML
    4 - DBL
    5 - Data Types
    6 - Index partitioning
    7 - Back to SQL menu
    8 - Exit
    Answer: """}
    sql_theory_select_topic = get_selected_topic_or_return_to_menu(sql_theory_options, 'SQL')()
    execute_sql_theory(sql_theory_select_topic)()


def execute_sql(sql_select_topic):
    """
    Function which returns behaviour (function) of a particular topic

    E.g if the sql_selected_topic is 1 then we return the function "theory"
    This function is then called as part of sql() function
    """

    return{'1': sql_theory, '2': 'sql_commands', '3': 'sql_practice_links', '4': menu}[sql_select_topic]()

    # Return to sql menu
    sql()


def sql():
    # sql info provided here, options are theory, commands and practice links
    sql_select_topic = input("""
    Please select an SQL topic:
    1 - Theory
    2 - Commands
    3 - Practice links
    4 - Back to main menu
    Answer: """)

    if sql_select_topic not in ('1', '2', '3', '4'):
        print('Invalid option, select a number between 1 and 4.')
        sql()

    # Function to be executed based on
    execute_sql(sql_select_topic)()


def execute_python(python_select_topic):
    """
        Function which returns behaviour (function) of a particular topic

        E.g if the sql_selected_topic is 1 then we return the function "theory"
        This function is then called as part of sql() function
        """

    return{'1': 'packages', '2': 'functional_programming', '3': 'python_links', '4': menu,
           '5': quit}[python_select_topic]()
    # Return to python menu
    python()


def python():
    python_select_topic = input("""
    1 - Python packages
    2 - Functional programming
    3 - Useful learning links
    4 - Back to main menu
    5 - Quit
    Answer: 
    """)
    if python_select_topic not in ('1', '2', '3', '4', '5'):
        print("Invalid option, select a number between 1 and 5.")
        dwh()
    # Function to be executed based on
    execute_python(python_select_topic)()


def downloads():
    print("Downloads")
    print("""
These are some useful downloads:
Slack: https://community.getdbt.com/
Homebrew: https://brew.sh
Pycharm community edition: https://www.jetbrains.com/pycharm/download/#section=mac
Intellij community edition: https://www.jetbrains.com/idea/download/#section=mac
Teradata Studio: https://downloads.teradata.com/download/tools/teradata-studio
DBeaver: https://dbeaver.io
                 """)
    menu()


def execute_dwh(dwh_select_topic):
    """
    Function which returns behaviour of dwh() selected topic
    dwh_select_topic = '1', returns "overview" function which is then called.
    """

    def dwh_overview():
        print("Overview")
        dwh()

    def dwh_aws():
        print("AWS")
        dwh()

    def dwh_teradata():
        print("Teradata")
        dwh()

    def dwh_menu():
        menu()

    def dwh_quit():
        raise SystemExit

    return {'1': dwh_overview, '2': dwh_aws, '3': dwh_teradata, '4': dwh_menu, '5': dwh_quit}[dwh_select_topic]()


def dwh():
    dwh_select_topic = input("""
    Data Warehousing
    1 - Overview
    2 - AWS
    3 - Teradata
    4 - Back to main menu
    5 - Quit programme
    Answer: 
    """)

    if dwh_select_topic not in ('1', '2', '3', '4', '5'):
        print("Invalid option, select a number between 1 and 5.")
        dwh()
    # Function to be executed based on
    execute_dwh(dwh_select_topic)()


def quit():
    raise SystemExit


def execute_menu(select_topic):
    """
    Function which returns behaviour of menu() selected topic
    select_topic = '1', returns "SQL" function which is then called.
    """

    return {'1': sql, '2': python, '3': menu, '4': dwh, '5': downloads,
            '6': menu, '7': menu, '8': menu, '9': quit}[select_topic]()


def menu():
    """
        Returned argument is a menu offering access to learning resources organised by topic.

        select_topic(int) user enters number of topic they wish to study.

        Returns:
            menu option: selected topic

    """
    select_topic = input("""
    Welcome! Please select a topic:
    1 - SQL
    2 - Python
    3 - Data modelling
    4 - Data Warehousing
    5 - Downloads
    6 - Scrum and agile
    7 - GIT Commands
    8 - Further reading
    9 - Quit
    Answer: """)

    if select_topic not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Invalid option, select a number between 1 and 9.")
        menu()

    # Function to be executed based on
    execute_menu(select_topic)()


if __name__ == '__main__':
    menu()

