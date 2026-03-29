# Transfer-Stickers-from-Iphone-Backup-to-Android-Phone
I noticed that apple's iphones aren't able to import stickers for whatsapp or any other app for that matter. Trying to help a friend out I realized all the solutions were either paid, didn't work, or were super demanding (create packs of 30 strickers, won't work for those who have 1000++ stickers)
The process can be pretty lengthy and very annoying (at least it was for me trying to figure it out). The reason stickers and other files don't transfer over as well is mostly due to a few reasons; files are saved at a different format on iphones (webp for stickers), iphones lock up their storage so they're inaccessible...

The previous solutions I've seen are literally either just send yourself the stickers somehow, which if you have thousands would take forever, then save all of them by individually selecting each and every single one of them. Try some paid service which costs 10s of dollars, which doesn't guarantee it'll work and will most likely
download some bloatware on your phones, or use the method I've created. 

What my program does it that it takes the .txt file and searches all the files in the backup with matching names, then converts all of the files to the relevant format for stickers, ready for you to copy and paste them to your whatsapp stickers folder in your phone!

You'll need the following:

-Your Iphone backup from itunes (unencrypted, for this just back up and select the option to not encrypt the backup)

-An IDE program, a program that can run code you've written

-An SQL program, preferably SQL lite, you can look it up online and download it

Step 1: Perform a back up of your iphone on itunes. Select the option for the backup to not be encrypted.


Step 2: Go into the SQL lite program and open the Manifest Data Base File. Since your back up is entirely hidden with all the files being labelled as "File" type and the paths and the names of all the files are hashed (names such as "fd0ac159cd08da671ea7a6780edbc434299093d7")


Step 3: Once the Manifest file is open, in the search bar just look up the word "Sticker", you can look up "Whatsapp Sticker" if you want but just putting in stickers, should be more than enough. 


Step 4: In your search you'll have shortened down the list of all the files to the stickers, but the problem is that not all of those files are stickers and not all of those files even exist in the back up. Don't worry my program makes sure it exists in the backup. Copy Paste the FileID of all the sticker
files and put it in a file named "sticker_fileIDs.txt"


Step 5: Great you're almost there! Before you go to your IDE make sure you have python installed, the easiest way of doing this is to go into your Microsoft Store and installing it throught there or just looking up online and doing it.


Step 6: Go to your IDE and open the file "extract_convert_stickers.py"


Step 7: open a terminal for the file and run the following code " python -m pip install pillow". This is a library that we'll need to be able to convert the sticker files from iphone types to the android ones. 


Step 8: Create a folder in your files called "stickers verified"


Step 9: In the python file loo at these lines:
BACKUP_PATH = r"D:\Apple Computer\MobileSync\Backup\00008110-001202840EEB801E"
FILELIST_PATH = r"C:\Users\Ironnix\Downloads\sticker_fileIDs.txt"  # text file with fileIDs pasted
OUTPUT_PATH = r"C:\Users\Ironnix\Documents\stickers verified"
copy paste the file paths first back up is where your iphone backup is located, second file list is the .txt file where the names of all the sticker files are, and third output path is the path of the "stickers verified" folder I just had you create.


Step 10: RUN THE PROGRAM.


Step 11: verify the stickers in the folder and if they're there copy paste them into the relevant folder in your android phone.


Step 12: Enjoy!


