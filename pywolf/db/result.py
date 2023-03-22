

class Result:
    @staticmethod
    def from_affected_rows(affected_rows):
        return Result().set_affected_rows(affected_rows)

    @staticmethod
    def from_rows(rows):
        return Result().set_rows(rows)
    
    @staticmethod
    def from_row(row):
        return Result().set_row(row)
    
    @staticmethod
    def from_last_id(id):
        return Result().set_last_id(id)

    @staticmethod
    def from_count(count):
        return Result().set_count(count)
    
    def __init__(self) -> None:
        self.data = []
        self.affected_rows = 0
        self.count = 0
        self.last_id = 0

    def set_rows(self, rows):
        if not isinstance(rows, list):
            raise SyntaxError('invalid db.result.rows format')

        self.data.append(rows)
        return self

    def set_row(self, row):
        if not isinstance(row, dict):
            raise SyntaxError('invalid db.result.row format')

        self.data.append(row)
        return self

    def set_last_id(self, id):
        self.last_id = id
        return self 

    def set_count(self, count):
        self.count = count
        return self  

    def set_affected_rows(self, affected_rows):
        self.affected_rows = affected_rows
        return self  
    
    def get_count(self) -> int:
        return self.count

    def get_rows(self) -> list:
        return self.data

    def get_row(self) -> dict:
        if len(self.data) < 1:
            return {}
        
        return self.data[0]

    def get_last_id(self):
        return self.last_id 

    def get_affected_rows(self) -> int:
        return self.affected_rows
    
    def get_cloumn(self, column):
        if len(self.data) < 1:
            return None
        
        if column not in self.data[0]:
            return None
        
        return self.data[0].get(column)