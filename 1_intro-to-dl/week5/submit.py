import sys
import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(os.path.join(dir_path, "./../utils"))
import grader


# code_size = 71
# img_shape = (38, 38, 3)
def submit_char_rnn(submission, score, email, token):
    grader_ = grader.Grader("cULEpp2NEeemQBKZKgu93A")
    history, samples = submission
    assert len(samples) == 25
    grader_.set_answer("pttMO", int(np.mean(history[:10]) > np.mean(history[-10:])) )
    grader_.set_answer("uly0D", len(set(samples)))
    grader_.submit(email, token)

