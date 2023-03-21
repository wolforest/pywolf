

class Result:
    def __init__(self, rows=None, count=0, affect_rows=0, row=None):
        pass

    def set_rows(self, rows):
        self.rows = rows
        return self

    def set_row(self, row):
        self.row = row
        return self

    def set_count(self, count):
        self.count = count
        return self  

    def set_affect_rows(self, affect_rows):
        self.affect_rows = affect_rows
        return self  
    
    def get_count(self) -> int:
        return 0

    def get_rows(self) -> list:
        return []

    def get_row(self) -> dict:
        return {}

    def get_affect_rows(self) -> int:
        return 0
    
    def get_cloumn(self, column):
        return None