from scipy import io
import torch

def pkl2mat(filename = '0.pkl',output_file=''):
    data = torch.load(filename)
    if output_file == '':
        output_file = filename
    output_file = update_filename(output_file)
    raw_data, information = data[0],data[1]
    information = dict(information)
    information['data'] = raw_data
    io.savemat(output_file,information)


def update_filename(filename):
    index = filename.rfind('.pkl')
    return filename[:index] + '.mat'

