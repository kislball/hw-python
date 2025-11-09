class HuffmanFile:
    def __init__(self, file_name: str):
        self.file_object = open(file_object, 'rwb')

    def __enter__(self):
        return self

    def __exit__(self):
        self.file_object.close()
