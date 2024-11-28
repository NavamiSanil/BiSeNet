cfg = dict(
    model_type='bisenetv2',  # Model type (BiSeNetV2)
    n_cats=19,  # Number of categories in the dataset (Cityscapes has 19 classes)
    num_aux_heads=4,  # Number of auxiliary heads in the network
    lr_start=5e-3,  # Starting learning rate
    weight_decay=5e-4,  # Weight decay for regularization
    warmup_iters=1000,  # Number of warmup iterations
    max_iter=150000,  # Maximum number of training iterations
    dataset='CityScapes',  # Dataset name (Cityscapes)
    im_root='/kaggle/input/cityscapes/Cityspaces/leftImg8bit/',  # Path to images (leftImg8bit folder in the dataset)
    train_im_anns='/kaggle/working/BiSeNet/train.txt',  # Path to training annotation file
    val_im_anns='/kaggle/input/cityscapes/Cityspaces/val.txt',  # Path to validation annotation file
    scales=[0.25, 2.],  # Data augmentation scales (used for image resizing during training)
    cropsize=[512, 1024],  # Crop size during training (height, width)
    eval_crop=[1024, 1024],  # Crop size during evaluation (height, width)
    eval_scales=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],  # Scales for evaluation
    ims_per_gpu=8,  # Number of images to process per GPU during training
    eval_ims_per_gpu=2,  # Number of images to process per GPU during evaluation
    use_fp16=True,  # Enable mixed-precision (FP16) training
    use_sync_bn=True,  # Use synchronized batch normalization across multiple GPUs
    respth='./res',  # Path to store results and model checkpoints
)
