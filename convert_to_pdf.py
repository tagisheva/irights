from docx2pdf import convert
from helpers.constants import today_datetime

convert("files/" + today_datetime.strftime("%B") + ".docx", "files/" + today_datetime.strftime("%B") + ".pdf")


