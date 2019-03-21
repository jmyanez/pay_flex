

class Beneficiary:


    def __init__(self,employer_id):
        self.employer_id = employer_id

    employer_id = "0128248"
    division = "0000000000"
    member_number = "000000000"
    ssn = "000000000"
    first_name = " " * 20
    last_name = " " * 20
    middle_initial = " "
    birth_date = "mm/dd/yyyy"
    hire_date = "mm/dd/yyyy"
    # Can be either M/F
    gender = "M"
    employee_status_date = "mm/dd/yyyy"
    employee_status = " "
    address_1 = " " * 50
    address_2 = " " * 50
    city = " " * 20
    state = "XX"
    zip = "00000-0000"
    country = "USA"
    control = "0000000"
    suffix = "000"
    account = "000"
    copay_medical = " " * 10
    copay_dental = " " * 10
    copay_vision = " " * 10
    copay_rx = " " * 10
    # Either I or F
    coverage_level = "I"
    filler = " " * 81
    email = " " * 50
    payroll_schedule_id = "0000132982"
    bank_account_number = "0" * 17
    bank_routing_number = "0" * 17
    # SAV/CHK
    bank_account_type = "SAV"
    driver_licence_number = "0" * 15
    driver_licence_authority = "NE"
########################Election Information############################################################################
    plan_year_effective = "MM/DD/YYYY"
    account_type = "XX"
    election_effective_date = "MM/DD/YYYY"
    annual_deduction = "00000.00"
    annual_contribution = "00000.00"
    scheduled_deduction = "00000.00"
    scheduled_contribution = "00000.00"
    #Can be either T/F
    debit_card_selected = "T"
    auto_pay_dental = " "
    auto_pay_healthcare = " "
    auto_pay_vision = " "
    auto_pay_rx = " "
    fsa_first = " "
    election_expiration_date ="MM/DD/YYYY"
    ltdfsa_ded_met_date = "MM/DD/YYYY"
    ########################Additional Information############################################################################
    commuter_transit = "F"
    commuter_parking = "F"
    wellness_location = " "