from Beneficiary import Beneficiary
import pandas as pd
import numpy as np


def create_header():
    record_indicator = "H"
    format_type = "F"
    #Layout type can be either E, Eligibility or D, payroll
    layout_type = "E"
    date_created = "20190319"
    time_created = "103000"
    employer_id = "0128248"
    employer_name = "County Of El Paso"
    memo = ""
    layout_version = "v20190312"
    online_enrollment = "T"
    online_commuter = "F"
    #This file includes updates or changes only, not full file? T/F
    change_only = "F"

    header = " " * 200
    header = header[:0] + record_indicator + header[2:]
    header = header[:1] + format_type + header[3:]
    header = header[:2] + layout_type + header[4:]
    header = header[:3] + date_created + header[12:]
    header = header[:11] + time_created + header[18:]
    header = header[:17] + employer_id + header[25:]
    header = header[:24] + employer_name + header[75:]
    header = header[:108] + online_enrollment + header[110:]
    header = header[:109] + online_commuter + header[111:]
    header = header[:110] + change_only + header[112:]

    header = header[0:111]

    return header


def create_trailer(number_of_record):
    record_indicator = "T"
    record_count = str(number_of_record)
    trailer =""
    trailer = trailer[:0] + record_indicator
    trailer = trailer[:1] + record_count + trailer[12:]
    print(trailer)
    return trailer

def generate_beneficiary(information):
    new_beneficiary = Beneficiary("0128248")
    new_beneficiary.member_number = information[5]
    new_beneficiary.ssn = information[5]
    new_beneficiary.first_name = information[6]
    new_beneficiary.last_name = information[8]
    new_beneficiary.birth_date = information[10]
    new_beneficiary.employee_status_date = information[16]
    new_beneficiary.employee_status = information[14]
    new_beneficiary.address_1 = information[17]
    new_beneficiary.city = information[18]
    new_beneficiary.state = information[19]
    new_beneficiary.zip = information[20]
    #Section2
    new_beneficiary.plan_year_effective = information[1]
    new_beneficiary.account_type = information[0]
    new_beneficiary.election_effective_date = information[1]
    new_beneficiary.annual_deduction = information[25]
    new_beneficiary.annual_contribution = information[26]
    new_beneficiary.copay_medical = " " * 10



    format_beneficiary(new_beneficiary)
    new_beneficiary_list = convert_object_to_list(new_beneficiary)
    # print(new_beneficiary.employee_status_date)
    return  new_beneficiary_list

def format_beneficiary(new_beneficiary):
    #Change the filed depending on the type of plan they have HSA/FSA
    if(new_beneficiary.employee_status == "Active"):
        new_beneficiary.employee_status = " "
        new_beneficiary.employee_status_date = " "
    else:
        new_beneficiary.employee_status = "T"


    if(new_beneficiary.account_type == "Health Savings Account 2019"):
        new_beneficiary.control = "0866233"
        new_beneficiary.account_type = "16"
        new_beneficiary.suffix = "012"
        new_beneficiary.account = "00"
    elif(new_beneficiary.account_type =="Healthcare FSA 2019"):
        new_beneficiary.control = "0866267"
        new_beneficiary.account_type="05"
        new_beneficiary.suffix = "010"
        new_beneficiary.account = "001"
    if(new_beneficiary.employee_status_date == np.nan):
        new_beneficiary.employee_status_date = "X"

    new_beneficiary.ssn = str(new_beneficiary.ssn)
    new_beneficiary.member_number = str(new_beneficiary.member_number)
    new_beneficiary.annual_deduction = str(new_beneficiary.annual_deduction)
    new_beneficiary.annual_contribution = str(new_beneficiary.annual_contribution)

