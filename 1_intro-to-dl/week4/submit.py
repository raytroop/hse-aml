import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "./../utils"))
import grader


# code_size = 71
# img_shape = (38, 38, 3)
def submit_autoencoder(submission, score, email, token):
    grader_ = grader.Grader("9TShnp1JEeeGGAoCUnhvuA")
    encoder, decoder = submission
    grader_.set_answer("FtBSK", encoder.output_shape[1])
    grader_.set_answer("83Glu", decoder.output_shape[1:])
    grader_.set_answer("fnM1K", score)
    grader_.submit(email, token)
