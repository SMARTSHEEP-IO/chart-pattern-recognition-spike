from ultralyticsplus import YOLO, render_result

model = YOLO("stockmarket-pattern-detection-yolov8/best.pt")

# set model parameters
model.overrides['conf'] = 0.15  # NMS confidence threshold
model.overrides['iou'] = 0.35  # NMS IoU threshold
model.overrides['agnostic_nms'] = True  # NMS class-agnostic
model.overrides['max_det'] = 100  # maximum

image="image/1.png"

results = model.predict(image)

# observe results
print(results[0].boxes)
render = render_result(model=model, image=image, result=results[0])
render.show(title="Pattern")