def convert_object_to_list(new_beneficiary):
    my_beneficiary_list = " " * 1000
    my_beneficiary_list = my_beneficiary_list[:0] + new_beneficiary.employer_id + my_beneficiary_list[10:]
    my_beneficiary_list = my_beneficiary_list[:17] + new_beneficiary.member_number + my_beneficiary_list[27:]
    my_beneficiary_list = my_beneficiary_list[:26] + new_beneficiary.ssn + my_beneficiary_list[36:]
    my_beneficiary_list = my_beneficiary_list[:35] + new_beneficiary.first_name + my_beneficiary_list[56:]
    my_beneficiary_list = my_beneficiary_list[:55] + new_beneficiary.last_name + my_beneficiary_list[76:]
    my_beneficiary_list = my_beneficiary_list[:76] + new_beneficiary.birth_date + my_beneficiary_list[87:]
    my_beneficiary_list = my_beneficiary_list[:97] + new_beneficiary.employee_status_date + my_beneficiary_list[108:]
    my_beneficiary_list = my_beneficiary_list[:107] + new_beneficiary.employee_status + my_beneficiary_list[109:]
    my_beneficiary_list = my_beneficiary_list[:108] + new_beneficiary.address_1 + my_beneficiary_list[159:]
    my_beneficiary_list = my_beneficiary_list[:208] + new_beneficiary.city + my_beneficiary_list[229:]
    my_beneficiary_list = my_beneficiary_list[:228] + new_beneficiary.state + my_beneficiary_list[231:]
    my_beneficiary_list = my_beneficiary_list[:230] + new_beneficiary.zip + my_beneficiary_list[241:]
    my_beneficiary_list = my_beneficiary_list[:240] + new_beneficiary.country + my_beneficiary_list[244:]
    my_beneficiary_list = my_beneficiary_list[:243] + new_beneficiary.control + my_beneficiary_list[251:]
    my_beneficiary_list = my_beneficiary_list[:250] + new_beneficiary.suffix + my_beneficiary_list[254:]
    my_beneficiary_list = my_beneficiary_list[:253] + new_beneficiary.account + my_beneficiary_list[257:]
    my_beneficiary_list = my_beneficiary_list[:428] + new_beneficiary.payroll_schedule_id + my_beneficiary_list[439:]
    my_beneficiary_list = my_beneficiary_list[:492] + new_beneficiary.plan_year_effective + my_beneficiary_list[503:]
    my_beneficiary_list = my_beneficiary_list[:502] + new_beneficiary.account_type + my_beneficiary_list[505:]
    my_beneficiary_list = my_beneficiary_list[:504] + new_beneficiary.election_effective_date + my_beneficiary_list[515:]
    my_beneficiary_list = my_beneficiary_list[:514] + new_beneficiary.annual_deduction + my_beneficiary_list[523:]
    my_beneficiary_list = my_beneficiary_list[:522] + new_beneficiary.annual_contribution + my_beneficiary_list[531:]
    my_beneficiary_list = my_beneficiary_list[:546] + new_beneficiary.debit_card_selected + my_beneficiary_list[547:]
    my_beneficiary_list = my_beneficiary_list[:547] + new_beneficiary.auto_pay_dental + my_beneficiary_list[548:]
    my_beneficiary_list = my_beneficiary_list[:548] + new_beneficiary.auto_pay_healthcare + my_beneficiary_list[550:]
    my_beneficiary_list = my_beneficiary_list[:549] + new_beneficiary.auto_pay_vision + my_beneficiary_list[551:]
    my_beneficiary_list = my_beneficiary_list[:550] + new_beneficiary.auto_pay_rx + my_beneficiary_list[552:]
    my_beneficiary_list = my_beneficiary_list[:572] + new_beneficiary.commuter_transit + my_beneficiary_list[574:]
    my_beneficiary_list = my_beneficiary_list[:573] + new_beneficiary.commuter_parking + my_beneficiary_list[575:]
    my_beneficiary_list = my_beneficiary_list[0 : 584]
    return my_beneficiary_list



def generate_file():
    InputFile = "C:/Users/Jmyanez-TEB/Desktop/payflexx.csv"
    OutputFile= "C:/Users/Jmyanez-TEB/Desktop/0128248_Eligibility_20190320_103000.txt"
    my_file = open(OutputFile,"w")
    my_header = create_header()
    my_file.write(my_header+"\n")

    users = pd.read_csv(InputFile)
    users.replace(np.nan, '', regex=True)

    count_rows = users.shape[0]
    count_coulumns = users.shape[1]
    for x in range(count_rows):
        user_info = users.values[x]
        my_beneficiary = generate_beneficiary(user_info)
        # print(my_beneficiary)
        my_file.write(my_beneficiary +"\n")
    my_trailer = create_trailer(count_rows+2)
    my_file.write(my_trailer)
    my_file.close()



generate_file()
# create_header()
# create_demographics()



