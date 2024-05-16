Business needs:
    An image upscaling solution to enhance the resolution of photos, 
    catering to various use cases such as improving image quality for 
    digital media, surveillance systems, medical imaging, and more.

Requirements:
    numpy
    cv2
    h5py
    matplotlib
    torch
    tqdm
    scikit-learn

Running:
    To run model, you need to install all libraries from 'requirements.txt'. 
    To do this you need to open command line in project and write command 'pip install requirements.txt'.
    After this you can put you photos in 'user_photos/' run 'test.py' and 
    get your upscaled photo results in 'output/upscaled_photos/'.

Training a Model:
    To train model on other photo data, you need to change photos in 'input/train_photos/'. 
    After this run 'data_preperation.py' and 'train.py', your new model will be saved in 'model_info/'