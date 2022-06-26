import cv2
import random
import dropbox
import time

start_time = time.time()

def take_snapShot():
    number=random.randint(0,100)
    videocaptureobj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobj.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        result=False
    print('snapShot taken')
    videocaptureobj.release()
    cv2.destroyAllWindows()
    return img_name


def upload_file(img_name):
    access_token='sl.BKQcJap3N4BKBRYi4VNXdQuuWMfctKTuvr2wiPN0Q-gK0Xc34HAWGCLHJS-v_yDQ1J7-uV9TovTppx08MOWXVIFmoR8SQtCJDHgIn11tKqmMbgTBvZVzhwmuVI3YJQyPYjygu7k'
    file=img_name
    file_from=file
    file_to='/c102/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('files uploaded')

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name=take_snapShot()
            upload_file(name)

main()