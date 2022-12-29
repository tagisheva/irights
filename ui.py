
from datetime import datetime
import inquirer
import utils
import create_ipreport_docx as generator
import convert_to_pdf as converter

_GENERATE = "Generate new ip report"
_CONVERT = "Convert report to pdf"
_EXIT = "Exit"
_INIT = "action"

# todo: validation of inputs
while True:
    _init = [inquirer.List(_INIT, message="Select what to do: ", choices=[_GENERATE, _CONVERT, _EXIT],)]
    _action = inquirer.prompt(_init)[_INIT]

    match _action:
        case "Generate new ip report":
            date_question_keys = ["year", "month", "today_day", "start_day", "end_day"]

            date_questions = [
                inquirer.Text(date_question_keys[0], message="Enter a year: ", default=datetime.now().year),
                inquirer.Text(date_question_keys[1], message="Enter a month as a number from 1 to 12: ", default=datetime.now().month),
                inquirer.Text(date_question_keys[2], message="Enter a day of report creation: ", default=datetime.now().day),
                inquirer.Text(date_question_keys[3], message="Enter the start day of the report: ", default=1),
                inquirer.Text(date_question_keys[4], message="Enter the last day of the report: "),
            ]
            date_responses = inquirer.prompt(date_questions)

            year = int(date_responses[date_question_keys[0]])
            month = int(date_responses[date_question_keys[1]])
            today_day = int(date_responses[date_question_keys[2]])
            start_day = int(date_responses[date_question_keys[3]])
            end_day = int(date_responses[date_question_keys[4]])

            with open("files/last_report_date.txt", "w") as file:
                file.writelines(value + '\n' for value in date_responses.values())

            try:
                generator.createReport(datetime(year, month, today_day), datetime(year, month, start_day), datetime(year, month, end_day))
                print("Report successfully created, you can find it in files folder by the name of the month you requested!")
            except Exception as inst:
                utils.exceptionResponse(inst)   

        case "Convert report to pdf":
            converter_questions = [
                inquirer.Confirm("last", message="Should I convert last created report?", default=True)
            ]

            converter_responses = inquirer.prompt(converter_questions)

            if converter_responses["last"] == True:
                with open("files/last_report_date.txt", "r") as file:
                    date = file.readlines()

                converter.convertDocxToPdf(
                    datetime(int(date[0].strip('\n')), int(date[1].strip('\n')), int(date[2].strip('\n'))).strftime("%B")
                )
            else:
                file_name = [inquirer.Text("fileName", message="Provide the name of docx file from files folder to convert it to pdf: ")]
                file_name_responses = inquirer.prompt(file_name)
                converter.convertDocxToPdf(file_name_responses["fileName"])

        case _EXIT:
            break