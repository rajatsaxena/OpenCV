import numpy as np
import cv2

def load_templates(tpls, title, file1, file2):
    im1 = cv2.imread(file1, 0)
    im2 = cv2.imread(file2, 0)
    if not im1 == None and not im2 == None:
        tpls[title] = { 'frame_start': im1, 'frame_end': im2 }


def detect_commercials(gray, tpls, title):
    if title:
        if template_match(gray, tpls[title]['frame_end']):
            title = ""
    else:
        for t, tpl in tpls.iteritems():
            if template_match(gray, tpl['frame_start']):
                title = t
    return title


def template_match(ref, tpl):
    res = cv2.matchTemplate(ref, tpl, cv2.TM_SQDIFF_NORMED)
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(res)
    return (minval <= 0.1)


def draw_text(im, label):
    if label:
        h, w = im.shape[:2]
        cv2.rectangle(im, (4, 4), (w-4, h-4), (0,0,255), 4)
        cv2.rectangle(im, (4, 4), (115, 25), (0,0,255), -1)
        cv2.putText(im, label, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255))


if __name__ == "__main__":
    tpls = {}
    load_templates(tpls, "Entrasol", "entrasol_start.png", "entrasol_end.png")
    load_templates(tpls, "Top Coffee", "top_coffee_start.png", "top_coffee_end.png")
    cap = cv2.VideoCapture("tv.mpg")
    if not cap.isOpened():
        import sys
        print "Cannot open video file!"
        sys.exit()
    title = ""
    while True:
        ok, frame = cap.read()
        if not ok:
            break;
        gray = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
        title = detect_commercials(gray, tpls, title)
        draw_text(frame, title)
        cv2.imshow("TV commercials detection", frame)
        if cv2.waitKey(40)% 0x100 == ord('q'):
            break

