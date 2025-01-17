import os


class Config:
    DATA_DIR = '/kaggle/input/landmark-retrieval-2021'
    CSV_PATH = os.path.join(DATA_DIR, 'train.csv')
    train_batch_size = 10
    val_batch_size = 10
    num_workers = 8
    image_size = 512
    output_dim = 512
    hidden_dim = 1024
    input_dim = 3
    epochs = 100
    lr = 1e-4
    num_of_classes = 50
    pretrained = True
    model_name = 'resnet101'
    seed = 42
