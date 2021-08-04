# Intro
+ Save user operations, and error prone.
# Todos
- Display working file, reuturn status after clicking the button
- Display working messages (fail/ok) to GUI
- Write user working logs (new session, button click...) and save to text file
- JSON file -> more info: check info of each file, display file name and file size... MD5, and the folder it's working. maybe also the commands?
- Extracted back from parent folder -> index all temperatures file -> move/copy to destination folder (in this case des folder will be /KNAN_software/data)
- Move status message to append first of NUC folder name (so user can soft easier)
- More strict file type checking function (and more option for easy program change)
# Features
- User can point to 'Phan mem lay mau du lieu', the software then navigates to Data folder, NUC_Table, Log... (or by user selection dir paths) -> check the files:
+ copy finished FTDI to one folder automatically -> Ready to be copied to store disk.
+ The user can select parent nuc folder. -> and select temperature folder -> Add feature: export valid temperature data files (by checking name and size in subfolders...) to temperature folder (to be generated NUC in software again)
- Export to current folder: json file contains FAIL/OK folders only
- Better GUI
# Practices
- Clean code
# References
https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter

## JSON
https://stackoverflow.com/questions/53110610/json-dump-in-python-writing-newline-character-and-carriage-returns-in-file/57021651
