class FileManager:
    def __init__(self, filename):
        self.pisz = open(filename, 'r+')
    def update_file(self):
        text_data = '\nUpdate done'
        self.pisz.write(text_data)
    def read_file(self):
        czytaj=self.pisz.read()
        print(czytaj)
    def zamknij(self):
        self.pisz.close()