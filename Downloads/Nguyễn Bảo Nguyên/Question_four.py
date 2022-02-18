import threading

def print_onehundred_thread():
    print("100")
    
def print_twohundreds_thread():
    print("200")
    
def question_four(n):
    for i in range(n):
        a = threading.Thread(target=print_onehundred_thread)
        b = threading.Thread(target=print_twohundreds_thread)
        a.start()
        b.start()

# You can modify an appropriate number of lines (n) , which you want to print out
n=8
question_four(n)