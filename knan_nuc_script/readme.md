# Intro
+ Save user operations, and error prone.
# Todos
- Display working file, return status after clicking the button. And the folder status
- Display working messages (fail/ok) to GUI
- Write user working logs (new session, button click...) and save to text file
- JSON file -> more info: check info of each file, display file name and file size... MD5, and the folder it's working. maybe also the commands?
- Extracted back from parent folder -> index all temperatures file -> move/copy to destination folder (in this case des folder will be /KNAN_software/data)
- Move status message to append first of NUC folder name (so user can soft easier)
- More strict file type checking function (and more option for easy program change)
# Features
- User can point to 'Phan mem lay mau du lieu', the software then navigates to Data folder, NUC_Table, Log... (or by user selection dir paths) -> check the files:
+ Copy finished FTDI to one folder automatically -> Ready to be copied to store disk.
+ The user can select parent nuc folder. -> and select temperature folder -> Add feature: export valid temperature data files (by checking name and size in subfolders...) to temperature folder (to be generated NUC in software again)
- Export to current folder: json file contains FAIL/OK folders only -> Done for 2 functions
- Better GUI design.
- Data structure: Link between FTDI and device serial
- Display usage text when user hovers to button (manual)
- Add scroll text box to display print message...
# Vietnamese
- Thêm hiển thị thông tin của working directory: có bao nhiêu files, bao nhiêu files đã hoàn thiện, sẵn sàng để copy qua thư mục đích (sử dụng trên máy lấy NUC)… 
- Phần mềm sẽ thường được sử dụng trên 2 máy: máy lấy NUC, máy gen NUC.
- Trên máy lấy NUC: Thêm chức năng gom files vào folder tương ứng nếu đủ các files (9 files nhiệt độ) và dung lượng -> click là có thể copy sang máy khác để gen nuc. Đồng thời hiển thị thông tin của folder KNAN_software đấy (bằng cách click vào). 
- Trên máy gen NUC: Gom files vào folder đối với các thiết bị đã gen xong, đủ files, và Log message đạt yêu cầu (15 files). Click xong là có thể copy sang ổ đĩa HDD để lưu trữ.

# Practices
- Clean code
# References
https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter

## JSON
https://stackoverflow.com/questions/53110610/json-dump-in-python-writing-newline-character-and-carriage-returns-in-file/57021651
