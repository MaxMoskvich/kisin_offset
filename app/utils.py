class SystemException(Exception):
    message = None
    error_log  = None
    
    def __init__(self, message, error_log = None):
        self.message = message
        self.error_log = error_log