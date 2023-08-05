import yolov5

def apple_counter(img_path):
# load pretrained model
    model = yolov5.load('best_apple_counter.pt')

    # or load custom model
    # model = yolov5.load('train/best.pt')
    
    # set model parameters
    model.conf = 0.70  # NMS confidence threshold
    model.iou = 0.20  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image

    # set image
    # img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'
    # img = r'C:\Users\HP\Desktop\apple_api\IMG-20230531-WA0009.jpg'
    img = img_path
    # perform inference
    results = model(img)

    # inference with larger input size
    results = model(img, size=1280)

    # inference with test time augmentation
    results = model(img, augment=True)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    print(len(results.pred[0]))
    return len(results.pred[0])
    # show detection bounding boxes on image
    # results.show()

    # save results into "results/" folder
    # results.save(save_dir='results/')