import cv2
import dropbox
import random
import time
import dropbox

start_time = time.time()

def Take_snapshot():
    number = random.randint(1, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame= videoCaptureObject.read()
        imageName = 'img'+str(number)+'.jpg'
        cv2.imwrite(imageName, frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print('Snapshot Taken')
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = 'sl.A_ayg-LAf9VQfhxbBemZ1U5oSLWiNqTaeA_EJ63s78q6xKaVfE9Ve9hxHyACwGaBUhCReaEi3zy0v41n3C2Ktk-9TTVZdMgTww_vFHNw0yA-hWcU8KiN97TqqGIOTJjIs0ugE3clSsM7'
    file_from = imageName
    file_to = '/test_dropbox/'+imageName  # The full path to upload the file to, including the file name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if ((time.time()-start_time)>=5):
            name = Take_snapshot()
            upload_file(name)

main()