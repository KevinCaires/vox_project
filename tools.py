RESPONSE_LIST = ['OI SUMIDA', 'APAGAR', 'LUZ']

class StandardResponses:
    def get_command(command):  # pylint: disable=no-self-argument
        if command.upper() in RESPONSE_LIST:  # pylint: disable=no-member
            if command.upper() == 'LUZ':  # pylint: disable=no-member
                return 'Ascendeu'
            
            if command.upper() == 'APAGAR':  # pylint: disable=no-member
                return 'A luz foi apagada!'

            if command.upper() == 'OI SUMIDA':  # pylint: disable=no-member
                return 'Sai encosto!'

        return 'Não me incomode!'
