#validações
def validate_name(name):
    return name.isalpha()
def validate_date(date_init, date_end):
    return date_init <= date_end
