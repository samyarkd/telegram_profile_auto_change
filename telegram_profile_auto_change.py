from pyrogram import *
from pyrogram.handlers import *
from pyrogram.raw import functions, types, base
import asyncio
import shutil
import time
import glob
import Key
import sys
import os


api_id = Key.api_id
api_hash = Key.api_hash

app = Client('TPAC', api_id, api_hash)


while True:
    try:
        times = input('Enter the wait change time (second | 1h --> 3600s recommended ): ')
        try:
            times = int(times)
        except:
            pass
        
        if type(times) == int:
            while True:
                kb = input('\n A ---> reupload your profile pics (recommended) \n B ---> upload from "pics" folder \n Enter your choice (A or B <3): ')
                if kb in ['a', 'b' ,'A', 'B']:
                    break
            break
    except Exception:
        print('Enter int number!! ')

#



def main():

    # mood one : A

    if kb in ['a','A']:
        
        photos = app.get_profile_photos("me")
        pc = app.get_profile_photos_count('me')
        print(f'Download {pc} photos , please wait until complete !!')
    
        if os.path.exists('downloads'):
            shutil.rmtree('downloads')

        x = 0
        for p in photos:
            fid = p.file_id
            
            
            
            app.download_media(fid)
            print(p)
            x += 1
            sys.stdout.write('\r'+str(x) + f'/{pc} photos downloaded in downloads folder !')

        
        
        
        while True:
            for file in glob.glob('downloads/*.*'):
                print(file)
                app.set_profile_photo(photo=f"{file}")
                time.sleep(times)



# -------------------------------------------------

    # mood two : B
    elif kb in ['b','B']:
        while True:
            for file in glob.glob('pics/*.*'):
                print(file)
                app.set_profile_photo(photo=f"{file}")
                time.sleep(times)

app.start()
main()  
app.stop()
