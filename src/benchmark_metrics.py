# TensorFlow
TENSORFLOW2_TRAINING_CPU_SYNTHETIC_THRESHOLD = 50
TENSORFLOW2_TRAINING_GPU_SYNTHETIC_THRESHOLD = 7000
TENSORFLOW2_TRAINING_GPU_IMAGENET_THRESHOLD = 7000
# unit of tensorflow inference threshold is s
TENSORFLOW2_INFERENCE_CPU_THRESHOLD = {"INCEPTION": 0.06,
                                       "RCNN-Resnet101-kitti": 0.65,
                                       "Resnet50v2": 0.35,
                                       "MNIST": 0.00045,
                                       "SSDResnet50Coco": 0.4}
TENSORFLOW2_INFERENCE_GPU_THRESHOLD = {"INCEPTION": 0.04,
                                       "RCNN-Resnet101-kitti": 0.06,
                                       "Resnet50v2": 0.014,
                                       "MNIST": 0.0024,
                                       "SSDResnet50Coco": 0.1}
TENSORFLOW2_SM_TRAINING_CPU_1NODE_THRESHOLD = 30
TENSORFLOW2_SM_TRAINING_CPU_4NODE_THRESHOLD = 20
TENSORFLOW2_SM_TRAINING_GPU_1NODE_THRESHOLD = 5000
TENSORFLOW2_SM_TRAINING_GPU_4NODE_THRESHOLD = 4000

TENSORFLOW1_TRAINING_CPU_SYNTHETIC_THRESHOLD = 50
TENSORFLOW1_TRAINING_GPU_SYNTHETIC_THRESHOLD = 5000
TENSORFLOW1_TRAINING_GPU_IMAGENET_THRESHOLD = 5000
TENSORFLOW1_INFERENCE_CPU_THRESHOLD = {"INCEPTION": 0.06,
                                       "RCNN-Resnet101-kitti": 0.65,
                                       "Resnet50v2": 0.35,
                                       "MNIST": 0.00045,
                                       "SSDResnet50Coco": 0.4}
TENSORFLOW1_INFERENCE_GPU_THRESHOLD = {"INCEPTION": 0.04,
                                       "RCNN-Resnet101-kitti": 0.06,
                                       "Resnet50v2": 0.014,
                                       "MNIST": 0.0024,
                                       "SSDResnet50Coco": 0.1}

# MXNet
MXNET_TRAINING_CPU_CIFAR_THRESHOLD = 1000
MXNET_TRAINING_GPU_IMAGENET_THRESHOLD = 4500
MXNET_INFERENCE_CPU_IMAGENET_THRESHOLD = 100
MXNET_INFERENCE_GPU_IMAGENET_THRESHOLD = 4500

# PyTorch
PYTORCH_TRAINING_GPU_SYNTHETIC_THRESHOLD = 2400
PYTORCH_TRAINING_GPU_IMAGENET_THRESHOLD = 660
# unit of pytorch inference threshold is ms
PYTORCH_INFERENCE_CPU_THRESHOLD = {"ResNet18": 0.08,
                                   "VGG13": 0.45,
                                   "MobileNetV2": 0.06,
                                   "GoogleNet": 0.12,
                                   "DenseNet121": 0.15,
                                   "InceptionV3": 0.25}
PYTORCH_INFERENCE_GPU_THRESHOLD = {"ResNet18": 0.00075,
                                   "VGG13": 0.004,
                                   "MobileNetV2": 0.013,
                                   "GoogleNet": 0.018,
                                   "DenseNet121": 0.04,
                                   "InceptionV3": 0.03}
