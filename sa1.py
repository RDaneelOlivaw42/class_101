import dropbox

class Transfer_Data():

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():

    access_token = 'sl.BJliU7yCq1Le28_ox6jzaC2V_jLpRFbkGj5QyRkpzEu830hg1jJ_pWZQXfY5L1QEqfZF-kQaNhY7lQeQYaW7YE2_uC5GwL4lrZcp25ozoHvg07okYheos2n_2QXfM8xF2W-LQcuCY1M'

    transfer_data = Transfer_Data(access_token)
    file_from = input("Enter the file path to be transferred ")
    file_to = input("Enter the full path to be uploaded to Dropbox ")

    transfer_data.upload_file(file_from, file_to)
    print("File has been moved")

main()