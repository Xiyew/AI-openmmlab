_base_=['mask_rcnn_r50_fpn_2x_coco.py']


model = dict(roi_head=dict(bbox_head=dict(num_classes=1),mask_head=dict(num_classes=1)))

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train=dict(
        ann_file='/input0/train/coco.json',
        img_prefix='/input0/train/',
        classes=('balloon',)
    ),
    val=dict(
        ann_file='/input0/val/coco.json',
        img_prefix='/input0/val/',
        classes=('balloon',)
    ),
    test=dict(
        ann_file='/input0/val/coco.json',
        img_prefix='/input0/val/',
        classes=('balloon',)
    )
)
runner = dict(type='EpochBasedRunner', max_epochs=8)
optimizer = dict(type='SGD', lr=0.001)
lr_config = None
log_config = dict(interval=10, hooks=[dict(type='TextLoggerHook')])
load_from='mask_rcnn_r50_fpn_2x_coco_bbox_mAP-0.392__segm_mAP-0.354_20200505_003907-3e542a40.pth'