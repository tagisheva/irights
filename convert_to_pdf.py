from docx2pdf import convert
import utils

def convertDocxToPdf(fileName):
    try:
        convert("files/" + fileName + ".docx", "files/" + fileName + ".pdf")
        print("Report successfully converted to pdf, you can find it in files folder by the name of the month you requested!")

    except Exception as inst:
        utils.exceptionResponse(inst)
                    
            

