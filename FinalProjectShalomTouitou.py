import tkinter as tk


FONT_SIZE = 12

# Background root color
root_bg_color = "#%02x%02x%02x" % (128, 192, 200)


def init():
    all_letters = [chr(ord('a') + i) for i in range(ord('z') - ord('a') + 1)]
    all_capital_letters = [chr(ord('A') + i)
                           for i in range(ord('Z') - ord('A') + 1)]
    all = []
    for i in range(len(all_letters)):
        all.append(all_letters[i])
    for i in range(len(all_capital_letters)):
        all.append(all_capital_letters[i])
    return all

# This is the Encryption logic
def encryption(text_to_encrypt, move=15):
    enc = []
    dec = []
    i = 0
    letter_enc = {}
    letter_dec = {}
    while (len(enc) != len(text_to_encrypt)):
        j = move
        while (text_to_encrypt[(i) % (len(text_to_encrypt))] in (enc)):
            i = i + 1
        while (text_to_encrypt[(i + j) % (len(text_to_encrypt))] in (dec)):
            j = j + 1
        # Original text
        original = text_to_encrypt[(i) % (len(text_to_encrypt))]
        # Replace text
        replaced = text_to_encrypt[(i + j) % (len(text_to_encrypt))]
        letter_enc[original] = replaced
        letter_dec[replaced] = original
        enc.append(original)
        dec.append(replaced)
    return (letter_enc, letter_dec)


# This do the Encry/Decry 
def to_mode(mode_map, text):
    str = ""
    for i in range(len(text)):
        if text[i] in mode_map:
            str += mode_map[text[i]]
        else:
            str += text[i]
    return str


# This is the select Mode Enrypt / Decrypt
def selected_mood(root):
    selected_button_mood = tk.IntVar()

    mode_enc_btn = tk.Radiobutton(
        root, text=' Encryption ', value=1, variable=selected_button_mood)
    mode_dec_btn = tk.Radiobutton(
        root, text=' Decryption ', value=2, variable=selected_button_mood)

    mode_enc_btn.place(x=250, y=100)
    mode_dec_btn.place(x=100, y=100)

    def mode():
        mode_enc_btn.focus_displayof()
        mode_dec_btn.focus_displayof()
        submit_mode_btn.place_forget()
        value_of_mode = (selected_button_mood.get() == 1)
        input_type(root, value_of_mode)

    submit_mode_btn = tk.Button(
        root, text='Choose your mode', command=mode)
    submit_mode_btn.place(x=400, y= 100)


# Here choose the type of output
def output_type(root, message):
    selected_output_type = tk.IntVar()

    btn_text = tk.Radiobutton(
        root, text=' Output by text ', value=1, variable=selected_output_type)
    btn_file = tk.Radiobutton(
        root, text=' Output to file ', value=2, variable=selected_output_type)

    btn_text.place(x=100, y=250)
    btn_file.place(x=250, y=250)

    def submit_output_type():
        if (selected_output_type.get() == 1):
            display_mode_message_by_text = tk.Label(root)
            display_mode_message_by_text.place(x=150, y=350)
            display_mode_message_by_text.config(text=message,font=(None, FONT_SIZE+12))

            submit_mode_btn.place_forget()
        else:
            # write to file
            display_mode_message_by_text = tk.Label(root)
            display_mode_message_by_text.place(x=150, y=350)

            f = open("answer.txt", "a")
            f.write(message)
            f.close()

            file_message = "Saved on file : answer.txt"
            display_mode_message_by_text.config(text=file_message,font=(None, FONT_SIZE+5))

    submit_mode_btn = tk.Button(
        root, text='Submit mode', command=submit_output_type)
    submit_mode_btn.place(x=400, y=250)


# This is the Input Type that we want to choose
def input_type(root, mode_is_enc):
    (letter_enc_map, letter_dec_map) = encryption(init())
    mode_of_operation = letter_enc_map
    mode_of_operation_message = "Enc"

    if mode_is_enc == 0:
        mode_of_operation = letter_dec_map
        mode_of_operation_message = "Dec"

    selected_input_type = tk.IntVar()  

    # Here's give the value to the choosen mode
    display_text_message = mode_of_operation_message + ' by text '
    button_enc_selected_by_text = tk.Radiobutton(
        root, text=display_text_message, value=1, variable=selected_input_type)

    # Here's give the value to the choosen mode
    display_file_message = mode_of_operation_message + ' by file '
    button_enc_selected_by_file = tk.Radiobutton(
        root, text=display_file_message, value=2, variable=selected_input_type)


    # Other option:
    def has_clicked_on_enc_button():  # correct

        txt_input = tk.Entry(root)
        txt_input.place(x=100, y=200)
        if selected_input_type.get() == 1:
            def clicked():
                print(txt_input.get())
                output_text = to_mode(mode_of_operation, txt_input.get())
                res = "Your " + mode_of_operation_message + " is: " + output_text
                button.place_forget()

                output_type(root, res)

            button = tk.Button(root, text="Insert text", command=clicked)
            button.place(x=400, y=200)
        else:
            def clicked():
                print(txt_input.get())
                file_name = txt_input.get()  # the file name.
                with open(file_name, 'r') as file:
                    input_message = file.read()
                output_text = to_mode(mode_of_operation, input_message)
                res = "Return default the name: " + output_text

                button.place_forget()

                output_type(root, res)

            button = tk.Button(root, text="Insert file name", command=clicked)
            button.place(x=300, y=200)
        button_submit_type_of_input.place_forget()

    # Creating and clearing button.
    button_submit_type_of_input = tk.Button(
        root, text="Submit type ", command=has_clicked_on_enc_button)

    button_submit_type_of_input.place(x=400, y= 150)

    button_enc_selected_by_text.place(x=250, y=150)

    button_enc_selected_by_file.place(x=100, y=150)



# this is the main 
def main():
    root = tk.Tk()
    # App title
    root.title("Final Project Shalom Touitou")
    # Size
    root.geometry("550x550+300+50")
    # Not resizeble 
    root.resizable(width=False, height=False)
    # Attributes
    root.attributes("-toolwindow", True)
    root.attributes("-topmost", True)
    # filename = tk.PhotoImage(file="image.png")
    background_label = tk.Label(root, bg=root_bg_color)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # upper Frame
    upper_frame = tk.Frame(root,bg=root_bg_color )
    lbl = tk.Label(upper_frame, text="Welcome to TKINTER Decrypt/Encrypt",bg=root_bg_color, fg ="white", font=(None, FONT_SIZE+5))
    # Place the message
    lbl.pack(ipady=5, ipadx=10)  
    lbl_sub= tk.Label(upper_frame,text="This is a Tkinter GUI to assist you Encrypt and Decrypt secret messages.\n *Please follow the steps*", bg=root_bg_color,fg="white",font=(None, FONT_SIZE))
    # Place the lbl_sub
    lbl_sub.pack(ipady=5, ipadx=10)
    # Place the upper frame
    upper_frame.place(x=1, y=1)  
    
    selected_mood(root)

    root.mainloop()


main()
