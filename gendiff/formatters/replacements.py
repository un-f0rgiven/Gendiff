replacements = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def replace_values(formatted_output, replacements):
    for old_value, new_value in replacements.items():
        # Заменяем старое значение на новое
        formatted_output = formatted_output.replace(str(old_value), new_value)
    return formatted_output
