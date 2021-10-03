class Util:

    @staticmethod
    def check_repeated_elements(list):
        s = set()
        for element in list:
            if element in s:
                return element
            s.add(element)
        return None
