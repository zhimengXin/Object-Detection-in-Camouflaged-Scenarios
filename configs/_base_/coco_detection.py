# dataset settings
dataset_type = 'CocoDataset'
backend_args = None

train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True),
    # If you don't have a gt annotation, delete the pipeline
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        #data_root=data_root,
        ann_file='dataset/COD10K-D/train.json',
        data_prefix=dict(img = 'dataset/COD10K-D/train'
                         
                         ),
        filter_cfg=dict(filter_empty_gt=True, min_size=32),
        pipeline=train_pipeline,
        backend_args=backend_args)) 
val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
       
        # COD10K-D dataset
        ann_file='dataset/COD10K-D/test.json',
        data_prefix=dict(img='dataset/COD10K-D/test'),

        # CAMO-D dataset
        # ann_file='dataset/CAMO-D/test.json',
        # data_prefix=dict(img='dataset/CAMO-D/test'),

        # NC4K-D
        # ann_file='dataset/NC4K-D/test.json',
        # data_prefix=dict(img='dataset/NC4K-D/test'),

        test_mode=True,
        pipeline=test_pipeline,
        backend_args=backend_args))
test_dataloader = val_dataloader

val_evaluator = dict(
    type='CocoMetric',

    # COD10K-D dataset
    ann_file='dataset/COD10K-D/test.json',

    # CAMO-D dataset
    # ann_file='dataset/CAMO-D/test.json',

    # NC4K-D
    # ann_file='dataset/NC4K-D/test.json',
   

    metric='bbox',
    format_only=False,
    backend_args=backend_args)
test_evaluator = val_evaluator

