from picamera2 import Picamera2, Preview
import cv2
import numpy as np

def capture_hdr_image(exposure_times):
    picam2 = Picamera2()
    picam2.start_preview(Preview.QTGL)

    images = []
    for exposure in exposure_times:
        picam2.set_controls({"ExposureTime": exposure})
        picam2.start()
        image = picam2.capture_array()
        images.append(image)
        picam2.stop()

    picam2.stop_preview()

    # Merge images to create HDR
    merge_debevec = cv2.createMergeDebevec()
    hdr = merge_debevec.process(images, times=np.array(exposure_times, dtype=np.float32))

    # Tonemap HDR image
    tonemap = cv2.createTonemapDurand(gamma=2.2)
    ldr = tonemap.process(hdr)

    # Convert to 8-bit image
    ldr = np.clip(ldr * 255, 0, 255).astype('uint8')

    return ldr

# Example usage
if __name__ == "__main__":
    exposure_times = [1000, 10000, 100000]  # Example exposure times in microseconds
    hdr_image = capture_hdr_image(exposure_times)
    cv2.imwrite("hdr_image.jpg", hdr_image)