import gspread
from zone import Zone

def send_drive(zone_detect,plate,position):
        #Credetentials
        gc = gspread.service_account(filename='./cred.json')
        #Open register file in Google Drive called Registro_Zona_de_Congestion
        #Link : https://docs.google.com/spreadsheets/d/1TECxIuV1aWixGHmgehQNgxml8An3d4u3RkvBJEt4UiI
        sheet = gc.open("Registro_Zona_de_Congestion")
        #Open worksheet 1
        worksheet = sheet.get_worksheet(0)
        ROW_NUMBER=len(worksheet.col_values(0))-1
        #Update cell formula
        FORMULA=f'VLOOKUP(C{ROW_NUMBER},\'Vehiculos registrados\'!$A$2:$B$25,2,FALSE)'
        #Append row in drive document
        worksheet.append_row(['=TODAY()',zone_detect,plate,position,FORMULA],value_input_option='USER_ENTERED')